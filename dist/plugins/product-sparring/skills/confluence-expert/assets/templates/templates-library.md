# Templates Library
### Meeting Notes Template

```
**Date**: {date}
**Attendees**: @user1, @user2
**Facilitator**: @facilitator

## Agenda
1. Topic 1
2. Topic 2

## Discussion
- Key point 1
- Key point 2

## Decisions
{info}Decision 1{info}

## Action Items
{tasks}
- [ ] Action item 1 (@owner, due date)
- [ ] Action item 2 (@owner, due date)
{tasks}

## Next Steps
- Next meeting date
```

### Project Overview Template

```
{panel:title=Project Quick Facts}
**Status**: {status:colour=Green|title=Active}
**Owner**: @owner
**Start Date**: DD/MM/YYYY
**End Date**: DD/MM/YYYY
**Budget**: $XXX,XXX
{panel}

## Executive Summary
Brief project description

## Objectives
1. Objective 1
2. Objective 2

## Key Stakeholders
| Name | Role | Responsibility |
|------|------|----------------|
| @user | PM | Overall delivery |

## Milestones
{jira:project=PROJ AND type=Epic}

## Risks & Issues
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Risk 1 | High | Action plan |

## Resources
- [Design Docs](#)
- [Technical Specs](#)
```

### Decision Log Template

```
**Decision ID**: PROJ-DEC-001
**Date**: {date}
**Status**: {status:colour=Green|title=Approved}
**Decision Maker**: @decisionmaker

## Context
Background and problem statement

## Options Considered
1. Option A
   - Pros:
   - Cons:
2. Option B
   - Pros:
   - Cons:

## Decision
Chosen option and rationale

## Consequences
Expected outcomes and impacts

## Next Steps
- [ ] Action 1
- [ ] Action 2
```

### Sprint Retrospective Template

```
**Sprint**: Sprint XX
**Date**: {date}
**Team**: Team Name

## What Went Well
{info}
- Positive item 1
- Positive item 2
{info}

## What Didn't Go Well
{warning}
- Challenge 1
- Challenge 2
{warning}

## Action Items
{tasks}
- [ ] Improvement 1 (@owner)
- [ ] Improvement 2 (@owner)
{tasks}

## Metrics
**Velocity**: XX points
**Completed Stories**: X/X
**Bugs Found**: X
```
