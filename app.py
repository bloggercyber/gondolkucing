from flask import Flask, Response, request, jsonify
import subprocess
import sys
import shutil
import json

app = Flask(__name__)

def get_available_commands():
    commands = {
        "system_info": {
            "uname -a": "Show system information",
            "lscpu": "Display CPU information",
            "free -h": "Show memory usage",
            "df -h": "Show disk space usage",
            "uptime": "Show system uptime",
            "ps aux": "List running processes"
        },
        "network": {
            "ip addr": "Show network interfaces",
            "netstat -tuln": "Show listening ports",
            "ss -tuln": "Show socket statistics",
            "ping": "Test network connectivity",
            "curl": "Transfer data from/to servers",
            "wget": "Download files from web"
        },
        "file_system": {
            "ls": "List directory contents",
            "pwd": "Print working directory",
            "find": "Search for files",
            "grep": "Search text content",
            "du -sh": "Show directory size",
            "tree": "Display directory tree"
        },
        "package_management": {
            "apt list --installed": "List installed packages",
            "apt search": "Search packages",
            "dpkg -l": "List installed packages (detailed)",
            "snap list": "List snap packages"
        },
        "process_management": {
            "top": "Monitor system processes",
            "htop": "Interactive process viewer",
            "kill": "Terminate processes",
            "pkill": "Kill processes by name",
            "pgrep": "List processes by name"
        },
        "user_management": {
            "whoami": "Show current user",
            "id": "Show user ID info",
            "last": "Show last logged in users",
            "w": "Show who is logged in"
        }
    }
    
    # Check which commands are actually available
    available_commands = {}
    for category, cmd_list in commands.items():
        available_in_category = {}
        for cmd_name, description in cmd_list.items():
            cmd_base = cmd_name.split()[0]  # Get the base command
            if shutil.which(cmd_base):  # Check if command exists
                available_in_category[cmd_name] = description
        if available_in_category:
            available_commands[category] = available_in_category
    
    return available_commands

def stream_command_output(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        text=True
    )
    
    for line in iter(process.stdout.readline, ''):
        yield line
    
    process.stdout.close()
    process.wait()

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    if not command:
        return 'No command provided', 400
    
    return Response(
        stream_command_output(command),
        mimetype='text/plain'
    )

@app.route('/commands', methods=['GET'])
def list_commands():
    """List all available system commands with their descriptions."""
    return jsonify(get_available_commands())

@app.route('/commands/<category>', methods=['GET'])
def list_category_commands(category):
    """List commands for a specific category."""
    commands = get_available_commands()
    if category in commands:
        return jsonify({category: commands[category]})
    return jsonify({"error": "Category not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)