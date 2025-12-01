<div>

# 🤖 MultiAgents — Modular AI Agent Framework
A production-ready, multi-agent system designed for building, extending, and monitoring large-scale AI workflows.

![Issue Triage](https://github.com/atharvvv10/MultiAgents/workflows/Issue%20triage%20(repo-aware)/badge.svg)
![PR Moderation](https://github.com/atharvvv10/MultiAgents/workflows/PR%20moderation%20(repo-aware)/badge.svg)
![Moderation Tracker](https://github.com/atharvvv10/MultiAgents/workflows/Moderation%20tracker/badge.svg)

</div>

---

# 🧠 Overview

**MultiAgents** is a modular AI agent framework for building intelligent systems, LLM-powered pipelines, and agent orchestration.

This repository includes:
- ⚙️ A modern agent architecture  
- 🛠 Prompt management utilities  
- 📡 Monitoring tools for agent behavior  
- 🧠 Multi-agent orchestration  
- 🔧 A complete public contribution & moderation pipeline  

---

# 📁 Project Structure

```
MultiAgents/
│
├── ai-agent/                # Core agent logic
├── agent_monitoring/        # Monitoring utilities
├── llm_project/             # LLM tools & pipelines
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   ├── contribution_template.md
│   │   └── config.yml
│   ├── workflows/
│   │   ├── issue-triage.yml
│   │   ├── pr-moderation.yml
│   │   └── issue-bot-tracker.yml
│   ├── MODERATORS.yml
│   └── PULL_REQUEST_TEMPLATE.md
│
├── CONTRIBUTING.md
└── README.md
```

---

# 🙌 Public Contribution Pipeline (Automated)

This repository has **three clean templates**:

### 🐞 Bug Report  
### 💡 Feature Request  
### 🧩 Contribution Request  

Each template supports:
- Level selection → `beginner` / `intermediate` / `advanced`  
- First-time contributor checkbox  
- Clean structured reporting  

Everything triggers automated CI/CD flows.

---

# 🏷 Automatic Issue Triage (GitHub Actions)

The workflow `issue-triage.yml` automatically:

- Detects issue type  
- Adds labels (`bug`, `enhancement`, etc.)  
- Detects level → `beginner` / `intermediate` / `advanced`  
- Detects first-time contributor → adds `good first issue`  
- Detects core module mentions → adds `needs-moderation`  
- Pings moderators using `.github/MODERATORS.yml`  

Core modules protected:

```
ai-agent/
agent_monitoring/
llm_project/
```

---

# 🔒 PR Moderation (Protected Core)

The workflow `pr-moderation.yml` checks changed files in a PR.

If a PR modifies any core folder:

- Adds `needs-moderation`
- Adds `awaiting-moderator`
- Tags moderators
- Requires `moderator-approved` before merge

No core code merges without human approval.

---

# 📊 Moderation Queue (Automated Issue Tracker)

`issue-bot-tracker.yml` runs daily or manually and:

- Scans all open issues  
- Finds issues needing moderation  
- Updates the **Moderation Queue** issue  
- Shows all pending items in one place  

Helps maintainers track work across the repo.

---

# 🛠️ Development Setup

```bash
git clone https://github.com/atharvvv10/MultiAgents.git
cd MultiAgents
pip install -r requirements.txt
```

Run agents inside the `ai-agent/` directory.

---

# 🤝 Contributing Guide

### 1️⃣ Open an Issue  
Choose:
- Bug  
- Feature  
- Contribution request  

Select:
- Your level  
- First-time contributor

### 2️⃣ Open a Pull Request  
- Fork the repo  
- Create a branch  
- Make changes  
- Submit PR  

If your PR touches core modules → moderator approval required.

---

# 🧩 Why This Repo Is Contributor-Friendly

- Clean 3-template system  
- Automated triaging  
- Automated first-time contributor support  
- Automated level detection  
- Automated moderation warnings  
- Moderation queue  
- Protected core modules  
- Professional GitHub Actions setup  

---

# ⭐ Credits

Maintainer: **@atharvvv10**  
Moderators listed in `.github/MODERATORS.yml`.

This project is open for contributions — feel free to join!

