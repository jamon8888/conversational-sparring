# Startup Architecture Lifecycle

## Phase 1: MVP (0-1,000 Users)

- **Goal**: Launch in days; zero infra management.
- **Stack**: AWS Amplify, Lambda, DynamoDB, Cognito.
- **Cost**: $20-$100/mo.

## Phase 2: Growth (1,000-100,000 Users)

- **Goal**: Handle volume; cost efficiency.
- **Add**: ElastiCache (Redis), Aurora Serverless, CodePipeline for CI/CD, multi-AZ for safety.
- **Cost**: $500-$2,000/mo.

## Phase 3: Scale-Up (100,000+ Users)

- **Goal**: Global reach; reliability; security.
- **Add**: Multi-region deployment, WAF/Shield for protection, Global Tables, Savings Plans.
- **Cost**: $3,000-$10,000/mo.

## Common Startup Pitfalls

- **Over-engineering**: Building for 1M users while still at 100.
- **Under-monitoring**: Failing to enable CloudWatch alerts on day one.
- **Cost Blindness**: Forgetting to enable lifecycle policies on S3 logs.
