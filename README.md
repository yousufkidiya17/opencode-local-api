# OpenCode Local Agent API 🚀

Welcome to the **OpenCode Local API Setup Guide**. This repository is built specifically for users of the new [OpenCode](https://opencode.ai) desktop app or any similar locally working LLM Desktop clients (like Big Pickle, GPT-5 Nano, MiMo V2, etc.).

Since OpenCode is currently new and still catching up with IDE integrations, it often faces issues such as:
- Struggling to run continuous terminal tasks.
- Facing execution block/hang during long server deployments.
- Failing to search the live web.
- Cluttering the user's terminal with multiple prompt windows without explicit approval boxes.

This **Local API Script (`opencode_local_api.py`)** acts as an autonomous bridge. By running this script locally, you give your LLM Agent "Super-Powers" to autonomously manage the file system, execute background scripts safely, and browse the internet.

## Features ✨
1. **Windows UI Safety Permission**: An `Alt+Enter` GUI Box will pop up on your Windows desktop before the LLM can execute any shell command or edit a file. Stay safe!
2. **Background Task Runner (`/run_background`)**: Start scripts like Python bots, Scrapers, or AWS SSH commands, and return immediately to avoid a context-timeout hang. 
3. **Live Web Search (`/search`)**: Empowers the LLM with Live Google/Duckduckgo search data.
4. **Direct Read & Write File API**: Edit codebase safely using API rather than cumbersome bash commands.

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

You can even add a `.vbs` script pointing to this file in your Windows `Startup` folder so your API awakens every time you turn on your Laptop!

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
