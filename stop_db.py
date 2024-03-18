import boto3
import os

def lambda_handler(event,context):

    client = boto3.client('rds')
    db_identifier = os.environ['RDS_INSTANCE_IDENTIFIER']
    if event['resources'][0].contains('rds_stop_rule'):
        response = client.stop_db_instance(DBInstanceIdentifier=db_identifier)
        print(response)
    elif event['resources'][0].contains('rds_start_rule'):
        response = client.start_db_instance(DBInstanceIdentifier=db_identifier)
        print(response)