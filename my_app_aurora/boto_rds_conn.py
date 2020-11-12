import boto3
import json
import os
from botocore.exceptions import ClientError


cluster_arn = os.environ['cluster_arn']
secret_arn = os.environ['secret_arn']

rds_data = boto3.client('rds-data')


class BotoPostgresqlDB(object):

    def execute_query(self, sql_query, parameters=[]):
        response = []
        try:
            response = rds_data.execute_statement( resourceArn=cluster_arn,
                                                   secretArn=secret_arn,
                                                   database=os.environ['database'],
                                                   sql=sql_query,
                                                   parameters=parameters)
            return response
        except Exception as e:
            print("Exception while connecting to db", e)
        return response
