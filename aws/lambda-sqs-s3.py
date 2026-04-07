import boto3
import uuid

s3 = boto3.client("s3")

BUCKET = "hl7-raw-storage-xxxxx"

def lambda_handler(event, context):

    for record in event["Records"]:

        hl7_message = record["body"]

        key = f"raw/{uuid.uuid4()}.hl7"

        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=hl7_message
        )

        print("Stored HL7:", key)

    return {"status": "ok"}