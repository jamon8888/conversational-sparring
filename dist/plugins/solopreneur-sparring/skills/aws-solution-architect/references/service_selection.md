# AWS Service Selection Guide

## Compute Selection

- **Lambda**: Short tasks (<15 min), event-driven, variable traffic.
- **ECS Fargate**: Containerized apps, long-running processes, predictable traffic.
- **App Runner**: Rapid container deployment from source; no infra management.
- **EC2**: Custom OS configuration, high-performance GPU, legacy Windows apps.

## Database Selection

- **DynamoDB**: NoSQL, serverless, single-digit ms scale, key-value data.
- **Aurora Serverless**: Relational (SQL), scales with traffic peaks, good for startups.
- **RDS**: Managed standard relational DBs (SQL Server, Oracle, MariaDB).
- **Neptune**: Graph data for relationship-heavy apps (Social, Fraud).
- **Timestream**: High-ingest time-series IoT data.

## Messaging & Orchestration

- **EventBridge**: Central event bus for cross-service communication.
- **SQS**: Point-to-point message queuing and buffering.
- **Step Functions**: Long-running workflow state machines.
- **SNS**: Fan-out notifications (Push, SMS, Email).
