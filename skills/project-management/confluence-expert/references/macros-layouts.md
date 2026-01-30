# Confluence Macro & Layout Reference

## 1. Essential Content Macros

- **Info/Note/Warning**: `{info}Message{info}`.
- **Expand**: `{expand:title=Title}Content{expand}`.
- **Table of Contents**: `{toc:maxLevel=3}`.
- **Excerpt**: `{excerpt}Reusable Content{excerpt}` / `{excerpt-include:Page Name}`.

## 2. Dynamic Content Macros

- **Jira Issues**: `{jira:JQL=project = ABC}`.
- **Jira Charts**: `{jirachart:type=pie|jql=project = ABC}`.
- **Recently Updated**: `{recently-updated:max=10}`.
- **Content by Label**: `{contentbylabel:label=important}`.

## 3. Collaboration & Formatting

- **Status**: `{status:colour=Green|title=Approved}`.
- **Task List**: `- [ ] Task`.
- **Panel**: `{panel:title=Title}Content{panel}`.
- **Section/Column**:
  ```
  {section}
  {column:width=50%}Content{column}
  {column:width=50%}Content{column}
  {section}
  ```
- **Code Block**: `{code:javascript} ... {code}`.
