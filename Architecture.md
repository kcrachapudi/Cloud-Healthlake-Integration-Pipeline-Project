# Original Architecture

PRODUCER (Hospital HL7 Systems)
        ↓
Mirth Connect (Transport + Reliability)
        ↓
Amazon S3 (Raw HL7 Storage / Buffer)
        ↓
AWS Lambda (Python)
  - HL7 Parsing
  - Business Logic
  - HL7 → FHIR Conversion
        ↓
AWS HealthLake (FHIR Store + Query Engine)
        ↓
FastAPI (Optional Consumer API Layer)