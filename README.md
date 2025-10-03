# Command Execution API

A Flask-based API that allows executing and streaming shell commands with real-time output. This API provides endpoints to execute commands and list available system commands organized by categories.

## Features

- Real-time streaming of command output
- List available system commands by categories
- Execute shell commands with live output
- Handles both stdout and stderr
- Command categorization and description

## API Endpoints

### 1. Execute Command
```
POST /execute
```
Executes a shell command and streams the output in real-time.

**Parameters:**
- `command` (form-data): The shell command to execute

**Example:**
```bash
curl -X POST -d "command=ping -c 5 google.com" http://localhost:5000/execute
```

### 2. List All Commands
```
GET /commands
```
Returns a JSON object containing all available commands grouped by categories.

**Example:**
```bash
curl http://localhost:5000/commands
```

### 3. List Category Commands
```
GET /commands/<category>
```
Returns commands for a specific category.

**Example:**
```bash
curl http://localhost:5000/commands/network
```

## Available Command Categories

1. **system_info**
   - System information commands (uname, lscpu, etc.)
   - Memory and CPU usage
   - Disk space information

2. **network**
   - Network interface information
   - Port and socket statistics
   - Network connectivity tools

3. **file_system**
   - Directory operations
   - File search and manipulation
   - Storage information

4. **package_management**
   - Package listing
   - Package search
   - Installation status

5. **process_management**
   - Process monitoring
   - Process control
   - System resource usage

6. **user_management**
   - User information
   - Session management
   - User activity monitoring

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/bloggercyber/gondolkucing.git
cd gondolkucing
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## Security Note

⚠️ This application executes shell commands directly on the host system. Use it only in trusted environments and implement appropriate security measures before deploying in production.

## Examples

1. Check system information:
```bash
curl -X POST -d "command=uname -a" http://localhost:5000/execute
```

2. List network interfaces:
```bash
curl -X POST -d "command=ip addr" http://localhost:5000/execute
```

3. View available network commands:
```bash
curl http://localhost:5000/commands/network
```

4. Monitor system resources:
```bash
curl -X POST -d "command=top -b -n 1" http://localhost:5000/execute
```

## Dependencies

- Flask 3.0.0
- Python 3.x

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is open source and available under the MIT License.