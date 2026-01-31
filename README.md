# Conversational Sparring & Skills Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.1.0-green.svg)
![Build Status](https://github.com/jamon8888/conversational-sparring/actions/workflows/validate.yml/badge.svg)

A comprehensive plugin for Claude Code that combines a **Strategic Sparring Partner** with a massive **Professional Skills Library**.

---

## 🚀 Installation Guide

Choose your preferred platform below to install the Domain Coaches (Sparring Partners).

### 1. Claude Code (Recommended)

Add the marketplace first:

```bash
/plugin marketplace add https://github.com/jamon8888/conversational-sparring
```

Then install your specific coach:

| Domain          | Coach Name           | Install Command                                                                      |
| :-------------- | :------------------- | :----------------------------------------------------------------------------------- |
| **All Domains** | **Master Plugin**    | `/plugin install conversational-sparring-csuite@conversational-sparring-marketplace` |
| **Marketing**   | Marketing Sparring   | `/plugin install marketing-sparring@conversational-sparring-marketplace`             |
| **Engineering** | Engineering Sparring | `/plugin install engineering-sparring@conversational-sparring-marketplace`           |
| **Strategy**    | Strategic Research   | `/plugin install strategic-research-sparring@conversational-sparring-marketplace`    |
| **Executive**   | C-Level Sparring     | `/plugin install c-level-sparring@conversational-sparring-marketplace`               |
| **Product**     | Product Sparring     | `/plugin install product-sparring@conversational-sparring-marketplace`               |
| **Solo/Indie**  | Solopreneur Sparring | `/plugin install solopreneur-sparring@conversational-sparring-marketplace`           |

---

### 2. Codex (Local Script)

If you are using the local Codex environment, use the provided scripts in `scripts/`.

**Windows (`.bat`):**

```cmd
REM Install specific skills by name
scripts\codex-install.bat --skill marketing-strategy-pmm
scripts\codex-install.bat --skill senior-fullstack

REM Or install everything
scripts\codex-install.bat --all
```

**Mac/Linux (`.sh`):**

```bash
# Install by category (Recommended)
./scripts/codex-install.sh --category marketing
./scripts/codex-install.sh --category engineering

# Or install everything
./scripts/codex-install.sh --all
```

---

## ⚙️ Configuration (Required)

To enable **Deep Research (Exa)**, **Jira**, and **Confluence**, you must configure the Model Context Protocol (MCP).

1.  **Copy Config**:
    ```bash
    cp mcp.example.json mcp.json
    ```
2.  **Add Keys**: Edit `mcp.json` and add your API keys (e.g., `EXA_API_KEY`, `ATLASSIAN_API_TOKEN`).

---

## 📚 Master Skill Catalog

You can also use any skill individually by referencing its path in `skills/`.

### 🔍 Strategic Research (`skills/research-strategic/`)

| Skill                             | Description                                  | Codex Install                                           |
| :-------------------------------- | :------------------------------------------- | :------------------------------------------------------ |
| `strategic-research-orchestrator` | **MASTER**: 18+ playbooks (Blue Ocean, etc.) | `codex-install --skill strategic-research-orchestrator` |
| `exa-search-expert`               | **AI SEARCH**: Neural search & deep agents   | `codex-install --skill exa-search-expert`               |
| `opportunity-scorer`              | RICE/ICE prioritization                      | `codex-install --skill opportunity-scorer`              |

### 📣 Marketing (`skills/marketing/`)

| Skill                          | Description                         | Codex Install                                        |
| :----------------------------- | :---------------------------------- | :--------------------------------------------------- |
| `content-creator`              | **CORE**: Brand voice & SEO writing | `codex-install --skill content-creator`              |
| `marketing-demand-acquisition` | Funnel analytics                    | `codex-install --skill marketing-demand-acquisition` |
| `marketing-strategy-pmm`       | GTM strategy                        | `codex-install --skill marketing-strategy-pmm`       |

### 💻 Engineering (`skills/engineering/`)

| Skill              | Description                   | Codex Install                            |
| :----------------- | :---------------------------- | :--------------------------------------- |
| `senior-fullstack` | **CORE**: Project scaffolding | `codex-install --skill senior-fullstack` |
| `senior-devops`    | CI/CD, K8s, Docker            | `codex-install --skill senior-devops`    |
| `senior-security`  | Vulnerability scanning        | `codex-install --skill senior-security`  |

### 👔 C-Level (`skills/c-level/`)

| Skill         | Description                   | Codex Install                       |
| :------------ | :---------------------------- | :---------------------------------- |
| `ceo-advisor` | Strategic decision frameworks | `codex-install --skill ceo-advisor` |
| `cto-advisor` | Technology strategy           | `codex-install --skill cto-advisor` |

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
