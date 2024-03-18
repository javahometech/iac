import boto3
import os

def lambda_handler(event,context):
    client = boto3.client('rds')
    db_identifier = os.environ['DB_INSTANCE_IDENTIFIER']
    response = client.start_db_instance(DBInstanceIdentifier=db_identifier)
    print(response)