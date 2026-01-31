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

REM Or install everything
scripts\codex-install.bat --all
```

**Mac/Linux (`.sh`):**

```bash
# Install by category (Recommended)
./scripts/codex-install.sh --category marketing

# Or install everything
./scripts/codex-install.sh --all
```

---

## 🧩 Individual Skills (Manual / Desktop)

You can download individual skills as **ZIP files** from the [Releases Page](../../releases).

### For Claude Desktop

1.  **Download** the skill zip (e.g., `content-creator.zip`).
2.  **Unzip** it to your preferred location (e.g., `~/Documents/Prompts/`).
3.  **Use**: Drag and drop the `.md` files into Claude Desktop, or point your MCP server to that directory if using a filesystem server.

### For Custom Integrations

Each zip contains the full skill package:

- `SKILL.md` (The prompt/logic)
- `scripts/` (Python automation)
- `references/` (Knowledge base)

---

## ⚙️ Configuration (Required)

To enable **Deep Research (Exa)**, **Jira**, and **Confluence**, you must configure the Model Context Protocol (MCP).

1.  **Copy Config**:
    ```bash
    cp mcp.example.json mcp.json
    ```
2.  **Add Keys**: Edit `mcp.json` and add your API keys (e.g., `EXA_API_KEY`, `ATLASSIAN_API_TOKEN`).

---

## 📚 Detailed Plugin Capabilities

Here is the **full list of skills** included in each domain plugin.

### � Marketing & Growth (`marketing-sparring`)

> _Optimized for Heads of Growth, CMOs, and Marketing Leads._

**Core Strategy:**

- `marketing-strategy-pmm` (GTM Strategy)
- `marketing-analytics`
- `growth-analytics`
- `attribution-roi`
- `market-analyst`
- `comparative-analyzer`
- `report-generator`

**Content & Creative:**

- `content-creator` (Brand Voice & SEO)
- `content-strategy`
- `content-distribution`
- `ad-copywriting`
- `social-media-analyzer`
- `email-marketing`

**Acquisition:**

- `marketing-demand-acquisition`
- `app-store-optimization`
- `campaign-orchestration`
- `sales-marketing-alignment`
- `revenue-analytics`

**Tools:**

- `docx`, `pdf`, `pptx`

---

### 💻 Engineering (`engineering-sparring`)

> _Optimized for CTOs, VPs of Engineering, and Tech Leads._

**Leadership:**

- `cto-advisor`
- `senior-architect`
- `tech-stack-evaluator`
- `technical-researcher`
- `compliance-analyst`

**Development:**

- `senior-fullstack`
- `senior-backend`
- `senior-frontend`
- `code-reviewer`
- `tdd-guide`
- `solution-architect`

**Operations & Quality:**

- `senior-devops`
- `senior-security` (Vuln Scanning)
- `senior-qa`
- `quality-validator`
- `aws-solution-architect`

**Process:**

- `sprint-executor`
- `senior-data-scientist`
- `docx`, `pdf`, `pptx`

---

### 👔 C-Level Strategy (`c-level-sparring`)

> _Optimized for CEOs, Founders, and Chief Strategy Officers._

**Executive Strategy:**

- `ceo-advisor`
- `cto-advisor`
- `product-strategist`
- `senior-architect`
- `risk-management-specialist`

**Business Intelligence:**

- `growth-analytics`
- `revenue-analytics`
- `pipeline-forecasting`
- `pricing-packaging`
- `market-analyst`
- `comparative-analyzer`

**Planning:**

- `opportunity-discovery`
- `opportunity-scorer` (RICE/ICE)
- `roadmap-planner`
- `marketing-strategy-pmm`
- `report-synthesizer`
- `docx`, `pdf`, `pptx`

---

### � Strategic Research (`strategic-research-sparring`)

> _Deep research intelligence with Exa.ai integration._

**Core Intelligence:**

- `strategic-research-orchestrator` (Master Orchestrator)
- `exa-search-expert` (Neural Search)
- `research-synthesizer`
- `market-analyst`
- `comparative-analyzer`

**Analysis Tools:**

- `opportunity-scorer`
- `market-scenario-modeler`
- `win-loss-dataset`
- `insights-repository-kit`
- `participant-operations-hub`
- `executive-briefing-kit`

---

### 📦 Product Management (`product-sparring`)

> _Optimized for CPOs and Product Managers._

**Product Strategy:**

- `product-manager-toolkit`
- `product-strategist`
- `product-launch-orchestration`
- `product-led-growth`
- `marketing-strategy-pmm`
- `roadmap-planner`

**Execution:**

- `agile-product-owner`
- `senior-pm`
- `scrum-master`
- `sprint-orchestrator`
- `sprint-progress-tracker`

**UX & Design:**

- `ux-researcher-designer`
- `ui-design-system`

**Atlassian Suite:**

- `jira-expert`
- `confluence-expert`
- `atlassian-templates`

**Tools:**

- `market-analyst`
- `opportunity-discovery`
- `docx`, `pdf`, `pptx`

---

### � Solopreneur (`solopreneur-sparring`)

> _The "All-in-One" kit for Indie Founders._

**Build:**

- `senior-fullstack`
- `aws-solution-architect`
- `product-manager-toolkit`

**Growth:**

- `content-creator`
- `marketing-demand-acquisition`
- `growth-analytics`
- `email-marketing`
- `ad-copywriting`
- `content-distribution`

**Business:**

- `ceo-advisor`
- `revenue-analytics`
- `pricing-packaging`
- `market-analyst`
- `opportunity-discovery`
- `opportunity-scorer`
- `product-launch-orchestration`
- `docx`, `pdf`, `pptx`

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
