# Jira Reporting & JQL Reference

## JQL Operators & Syntax

- **Equals/Not**: `=`, `!=`, `IN`, `NOT IN`, `IS EMPTY`.
- **Comparison**: `>`, `<`, `>=`, `<=`.
- **History**: `WAS`, `WAS IN`, `CHANGED`.
- **Text Search**: `~` (contains), `!~` (does not contain).

## Advanced JQL Functions

- **Date**: `startOfDay()`, `endOfWeek()`, `startOfMonth()`, `endOfYear()`.
- **Sprints**: `openSprints()`, `closedSprints()`, `futureSprints()`.
- **User**: `currentUser()`, `membersOf("group-name")`.
- **Linking**: `linkedIssues("issue-key")`.

## Standard Reporting Templates

### Sprint Status

```jql
project = [KEY] AND sprint = [ID]
```

### Team Velocity (Past Sprints)

```jql
assignee IN membersOf("team") AND sprint IN closedSprints() AND resolution = Done
```

### Bug Trend (30 Days)

```jql
type = Bug AND created >= -30d
```

### Overdue/Stale Analysis

```jql
dueDate < now() AND status != Done
updated < -30d AND status != Done
```

### Blocker Analysis

```jql
priority = Blocker AND status != Done
```
