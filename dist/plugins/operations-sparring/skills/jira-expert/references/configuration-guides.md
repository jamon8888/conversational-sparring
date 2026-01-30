# Jira Configuration Patterns

## Custom Fields

### When to Create

- Track data not in standard fields.
- Capture process-specific information.
- Enable advanced reporting.

### Field Types

- **Text**: Short text, paragraph.
- **Numeric**: Number, decimal.
- **Date**: Date picker, date-time.
- **Select**: Single select, multi-select, cascading.
- **User**: User picker, multi-user picker.

### Configuration Workflow

1. Create custom field.
2. Configure field context (which projects/issue types).
3. Add to appropriate screens.
4. Update search templates if needed.

## Issue Linking

### Link Types

- Blocks / Is blocked by.
- Relates to.
- Duplicates / Is duplicated by.
- Clones / Is cloned by.
- Epic-Story relationship.

### Best Practices

- Use Epic linking for feature grouping.
- Use blocking links to show dependencies.
- Document link reasons in comments.

## Permissions & Security Schemes

### Permission Levels

- Browse Projects.
- Create/Edit/Delete Issues.
- Administer Projects.
- Manage Sprints.

### Security Levels

- Define confidential issue visibility.
- Control access to sensitive data.
- Audit security changes.

## Bulk Operations

### Bulk Change

1. Use JQL to find target issues.
2. Select bulk change operation.
3. Choose fields to update.
4. Preview changes.
5. Execute and confirm.

### Bulk Transitions

- Move multiple issues through workflow.
- Useful for sprint cleanup.
- Requires appropriate "Transition Issues" permission.
