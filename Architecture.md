# Original Architecture

                  ┌────────────────────────┐
                  │   HL7 Producer Systems  │
                  │  (ADT / ORU / ORM / SIU)│
                  └──────────┬─────────────┘
                             │ TCP/MLLP/HTTP
                             ▼
                ┌────────────────────────────┐
                │ Python Integration Engine  │
                │  (Mini Mirth Consumer)     │
                │                            │
                │ • HL7 Parsing              │
                │ • Routing Rules            │
                │ • ACK Generator            │
                │ • Validation               │
                └──────────┬─────────────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │   AWS SQS Queue     │
                 │  (Async Buffering)  │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │  Lambda Router      │
                 │  (Message Type)     │
                 └─────────┬───────────┘
          ┌────────────────┼─────────────────┐
          ▼                ▼                 ▼
 ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
 │ Lambda ORU  │   │ Lambda ORM  │   │ Lambda SIU  │
 │ HL7 → FHIR  │   │ HL7 → FHIR  │   │ HL7 → FHIR  │
 └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
        │                 │                 │
        └──────────┬──────┴──────┬──────────┘
                   ▼             ▼
            ┌────────────────────────┐
            │ FHIR Validation Lambda │
            └──────────┬─────────────┘
                       ▼
               ┌───────────────────┐
               │  Raw FHIR S3      │
               └─────────┬─────────┘
                         ▼
                ┌───────────────────┐
                │ AI Clinical NLP   │
                │ Summarization     │
                └─────────┬─────────┘
                         ▼
               ┌─────────────────────┐
               │ HealthLake Datastore│
               └─────────┬───────────┘
                         ▼
                ┌────────────────────┐
                │ FastAPI API Layer  │
                └─────────┬──────────┘
                          ▼
                  Analytics / Athena / BI

Observability Layer:
CloudWatch Logs + Metrics + Alerts

Infra Layer:
Terraform Automation