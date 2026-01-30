# Template Design Standards

## 1. Design Principles

- **Clarity**: Use clear headers and structured navigation.
- **Completeness**: Ensure all required metadata and status fields are present.
- **Flexibility**: Define which sections are optional vs. mandatory.
- **Interactivity**: Use expand macros to prevent "wall of text" syndrome.

## 2. Macro Best Practices

- **Dynamic Data**: Use `{jira}`, `{tasks}`, and `{date}` macros for live information.
- **Visual Hierarchy**: Implement `{panel}`, `{info}`, and `{status}` for visual scanability.
- **Blueprint Logic**: Design multi-page structures that link together automatically.

## 3. Library Organization

- **Global vs. Space**: Maintain a core set of global templates with space-level overrides for specialized teams.
- **Categorization**: Group templates by intent (Planning, Execution, reporting, Archiving).
