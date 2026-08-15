# OpenCode Local Agent API 🚀🔥

![GitHub release (latest by date)](https://img.shields.io/github/v/release/yousufkidiya17/opencode-local-api?style=flat-square)
![GitHub license](https://img.shields.io/github/license/yousufkidiya17/opencode-local-api?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
<p align="left">
  <img src="https://komarev.com/ghpvc/?username=yousufkidiya17&label=Views&color=blue&style=flat-square" alt="yousufkidiya17" />
</p>
Welcome to the **OpenCode Local API Setup Guide**. This repository is built specifically for users of the new [OpenCode](https://opencode.ai) desktop app or any similar locally working LLM Desktop clients (like Big Pickle, GPT-5 Nano, MiMo V2, etc.).

Since OpenCode is currently new and still catching up with IDE integrations, it often faces issues such as:
- Struggling to run continuous terminal tasks.
- Facing execution block/hang during long server deployments.
- Failing to search the live web.
- Cluttering the user's terminal with multiple prompt windows without explicit approval boxes.

This **Local API Script (`opencode_local_api.py`)** acts as an autonomous bridge. By running this script locally, you give your LLM Agent "Super-Powers" to autonomously manage the file system, execute background scripts safely, and browse the internet.

## Features ✨
1. **Safe Local Terminal Access (`/run`)**: The core feature! Allows your Agent to run full shell/terminal commands directly on your PC, completely silently without annoying black CMD windows popping up on your screen.
2. **Windows UI Safety Permission**: An `Alt+Enter` GUI Box will pop up on your Windows desktop before the LLM can execute any terminal command or edit a file. You are always in control!
3. **Background Task Runner (`/run_background`)**: Start long-running servers (like localhost or web scrapers) and return immediately. This solves the major issue where LLM agents "hang" or freeze forever when they try to start a server.
4. **Live Web Search (`/search`)**: Empowers the LLM with Live Google/Duckduckgo search data.
5. **Direct Read & Write File API (`/read_file`, `/write_file`)**: Edit your codebase safely using exact API endpoints rather than cumbersome bash commands which LLMs usually mess up.

## Installation 🛠️
1. Clone the repository and install dependencies:
```bash
git clone https://github.com/yousufkidiya17/opencode-local-api.git
cd opencode-local-api
pip install -r requirements.txt
```

2. **Starting the API Server:**
Run the server to listen on port `5000`:
```bash
python opencode_local_api.py
```

*Pro-tip for Windows Users:* To run the server entirely in the **background** (invisible), use:
```powershell
pythonw opencode_local_api.py
```

## 🚀 Auto-Start on Windows Boot (Set it and Forget it!)
If you want this API server to wake up silently in the background every time you turn on your computer (so you never have to manually run it again), follow these steps:

1. Press `Win + R`, type `shell:startup`, and hit Enter. This opens the Windows Startup folder.
2. In that folder, right-click -> New -> Text Document. Name it `opencode_startup.vbs` (make sure the extension is `.vbs` and not `.txt`).
3. Right-click, select **Edit**, and paste the following code (make sure to replace `D:\Private\opencode-local-api` with your actual repo path):

```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\Private\opencode-local-api"
WshShell.Run "pythonw.exe opencode_local_api.py", 0, False
```
Save and close! Now your API background terminal will automatically run invisibly every time you boot up!

## 🤖 The LLM Prompt (Crucial Step)
Every time you start a **New Session / Chat** in OpenCode, its memory resets. Simply copy and paste the following prompt block as your **very first message** to automatically load the API powers into the Agent:

```text
My terminal and file system local API are running at http://127.0.0.1:5000. For any actions on my PC, please make a POST request with JSON to the following endpoints based on your need:

1. `/run` - For normal terminal/bash commands. (Format: {"command": "your_command_here"})
2. `/run_background` - To start long-running tasks, servers, bots, or AWS scripts in the background and return immediately to avoid timeout. (Format: {"command": "your_background_command"})
3. `/read_file` - To strictly read entire file contents into context. (Format: {"path": "/absolute/path/file.py"})
4. `/write_file` - To directly create or overwrite a file safely. (Format: {"path": "/absolute/path", "content": "your_new_code_here"})
5. `/search` - To search live news or current data from the web. (Format: {"query": "bitcoin news today"})

Please do not ask me for permission in chat, my API has a Windows GUI pop-up built-in, and I will approve it manually. Run a test by using the `/run` endpoint to check the directory list (e.g. `dir`).
```

That's it! Watch your Agent instantly utilize the background terminal for all commands seamlessly.

## License
MIT License. Feel free to fork and improve this API bridge!
