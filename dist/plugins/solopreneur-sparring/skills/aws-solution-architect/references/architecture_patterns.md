# AWS Architecture Patterns

## 1. Serverless Web Application

- **Use Case**: Startups, SaaS backends, low-operation sites.
- **Stack**: S3/CloudFront (FE) + API Gateway/Lambda (API) + DynamoDB (DB) + Cognito (Auth).
- **Benefits**: Zero maintenance, pay-per-use, scales to zero.

## 2. Event-Driven Microservices

- **Use Case**: Decoupled workflows, async processing.
- **Stack**: EventBridge (Bus) + SQS (Queue) + Step Functions (State) + Lambda (Compute).
- **Benefits**: loose coupling, failure isolation.

## 3. High-Performance Three-Tier

- **Use Case**: E-commerce, CMS, traditional dynamic sites.
- **Stack**: ALB (Load Balancer) + ECS Fargate (Compute) + Aurora (Relational DB) + ElastiCache (Redis).
- **Benefits**: Proven reliability, flexible scaling.

## 4. Real-Time Data Pipeline

- **Use Case**: IoT, streaming logs, real-time analytics.
- **Stack**: Kinesis (Ingestion) + Lambda/Glue (Processing) + S3 (Data Lake) + Athena (Query).

## 5. Multi-Region Global Stack

- **Use Case**: Global availability, disaster recovery.
- **Stack**: Route 53 (Geo-routing) + CloudFront (Edge) + DynamoDB Global Tables + Multi-Region Lambda.
