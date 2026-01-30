# Conversational Sparring & Skills Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.1.0-green.svg)
![Build Status](https://github.com/jamon8888/conversational-sparring/actions/workflows/validate.yml/badge.svg)

A comprehensive plugin for Claude Code that combines a **Strategic Sparring Partner** with a massive **Professional Skills Library**.

---

## 🚀 Marketplace Installation (Easiest Way)

This repository serves as a **Plugin Marketplace**. You can add it to Claude Code and then install any of the specialized plugins below.

### 1. Add this Marketplace

```bash
/plugin marketplace add https://github.com/jamon8888/conversational-sparring
```

### 2. Install Your Preferred Plugin

| Plugin Name              | Description                                          | Install Command                                                                      |
| :----------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **Master Plugin**        | **ALL** 48+ skills and agents. Best for power users. | `/plugin install conversational-sparring-csuite@conversational-sparring-marketplace` |
| **Marketing Sparring**   | Content creation, SEO, Demand Gen (18+ skills).      | `/plugin install marketing-sparring@conversational-sparring-marketplace`             |
| **Engineering Sparring** | Code review, DevOps, Architecture (21+ skills).      | `/plugin install engineering-sparring@conversational-sparring-marketplace`           |
| **C-Level Sparring**     | CEO/CTO strategic advisors and decision frameworks.  | `/plugin install c-level-sparring@conversational-sparring-marketplace`               |
| **Product Sparring**     | RICE scoring, User Stories, Roadmapping.             | `/plugin install product-sparring@conversational-sparring-marketplace`               |
| **Solopreneur Sparring** | Full-stack business management for single founders.  | `/plugin install solopreneur-sparring@conversational-sparring-marketplace`           |

> **Note**: If marketplace commands are not yet available in your version, use the [Manual Installation](#-manual-installation-git-clone) method below.

---

## 📦 MCP Configuration (Required)

To enable **Exa Neural Search**, **Jira**, and **Confluence**, you must configure the Model Context Protocol.

1.  Copy the example config:
    ```bash
    cp mcp.example.json mcp.json
    ```
2.  Edit `mcp.json` to add your API keys (e.g., `EXA_API_KEY`).

---

## 🛠️ Manual Installation (Git Clone)

If you prefer to manage the code yourself or contribute:

1.  **Clone the Repo**:

    ```bash
    git clone https://github.com/jamon8888/conversational-sparring.git
    cd conversational-sparring
    ```

2.  **Generate Standalone Plugins** (Optional):
    If you only want a specific domain (e.g., Marketing), run the factory script:
    ```bash
    python scripts/generate_plugins.py
    cd dist/plugins/marketing-sparring
    # Point Claude Code to this folder
    ```

---

## 📚 Master Skill Catalog

You can also use any skill individually by referencing its path in `skills/`.

### 🔍 Strategic Research (`skills/research-strategic/`)

| Skill                             | Description                                        |
| :-------------------------------- | :------------------------------------------------- |
| `strategic-research-orchestrator` | **MASTER**: 18+ playbooks (Blue Ocean, Rumelt)     |
| `exa-search-expert`               | **AI SEARCH**: Neural search, deep research agents |
| `opportunity-scorer`              | RICE/ICE frameworks                                |
| `market-analyst`                  | TAM/SAM/SOM modeling                               |
| `comparative-analyzer`            | Competitive intelligence & SWOT                    |
| ...                               | _See folder for 14+ more_                          |

### 📣 Marketing (`skills/marketing/`)

| Skill                          | Description                                                |
| :----------------------------- | :--------------------------------------------------------- |
| `content-creator`              | **CORE**: Brand voice analysis (`brand_voice_analyzer.py`) |
| `marketing-demand-acquisition` | Funnel analytics                                           |
| `marketing-strategy-pmm`       | Go-to-Market strategy                                      |
| `ad-copywriting`               | Direct response copy                                       |
| `email-marketing`              | Newsletter strategy                                        |
| `seo-blog-writing`             | Search-first drafting                                      |
| ...                            | _See folder for 30+ more_                                  |

### 💻 Engineering (`skills/engineering/`)

| Skill                   | Description                                 |
| :---------------------- | :------------------------------------------ |
| `senior-fullstack`      | **CORE**: Project scaffolding, code quality |
| `senior-devops`         | CI/CD, Kubernetes, Docker                   |
| `senior-security`       | Vulnerability scanning                      |
| `senior-data-scientist` | Experiment design                           |
| `tech-stack-evaluator`  | Selection matrices                          |
| ...                     | _See folder for 15+ more_                   |

### 👔 C-Level (`skills/c-level/`)

| Skill         | Description                   |
| :------------ | :---------------------------- |
| `ceo-advisor` | Strategic decision frameworks |
| `cto-advisor` | Technology strategy           |

---

## 🔧 Automation Tools

Run Python automation scripts directly from the command line:

```bash
# Analyze Brand Voice
python skills/marketing/content-creator/scripts/brand_voice_analyzer.py draft.md

# Prioritize Features (RICE)
python skills/product/product-manager-toolkit/scripts/rice_prioritizer.py features.csv
```

## Contributing

1.  Fork the repo.
2.  Add skill to `skills/<category>/`.
3.  Submit PR (CI will validate `SKILL.md`).

## License

MIT
