"""
# Author - shubham.gupta@zeno.health
# Purpose - script with DSS write action for premium customer
"""

import argparse
import os
import sys
from datetime import datetime as dt

from dateutil.tz import gettz

sys.path.append('../../../..')

from zeno_etl_libs.helper.aws.s3 import S3
from zeno_etl_libs.db.db import DB
from zeno_etl_libs.helper import helper
from zeno_etl_libs.logger import get_logger
from zeno_etl_libs.helper.email.email import Email
from zeno_etl_libs.helper.parameter.job_parameter import parameter

parser = argparse.ArgumentParser(description="This is ETL script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False)

args, unknown = parser.parse_known_args()
env = args.env
os.environ['env'] = env
job_params = parameter.get_params(job_id=42)
email_to = job_params['email_to']

logger = get_logger()

# params
# Segment calculation date should be 1st of every month

try:
    period_end_d_plus1 = job_params['period_end_d_plus1']
    period_end_d_plus1 = str(dt.strptime(period_end_d_plus1, "%Y-%m-%d").date())
    period_end_d_plus1 = period_end_d_plus1[:-3] + '-01'
except ValueError:
    period_end_d_plus1 = dt.today().strftime('%Y-%m') + '-01'

logger.info(f"segment calculation date : {period_end_d_plus1}")

read_schema = 'prod2-generico'
table_name = 'premium-segment'

rs_db = DB()
rs_db.open_connection()

s3 = S3()

table_info = helper.get_table_info(db=rs_db, table_name=table_name, schema=read_schema)
logger.info(table_info)
if isinstance(table_info, type(None)):
    logger.info(f"table: {table_name} do not exist")

s = f"""
        select
            t1."patient-id",
            pm."primary-store-id"::int,
            'premium-customer' as "type",
            date('{period_end_d_plus1}') as "segment-calc-date",
            percent_rank() over ( partition by pm."primary-store-id" order by random()) "rank-pharmacist",
            (case 
                when "rank-pharmacist" <=0.25 then 1 
                when "rank-pharmacist" <=0.5 then 2
                when "rank-pharmacist" <=0.75 then 3
                when "rank-pharmacist" <=1 then 4
            end)::int "assign-pharmacist"
        from
            ((
            select
                x1."patient-id"
            from
                (
                select
                    date_trunc('month', rm."created-at") as "month",
                    rm."patient-id",
                    row_number () over(partition by rm."patient-id"
                order by
                    "month" desc ) as "rn",
                    dateadd(month,
                    "rn"-1,
                    "month") as "plus_date"
                from
                    "prod2-generico"."retention-master" rm
                group by
                    date_trunc('month', rm."created-at"),
                    rm."patient-id"
            )x1
            where
                x1."plus_date" = date_trunc('month', dateadd(month , -1 , date('{period_end_d_plus1}')))
                and x1."rn" = 3)
        union
        (
        select
            x1."patient-id"
        from
            (
            select
                rm."patient-id",
                sum("total-spend") "total-sales",
                sum("spend-generic") "total-generic-sales",
                percent_rank() over (
            order by
                "total-sales" desc) "rank-total-revenue",
                percent_rank() over (
            order by
                "total-generic-sales" desc) "rank-generic-revenue"
            from
                "prod2-generico"."retention-master" rm
            where
                "created-at" between dateadd('month',
                -3,
                date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
            group by
                "patient-id") x1
        where
            (x1."rank-total-revenue" <= 0.10
                or x1."rank-generic-revenue" <= 0.10))) t1
        inner join "prod2-generico"."patients-metadata-2" pm on
            t1."patient-id" = pm.id
        """
logger.info(f"data query : {s}")
data = rs_db.get_df(query=s)

logger.info(data.head())
total_patients = data['patient-id'].nunique()
logger.info(f"total patient count for run {period_end_d_plus1} : {total_patients}")

len_data = len(data)
logger.info(len_data)

data['primary-store-id'] = data['primary-store-id'].astype(int)

# Write to csv
s3.save_df_to_s3(df=data,
                 file_name=f'Shubham_G/premium_customer/premium_customer_{period_end_d_plus1}.csv')

# etl
data['created-at'] = dt.now(tz=gettz('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
data['created-by'] = 'etl-automation'
data['updated-at'] = dt.now(tz=gettz('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
data['updated-by'] = 'etl-automation'

logger.info(f"data write : \n {data.head()}")

# truncate data if current month data already exist

if isinstance(table_info, type(None)):
    logger.info(f"table: {table_name} do not exist")
else:
    truncate_query = f"""
            DELETE
            FROM
                "{read_schema}"."{table_name}"
            WHERE
                "segment-calc-date" = '{period_end_d_plus1}';
                """
    logger.info(truncate_query)
    rs_db.execute(truncate_query)

# drop duplicates subset - patient-id
data.drop_duplicates(subset=['patient-id'], inplace=True)

# Write to db
s3.write_df_to_db(df=data[table_info['column_name']], table_name=table_name,
                  db=rs_db, schema=read_schema)

logger.info("Script ran successfully")

# email after job ran successfully
email = Email()

mail_body = f"premium customer upload succeeded for segment calculation date {period_end_d_plus1} " \
            f"with data shape {data.shape} and total patient count {total_patients}"

if data.shape[0] == total_patients:
    subject = "Task Status segment calculation : successful"
else:
    subject = "Task Status segment calculation : failed"

email.send_email_file(subject=subject,
                      mail_body=mail_body,
                      to_emails=email_to, file_uris=[], file_paths=[])

# closing connection
rs_db.close_connection()