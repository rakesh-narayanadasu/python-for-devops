# Module 8: OS & System Automation

## 📖 What You'll Learn
- os module for system operations
- subprocess module for running commands
- pathlib for modern path handling
- Environment variables
- Automating system tasks

---

## 1. The os Module

### Concept Explanation

The `os` module provides functions to interact with the operating system.

**Common operations:**
- File/directory operations
- Environment variables
- Process management
- Path operations

### DevOps Use Case

- Check if files/directories exist
- Create/delete directories
- Get environment variables
- Execute system commands
- Navigate file systems

### Code Example

```python
import os

# Current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Change directory
os.chdir('/path/to/directory')

# List directory contents
files = os.listdir('.')
print(f"Files: {files}")

# Check if path exists
if os.path.exists('/var/log/app.log'):
    print("Log file exists")

# Check if it's a file or directory
if os.path.isfile('config.txt'):
    print("It's a file")
if os.path.isdir('/var/log'):
    print("It's a directory")

# Get file size
size = os.path.getsize('config.txt')
print(f"File size: {size} bytes")

# Create directory
os.mkdir('new_directory')

# Create nested directories
os.makedirs('parent/child/grandchild', exist_ok=True)

# Remove directory
os.rmdir('new_directory')

# Remove file
os.remove('temp_file.txt')

# Rename file
os.rename('old_name.txt', 'new_name.txt')

# Environment variables
home = os.getenv('HOME')
path = os.getenv('PATH')
custom = os.getenv('CUSTOM_VAR', 'default_value')

# Set environment variable
os.environ['MY_VAR'] = 'my_value'

# Path operations
full_path = os.path.join('logs', 'app', 'error.log')
# Windows: logs\app\error.log
# Linux: logs/app/error.log

directory = os.path.dirname('/var/log/app.log')  # /var/log
filename = os.path.basename('/var/log/app.log')  # app.log
name, ext = os.path.splitext('config.yaml')  # ('config', '.yaml')

# Real DevOps example: Check log directory
log_dir = '/var/log/myapp'

if not os.path.exists(log_dir):
    print(f"Creating log directory: {log_dir}")
    os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, 'app.log')
print(f"Log file path: {log_file}")
```

---

## 2. The subprocess Module

### Concept Explanation

The `subprocess` module allows you to run shell commands from Python and capture their output.

**Methods:**
- `subprocess.run()` - Run command and wait
- `subprocess.Popen()` - Run command asynchronously
- `subprocess.check_output()` - Run and return output

### DevOps Use Case

- Run shell commands
- Execute deployment scripts
- Check service status
- Run git commands
- Execute docker/kubectl commands
- Automate system administration

### Code Example

```python
import subprocess

# Basic command execution
result = subprocess.run(['echo', 'Hello World'], capture_output=True, text=True)
print(result.stdout)  # Hello World

# Run command and check return code
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
if result.returncode == 0:
    print("Command successful")
    print(result.stdout)
else:
    print("Command failed")
    print(result.stderr)

# Run with shell=True (use carefully!)
result = subprocess.run('dir', shell=True, capture_output=True, text=True)
print(result.stdout)

# Check if command succeeds (raises exception on failure)
try:
    subprocess.run(['invalid_command'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code {e.returncode}")

# Real DevOps examples:

# 1. Check disk space
result = subprocess.run(['df', '-h'], capture_output=True, text=True)
print("Disk usage:")
print(result.stdout)

# 2. Check service status (Linux)
result = subprocess.run(['systemctl', 'status', 'nginx'], 
                       capture_output=True, text=True)
if 'active (running)' in result.stdout:
    print("Nginx is running")

# 3. Git operations
result = subprocess.run(['git', 'status'], capture_output=True, text=True)
print(result.stdout)

# 4. Docker commands
result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
print("Running containers:")
print(result.stdout)

# 5. Run with timeout
try:
    result = subprocess.run(['long_running_command'], 
                           timeout=30, 
                           capture_output=True, 
                           text=True)
except subprocess.TimeoutExpired:
    print("Command timed out after 30 seconds")

# 6. Pipe commands
# Get running processes and filter
ps = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
lines = ps.stdout.split('\n')
python_processes = [line for line in lines if 'python' in line.lower()]
print("Python processes:")
for proc in python_processes:
    print(proc)
```

---

## 3. pathlib Module (Modern Approach)

### Concept Explanation

`pathlib` provides an object-oriented approach to file paths.

### Code Example

```python
from pathlib import Path

# Create path object
log_dir = Path('/var/log')
config_file = Path('config.yaml')

# Join paths
log_file = log_dir / 'app' / 'error.log'
print(log_file)  # /var/log/app/error.log

# Check existence
if log_file.exists():
    print("File exists")

if log_dir.is_dir():
    print("It's a directory")

# Create directory
new_dir = Path('logs/app')
new_dir.mkdir(parents=True, exist_ok=True)

# Read file
config = Path('config.txt')
content = config.read_text()

# Write file
config.write_text("host=localhost\nport=8080")

# Get file info
stat = config.stat()
print(f"Size: {stat.st_size} bytes")
print(f"Modified: {stat.st_mtime}")

# List directory
log_dir = Path('/var/log')
for file in log_dir.glob('*.log'):
    print(file)

# Recursive search
for file in log_dir.rglob('*.log'):
    print(file)

# Path components
path = Path('/var/log/app/error.log')
print(path.parent)      # /var/log/app
print(path.name)        # error.log
print(path.stem)        # error
print(path.suffix)      # .log
print(path.parts)       # ('/', 'var', 'log', 'app', 'error.log')

# Real DevOps example: Find all Python files
project_dir = Path('.')
python_files = list(project_dir.rglob('*.py'))
print(f"Found {len(python_files)} Python files")
for file in python_files:
    print(f"  {file}")
```

---

## 4. Environment Variables

### Concept Explanation

Environment variables store configuration outside your code.

### DevOps Use Case

- Store credentials (API keys, passwords)
- Configuration per environment (dev/staging/prod)
- CI/CD pipeline variables
- Docker container configuration

### Code Example

```python
import os
from dotenv import load_dotenv  # pip install python-dotenv

# Read environment variables
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
debug = os.getenv('DEBUG', 'False') == 'True'

# Set environment variable
os.environ['MY_VAR'] = 'value'

# Using .env file
# Create .env file:
# DATABASE_URL=postgresql://localhost/mydb
# API_KEY=secret123
# DEBUG=True

load_dotenv()  # Load from .env file

database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')

# Real DevOps example: Configuration
class Config:
    def __init__(self):
        load_dotenv()
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
        self.api_key = os.getenv('API_KEY')
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = os.getenv('DEBUG', 'False') == 'True'
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
    
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY not set")
        if self.environment not in ['development', 'staging', 'production']:
            raise ValueError(f"Invalid environment: {self.environment}")

config = Config()
config.validate()
```

---

## 5. Real DevOps Automation Examples

### Example 1: Backup Script

```python
import os
import subprocess
from datetime import datetime
from pathlib import Path

def backup_directory(source, backup_dir):
    """Create timestamped backup of directory"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{timestamp}.tar.gz"
    backup_path = Path(backup_dir) / backup_name
    
    # Create backup directory if doesn't exist
    Path(backup_dir).mkdir(parents=True, exist_ok=True)
    
    # Create compressed backup
    cmd = ['tar', '-czf', str(backup_path), source]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        size = backup_path.stat().st_size
        print(f"Backup created: {backup_path} ({size} bytes)")
        return True
    else:
        print(f"Backup failed: {result.stderr}")
        return False

# Usage
backup_directory('/var/www/html', '/backups')
```

### Example 2: Log Rotation

```python
import os
from pathlib import Path
from datetime import datetime

def rotate_logs(log_dir, max_files=5):
    """Keep only the latest N log files"""
    log_path = Path(log_dir)
    
    if not log_path.exists():
        print(f"Log directory not found: {log_dir}")
        return
    
    # Get all .log files
    log_files = sorted(log_path.glob('*.log'), 
                      key=lambda x: x.stat().st_mtime,
                      reverse=True)
    
    # Keep only max_files
    for log_file in log_files[max_files:]:
        print(f"Removing old log: {log_file}")
        log_file.unlink()
    
    print(f"Kept {min(len(log_files), max_files)} log files")

# Usage
rotate_logs('/var/log/myapp', max_files=5)
```

### Example 3: Service Health Check

```python
import subprocess
import time

def check_service_status(service_name):
    """Check if a service is running"""
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip() == 'active'
    except subprocess.TimeoutExpired:
        return False
    except FileNotFoundError:
        # systemctl not available (not Linux)
        return None

def restart_service_if_down(service_name, max_retries=3):
    """Restart service if it's down"""
    for attempt in range(1, max_retries + 1):
        if check_service_status(service_name):
            print(f"{service_name} is running")
            return True
        
        print(f"Attempt {attempt}: {service_name} is down, restarting...")
        subprocess.run(['systemctl', 'restart', service_name])
        time.sleep(5)
    
    print(f"Failed to restart {service_name} after {max_retries} attempts")
    return False

# Usage
restart_service_if_down('nginx')
```

### Example 4: Disk Space Monitor

```python
import subprocess
import os

def check_disk_space(path='/', threshold=80):
    """Check if disk usage exceeds threshold"""
    result = subprocess.run(
        ['df', '-h', path],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    if len(lines) < 2:
        return None
    
    # Parse output
    parts = lines[1].split()
    usage_percent = int(parts[4].rstrip('%'))
    
    return {
        'path': path,
        'total': parts[1],
        'used': parts[2],
        'available': parts[3],
        'usage_percent': usage_percent,
        'alert': usage_percent > threshold
    }

# Usage
disk_info = check_disk_space('/')
if disk_info and disk_info['alert']:
    print(f"⚠ Disk usage high: {disk_info['usage_percent']}%")
else:
    print(f"✓ Disk usage OK: {disk_info['usage_percent']}%")
```

---

## 🎯 Mini Exercise 1: Directory Creator

**Task**: Create a function that creates a directory structure for a new project.

**Requirements:**
- Create main directory
- Create subdirectories: src, tests, logs, config
- Create empty __init__.py files

---

## ✅ Solution 1

```python
from pathlib import Path

def create_project_structure(project_name):
    base = Path(project_name)
    
    # Create directories
    (base / 'src').mkdir(parents=True, exist_ok=True)
    (base / 'tests').mkdir(parents=True, exist_ok=True)
    (base / 'logs').mkdir(parents=True, exist_ok=True)
    (base / 'config').mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py files
    (base / 'src' / '__init__.py').touch()
    (base / 'tests' / '__init__.py').touch()
    
    print(f"Project structure created: {project_name}")

create_project_structure('my-devops-tool')
```

---

## 📝 Key Takeaways

✅ **Use os module** - For system operations
✅ **Use subprocess** - For running commands
✅ **Use pathlib** - Modern path handling
✅ **Use environment variables** - For configuration
✅ **Handle errors** - Commands can fail
✅ **Use timeouts** - Prevent hanging
✅ **Be careful with shell=True** - Security risk

---

## 🚀 Practice Challenge

Create a system monitoring script that:
1. Checks disk space
2. Lists running processes
3. Checks if specific services are running
4. Creates a report file with timestamp
5. Sends alert if disk > 80%

---

## Next Module

Ready for **Module 9: JSON, YAML & APIs**? Learn to work with data formats and APIs! 🎯
