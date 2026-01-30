# Atlassian User Lifecycle Management

## 1. User Provisioning Workflow

1. **Verification**: Confirm identity and role requirements.
2. **Creation**: Create account in the organization directory.
3. **Groups**: Add to relevant product groups (e.g., `jira-software-users`).
4. **Access**: Assign specialized product roles.
5. **Onboarding**: Send standardized welcome communications.

## 2. User Deprovisioning Workflow

1. **Audit**: Identify all content and tickets owned by the user.
2. **Transfer**: Reassign ownership of Projects, Spaces, Filters, and Dashboards.
3. **Revocation**: Remove from all groups and deactivate account.
4. **Logging**: Document action in the system audit log.

## 3. Group Management Strategy

- **Team Groups**: Aligned to organizational structure (Engineering, Sales, etc.).
- **Role Groups**: Aligned to system permissions (Admins, Users, Viewers).
- **Project Groups**: For granular security on specific initiatives.
- **Review**: Conduct quarterly cleanup of empty or specialized groups.

## Best Practices

- **SCIM**: Use Identity Provider (Okta, Azure AD) sync for automated provisioning.
- **Group-Based**: Never assign site permissions to individuals; always use groups.
- **Audit**: Log all administrative changes for compliance.
