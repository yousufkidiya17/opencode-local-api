from flask import Flask, request, jsonify
import subprocess
import tkinter as tk
import os
import threading
import time
from ddgs import DDGS

app = Flask(__name__)

background_tasks = {}

def get_creationflags():
    flags = 0
    if os.name == 'nt':
        try:
            flags = subprocess.CREATE_NO_WINDOW
        except AttributeError:
            flags = 0x08000000
    return flags

def ask_permission(cmd_or_action):
    result = {"allowed": False}
    
    def on_run(event=None):
        result["allowed"] = True
        root.destroy()
        
    def on_cancel(event=None):
        result["allowed"] = False
        root.destroy()
        
    root = tk.Tk()
    root.title("OpenCode API Permission")
    window_width = 500
    window_height = 200
    x_cordinate = int((root.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((root.winfo_screenheight()/2) - (window_height/2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    root.attributes('-topmost', True)
    
    tk.Label(root, text="OpenCode is requesting action:", font=("Arial", 12, "bold")).pack(pady=(15, 5))
    cmd_text = tk.Text(root, height=3, width=55, bg="#eaeaea", font=("Consolas", 10))
    cmd_text.insert(tk.END, cmd_or_action)
    cmd_text.config(state=tk.DISABLED)
    cmd_text.pack(padx=20, pady=5)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    btn_run = tk.Button(btn_frame, text="Allow (Alt+Enter)", command=on_run, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
    btn_run.pack(side=tk.LEFT, padx=10)
    btn_cancel = tk.Button(btn_frame, text="Deny (Esc)", command=on_cancel, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=15)
    btn_cancel.pack(side=tk.LEFT, padx=10)
    
    root.bind('<Alt-Return>', on_run)
    root.bind('<Escape>', on_cancel)
    root.focus_force()
    root.mainloop()
    return result["allowed"]

@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    if not data or 'command' not in data: return jsonify({'error': 'No command provided'}), 400
    try:
        if not ask_permission(f"RUN: {data['command']}"): return jsonify({'status': 'error', 'error': 'Canceled'}), 403
    except Exception as e: return jsonify({'status': 'error', 'error': str(e)}), 500
    try:
        result = subprocess.run(data['command'], shell=True, capture_output=True, text=True, timeout=30, creationflags=get_creationflags())
        return jsonify({'status': 'success', 'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    except subprocess.TimeoutExpired:
        return jsonify({'status': 'error', 'error': 'Command timed out'}), 408
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/run_background', methods=['POST'])
def run_background():
    data = request.get_json()
    if not data or 'command' not in data: return jsonify({'error': 'No command provided'}), 400
    try:
        if not ask_permission(f"RUN BACKGROUND: {data['command']}"): return jsonify({'status': 'error', 'error': 'Canceled'}), 403
    except Exception as e: return jsonify({'status': 'error', 'error': str(e)}), 500
    try:
        task_id = str(int(time.time()))
        proc = subprocess.Popen(data['command'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=get_creationflags())
        background_tasks[task_id] = proc
        return jsonify({'status': 'success', 'message': 'Started', 'task_id': task_id})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/read_file', methods=['POST'])
def read_file():
    data = request.get_json()
    if not data or 'path' not in data: return jsonify({'error': 'No path provided'}), 400
    try:
        with open(data['path'], 'r', encoding='utf-8') as f: return jsonify({'status': 'success', 'content': f.read()})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/write_file', methods=['POST'])
def write_file():
    data = request.get_json()
    if not data or 'path' not in data or 'content' not in data: return jsonify({'error': 'Missing path or content'}), 400
    try:
        if not ask_permission(f"WRITE FILE: {data['path']}"): return jsonify({'status': 'error', 'error': 'Canceled'}), 403
        with open(data['path'], 'w', encoding='utf-8') as f: f.write(data['content'])
        return jsonify({'status': 'success', 'message': f"Written to {data['path']}"})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500

@app.route('/search', methods=['POST'])
def search_web():
    data = request.get_json()
    if not data or 'query' not in data: return jsonify({'error': 'No query provided'}), 400
    try:
        results = DDGS().text(data['query'], max_results=data.get('limit', 5))
        return jsonify({'status': 'success', 'results': list(results)})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting OpenCode Advance API on port 5000...")
    app.run(host='0.0.0.0', port=5000)
