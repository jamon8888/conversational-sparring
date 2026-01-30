# Atlassian Security & Compliance

## 1. Authentication (SSO/SAML)

- **Integration**: Okta, Azure AD, or Google Workspace.
- **SCIM**: Automated user provisioning and attribute sync.
- **Policy**: Enforce 2FA/MFA and SSO session timeouts.

## 2. Security Schemes

### Jira Permission Schemes

- **Public**: Org-wide view access.
- **Team**: Standard access for project members.
- **Restricted**: Confidential/Named users only.

### Confluence Space Permissions

- **Public**: Read access for all users.
- **Team**: Collaborative access for specific departments.
- **Personal**: Individual vault for drafting.

## 3. Data Governance & Compliance

- **Data Residency**: Pin data to specific regions (US, EU, APAC) for GDPR/Soc2.
- **Audit Logs**: Maintain logs for 7 years for regulatory compliance.
- **Encryption**: Enable encryption at rest and in transit.

## 4. Disaster Recovery

- **Backups**: Daily automated backups with weekly manual verification.
- **RTO/RPO**: Measure and test recovery time/point objectives quarterly.
- **Retention**: 30-day minimum online snapshot retention.
