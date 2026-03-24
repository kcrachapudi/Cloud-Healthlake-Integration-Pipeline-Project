import boto3
import os
import dotenv
dotenv.load_dotenv()
AWS_REGION = os.getenv("AWS_REGION")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")

sqs = boto3.client("sqs", region_name = AWS_REGION) 

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