import boto3
import os
import dotenv
dotenv.load_dotenv()
AWS_REGION = os.getenv("AWS_REGION")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
sqs = boto3.client("sqs", region_name = AWS_REGION, \
    aws_access_key_id = AWS_ACCESS_KEY_ID, \
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

def send_to_queue(message, msg_type):

    sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=message,
        MessageAttributes={
            "MessageType": {
                "StringValue": msg_type,
                "DataType": "String"
            }
        }
    )