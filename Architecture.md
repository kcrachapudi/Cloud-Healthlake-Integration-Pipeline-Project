# Original Architecture

HL7 Producer (Python Script)
        ↓
TCP / File / HTTP
        ↓
Python Integration Engine (Mini Mirth)
        ↓
AWS S3 Bucket (Raw HL7 Storage)
        ↓
Lambda Parser (HL7 → FHIR Bundle)
        ↓
FHIR Bundle JSON → S3 Processed Bucket
        ↓
Lambda Loader
        ↓
HealthLake Datastore
        ↓
API Layer (FastAPI)