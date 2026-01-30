# Conversational Sparring & Skills Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.1.0-green.svg)
![Build Status](https://github.com/jamon8888/conversational-sparring/actions/workflows/validate.yml/badge.svg)

A comprehensive plugin for Claude Code that combines a **Strategic Sparring Partner** with a massive **Professional Skills Library**.

## 🚀 Two Ways to Use

### 1. The Master Plugin (Recommended for Power Users)

Install this entire repository as a single plugin to get **ALL** agents, skills, and the sparring engine.

```bash
git clone https://github.com/jamon8888/conversational-sparring.git
# Configure MCP (see below)
# Point Claude Code to this folder
```

### 2. The Domain Plugin Factory (Recommended for Specialists)

Generate lightweight, standalone plugins just for your role (e.g., "Marketing Sparring", "Engineering Sparring").

```bash
# 1. Generate plugins
python scripts/generate_plugins.py

# 2. Pick your plugin from dist/
cd dist/plugins/marketing-sparring
# Install this folder as your local plugin
```

---

## 📦 MCP Configuration (Required for Deep Research)

To enable **Exa Neural Search**, **Jira**, and **Confluence** integrations, you must configure the Model Context Protocol.

1.  Copy the example config:
    ```bash
    cp mcp.example.json mcp.json
    ```
2.  Edit `mcp.json` to add your API keys (e.g., `EXA_API_KEY`).

---

## 📚 Full Skill Catalog

You can install any skill individually by copying its folder or referencing its `SKILL.md`.

### 🔍 Strategic Research (`skills/research-strategic/`)

| Skill Folder                      | Description                                                         |
| :-------------------------------- | :------------------------------------------------------------------ |
| `strategic-research-orchestrator` | **MASTER SKILL**: 18+ playbooks (Blue Ocean, Rumelt, etc.)          |
| `exa-search-expert`               | **AI SEARCH**: Neural search, deep research agents, company finding |
| `opportunity-scorer`              | RICE/ICE frameworks for prioritization                              |
| `market-analyst`                  | TAM/SAM/SOM modeling                                                |
| `comparative-analyzer`            | Deep competitive intelligence & SWOT                                |
| `multi-agent-sprint-research`     | Parallel research sprints                                           |
| `insights-repository-kit`         | Managing research insights                                          |
| `market-scenario-modeler`         | Forecasting market shifts                                           |
| `battlecard-library`              | Sales battlecards generator                                         |
| `brand-governance-os`             | Brand guidelines enforcement                                        |
| `brand-measurement-dashboard`     | Brand equity tracking                                               |
| `brand-narrative-playbook`        | Storytelling frameworks                                             |
| `brand-voice-glossary`            | Tone and voice definitions                                          |
| `executive-briefing-kit`          | Board-level presentations                                           |
| `experience-system-blueprint`     | CX mapping                                                          |
| `participant-operations-hub`      | User research recruiting                                            |
| `research-brief-blueprint`        | Research planning templates                                         |
| `research-synthesizer`            | Insight extraction                                                  |
| `win-loss-dataset`                | Sales win/loss analysis                                             |

### 📣 Marketing (`skills/marketing/`)

| Skill Folder                     | Description                                                     |
| :------------------------------- | :-------------------------------------------------------------- |
| `content-creator`                | **CORE**: Brand voice analysis (`brand_voice_analyzer.py`), SEO |
| `marketing-demand-acquisition`   | Funnel analytics, campaign tracking                             |
| `marketing-strategy-pmm`         | Go-to-Market strategy                                           |
| `campaign-orchestration`         | Multi-channel campaign planning                                 |
| `ad-copywriting`                 | Direct response copy                                            |
| `app-store-optimization`         | ASO for mobile apps                                             |
| `brand-guidelines`               | Identity framework                                              |
| `content-attribution`            | ROI modeling                                                    |
| `content-creation-at-scale`      | Batch production                                                |
| `content-distribution`           | Repurposing workflows                                           |
| `content-governance`             | QA and compliance                                               |
| `content-personalization`        | Dynamic content strategy                                        |
| `content-pipeline-orchestration` | Editorial colendars                                             |
| `content-repurposing`            | Blog to social conversion                                       |
| `content-strategy`               | Long-term planning                                              |
| `email-campaign-automation`      | Drip sequences                                                  |
| `email-marketing`                | Newsletter strategy                                             |
| `experiment-design`              | A/B testing frameworks                                          |
| `growth-analytics`               | Viral loops and KPIs                                            |
| `landing-page-copy`              | Conversion optimization                                         |
| `lead-magnets`                   | Whitepapers and tools                                           |
| `marketing-analytics`            | General dashboarding                                            |
| `multi-language-content`         | Localization                                                    |
| `partnership-development`        | Co-marketing                                                    |
| `podcasting`                     | Audio strategy                                                  |
| `product-launch-orchestration`   | Launch day playbooks                                            |
| `product-led-growth`             | PLG frameworks                                                  |
| `referral-programs`              | Viral coefficients                                              |
| `seo-blog-writing`               | Search-first drafting                                           |
| `seo-geo-blog-writing`           | Local SEO                                                       |
| `seo-workflow-orchestration`     | Technical SEO                                                   |
| `social-campaign-orchestration`  | Social launches                                                 |
| `social-media-analyzer`          | Engagement metrics                                              |
| `social-media-content`           | Platform-native posts                                           |
| `storytelling`                   | Narrative arcs                                                  |
| `unified-analytics`              | Cross-channel views                                             |
| `user-onboarding`                | Activation flows                                                |
| `video-marketing`                | Scripting and strategy                                          |
| `viral-mechanics`                | K-factor optimization                                           |
| `webinars`                       | Event planning                                                  |

### 💻 Engineering (`skills/engineering/`)

| Skill Folder             | Description                                 |
| :----------------------- | :------------------------------------------ |
| `senior-fullstack`       | **CORE**: Project scaffolding, code quality |
| `senior-devops`          | CI/CD, Kubernetes, Docker                   |
| `senior-security`        | Vulnerability scanning                      |
| `senior-data-scientist`  | Experiment design                           |
| `aws-solution-architect` | Cloud patterns                              |
| `code-reviewer`          | Automated PR review                         |
| `ms365-tenant-manager`   | Microsoft 365 admin                         |
| `senior-architect`       | System design                               |
| `senior-backend`         | API design, DB scaling                      |
| `senior-computer-vision` | CV models                                   |
| `senior-data-engineer`   | ETL pipelines                               |
| `senior-frontend`        | React/Vue patterns                          |
| `senior-ml-engineer`     | MLOps                                       |
| `senior-prompt-engineer` | LLM optimization                            |
| `senior-qa`              | Testing frameworks                          |
| `senior-secops`          | Incident response                           |
| `tdd-guide`              | Test Driven Development                     |
| `tech-stack-evaluator`   | Selection matrices                          |

### 📦 Product (`skills/product/`)

| Skill Folder              | Description                           |
| :------------------------ | :------------------------------------ |
| `product-manager-toolkit` | RICE prioritization, stakeholder maps |
| `agile-product-owner`     | Backlog grooming                      |
| `product-strategist`      | Vision and roadmap                    |
| `ui-design-system`        | Component libraries                   |
| `ux-researcher-designer`  | User testing and prototypes           |

### 📅 Project Management (`skills/project-management/`)

| Skill Folder          | Description                   |
| :-------------------- | :---------------------------- |
| `senior-pm`           | Project charters, risk logs   |
| `scrum-master`        | Ceremony facilitation         |
| `jira-expert`         | **MCP**: Jira automation      |
| `confluence-expert`   | **MCP**: Knowledge management |
| `atlassian-admin`     | Suite administration          |
| `atlassian-templates` | Standard docs                 |

### 💰 Revenue & Sales (`skills/revenue/` & `skills/sales/`)

| Skill Folder                   | Description             |
| :----------------------------- | :---------------------- |
| `revenue/revenue-analytics`    | Forecasting             |
| `revenue/pipeline-forecasting` | Deal flow analysis      |
| `revenue/pricing-packaging`    | Monetization strategy   |
| `sales/cold-outreach`          | Email/LikedIn templates |
| `sales/discovery-calls`        | Question banks          |
| `sales/objection-handling`     | Battlecards             |
| `sales/social-selling`         | LinkedIn playbooks      |
| `sales/value-propositions`     | ROI calculators         |

### 👔 C-Level (`skills/c-level/`)

| Skill Folder  | Description                   |
| :------------ | :---------------------------- |
| `ceo-advisor` | Strategic decision frameworks |
| `cto-advisor` | Technology strategy           |

## 🔧 Automation Scripts

Many skills contain Python scripts (`scripts/`). You can run them directly:

```bash
# Example: Analyze Brand Voice
python skills/marketing/content-creator/scripts/brand_voice_analyzer.py content.txt

# Example: Generate Design Tokens
python skills/product/ui-design-system/scripts/design_token_generator.py "#0066CC"
```

## Contributing

1.  Fork the repo.
2.  Add your skill to `skills/<category>/<skill-name>`.
3.  Ensure `SKILL.md` frontmatter is valid.
4.  Submit a PR.

## License

MIT
