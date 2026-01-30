# AWS Well-Architected Best Practices

## Cost Optimization

- **Right-sizing**: Monitor CloudWatch metrics to adjust instance/Lambda memory sizes.
- **Savings Plans**: Commit to consistent compute usage for 60-72% discounts.
- **S3 Lifecycle**: Automate transitions to Infrequent Access (IA) or Glacier.
- **VPC Endpoints**: Use endpoints for S3/DynamoDB to avoid NAT Gateway charges.

## Security Hardening

- **Least Privilege**: Grant minimal IAM permissions; avoid `*` resources.
- **Encryption**: Enable KMS encryption at rest and TLS 1.2+ in transit.
- **Network Isolation**: Deploy sensitive compute/DBs in Private Subnets with Security Groups.
- **Secrets**: Use AWS Secrets Manager; never hardcode credentials in code or ENV.

## Scalability & Reliability

- **Horizontal Scale**: Prefer scaling out (auto-scaling) over scaling up (larger instances).
- **Chaos Testing**: Validate recovery by periodically injecting failures (e.g., terminating instances).
- **Caching**: Implement CloudFront (edge) and ElastiCache (compute) to protect DBs.
- **Async Buffers**: Use SQS to smooth out traffic spikes and decouple processing.
