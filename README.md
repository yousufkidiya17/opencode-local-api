<div align="center">

# ðŸ”§ OpenCode Local API

### _Supercharge AI Coding Agents with Local System Powers_

[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/API-REST-009688?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![AI Agent](https://img.shields.io/badge/AI-Agent_Tool-FF6F61?style=for-the-badge&logo=openai&logoColor=white)](#)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-8B5CF6?style=for-the-badge)](#)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1e1e2e,100:0d1117&height=120&section=header" width="100%"/>

**OpenCode Local API** is a lightweight Python server that gives AI coding agents (like OpenCode) **real superpowers** â€” terminal access, safe file editing, background task management, and live web search. Run it locally and watch your AI agent become 10x more capable.

[ðŸ“– **How It Works**](#-how-it-works) Â· [ðŸš€ **Quick Start**](#-quick-start) Â· [ðŸ› **Report Bug**](https://github.com/yousufkidiya17/opencode-local-api/issues)

</div>

---

## ðŸŽ¯ Overview

> _"Give your AI agent hands, eyes, and a brain â€” locally."_

AI coding agents are smart but sandboxed. They can't run terminal commands, edit files safely, or search the web. **OpenCode Local API** bridges that gap by exposing a simple REST API that gives AI agents controlled access to your local system.

<div align="center">

| ðŸ’» Terminal Access | ðŸ“ Safe File Editing | ðŸ”„ Background Tasks |
|:---:|:---:|:---:|
| Run shell commands with output capture | Read, write & patch files with safety checks | Queue and monitor long-running processes |

| ðŸ” Web Search | ðŸ›¡ï¸ Security First | âš¡ Zero Config |
|:---:|:---:|:---:|
| Live DuckDuckGo search from your agent | Sandboxed execution with path validation | Single file, instant startup |

</div>

---

## âœ¨ Features

### ðŸ’» Terminal Execution
- **Run any shell command** from your AI agent
- Full **stdout/stderr** capture and streaming
- **Timeout protection** to prevent hanging processes
- Working directory control

### ðŸ“ Safe File Operations
- **Read** files with encoding detection
- **Write** with automatic backup creation
- **Patch** files with targeted replacements
- Path validation to prevent destructive operations

### ðŸ”„ Background Task Management
- **Queue** long-running commands
- **Monitor** task status and progress
- **Kill** stuck processes gracefully
- Async execution with result polling

### ðŸ” Live Web Search
- **DuckDuckGo** integration â€” no API key needed
- Search results with titles, URLs, and snippets
- Perfect for research-heavy coding tasks

---

## ðŸ—ï¸ How It Works

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚           AI AGENT (OpenCode)                â”‚
â”‚                                              â”‚
â”‚   "Run the tests"  "Edit config.py"          â”‚
â”‚   "Search for Flask docs"                    â”‚
â”‚                                              â”‚
â”‚         â”‚ HTTP REST API calls                â”‚
â”‚         â–¼                                    â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚         OPENCODE LOCAL API                   â”‚
â”‚         (Python HTTP Server)                 â”‚
â”‚                                              â”‚
â”‚   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚   â”‚ Terminal  â”‚  â”‚  Files   â”‚  â”‚  Search  â”‚ â”‚
â”‚   â”‚ Executor  â”‚  â”‚  Manager â”‚  â”‚  Engine  â”‚ â”‚
â”‚   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â”‚         â”‚              â”‚             â”‚       â”‚
â”‚         â–¼              â–¼             â–¼       â”‚
â”‚   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚   â”‚  Shell   â”‚  â”‚ Local FS â”‚  â”‚DuckDuckGoâ”‚ â”‚
â”‚   â”‚ (bash/   â”‚  â”‚  (safe)  â”‚  â”‚  (free)  â”‚ â”‚
â”‚   â”‚  cmd)    â”‚  â”‚          â”‚  â”‚          â”‚ â”‚
â”‚   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## ðŸš€ Quick Start

### Prerequisites

- **Python** 3.10+
- **pip** (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/yousufkidiya17/opencode-local-api.git
cd opencode-local-api

# Install dependencies
pip install -r requirements.txt

# Start the API server
python opencode_local_api.py
```

The API server will be running at `http://localhost:8000` ðŸŽ‰

### Connect to OpenCode

Point your OpenCode agent to `http://localhost:8000` and it will automatically discover and use the available tools.

---

## ðŸ”Œ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/execute` | Run a terminal command |
| `POST` | `/read-file` | Read a file's contents |
| `POST` | `/write-file` | Write content to a file |
| `POST` | `/patch-file` | Patch specific file sections |
| `POST` | `/search` | Perform web search |
| `POST` | `/background/start` | Start a background task |
| `GET` | `/background/status/:id` | Check task status |
| `POST` | `/background/kill/:id` | Kill a background task |
| `GET` | `/health` | Health check |

---

## ðŸ“ Project Structure

```
opencode-local-api/
â”œâ”€â”€ opencode_local_api.py  # Complete API server (single file!)
â”œâ”€â”€ requirements.txt       # Python dependencies
â”œâ”€â”€ LICENSE                # MIT License
â””â”€â”€ README.md
```

> ðŸ’¡ **Yes, it's a single file.** That's the beauty of it â€” zero complexity, maximum utility.

---

## ðŸ› ï¸ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Server** | Python, HTTP Server | Lightweight API |
| **Terminal** | subprocess | Command execution |
| **Search** | DuckDuckGo | Web search integration |
| **Files** | pathlib, os | Safe file operations |

</div>

---

## ðŸ›¡ï¸ Security

- **Path validation** â€” prevents directory traversal attacks
- **Command timeout** â€” no infinite hanging processes
- **Local-only** â€” binds to `localhost` by default
- **No authentication required** â€” designed for local development only

> âš ï¸ **Warning:** Do not expose this API to the internet. It's designed for local development use only.

---

## ðŸ“œ License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## ðŸ‘¨â€ðŸ’» Author

**Yousuf Kidiya**

[![GitHub](https://img.shields.io/badge/GitHub-yousufkidiya17-181717?style=for-the-badge&logo=github)](https://github.com/yousufkidiya17)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1e1e2e,100:0d1117&height=100&section=footer" width="100%"/>

**Made with ðŸ¤ for the AI Agent Community**

_If you found this project useful, please consider giving it a â­!_

</div>
