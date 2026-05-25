# Module 4: Functions & Modules

## 📖 What You'll Learn
- Creating and using functions
- Function parameters and return values
- Default and keyword arguments
- Lambda functions
- Importing and using modules
- Creating your own modules

---

## 1. Creating Functions

### Concept Explanation

A **function** is a reusable block of code that performs a specific task. Functions help you:
- Avoid repeating code (DRY principle)
- Organize code into logical units
- Make code easier to test and maintain

**Syntax:**
```python
def function_name(parameters):
    """Docstring explaining what function does"""
    # code here
    return result
```

### DevOps Use Case

Functions are essential for:
- Checking server health repeatedly
- Deploying to multiple environments
- Parsing log files
- Making API calls
- Validating configurations
- Automating repetitive tasks

### Code Example

```python
# Basic function
def check_server_health():
    print("Checking server health...")
    return "healthy"

# Call the function
status = check_server_health()
print(f"Status: {status}")

# Function with parameters
def check_cpu(server_name, cpu_usage):
    if cpu_usage > 80:
        return f"{server_name}: HIGH CPU - {cpu_usage}%"
    else:
        return f"{server_name}: Normal - {cpu_usage}%"

# Call with arguments
result = check_cpu("web-01", 85)
print(result)

# Function with multiple return values
def get_server_stats(server):
    cpu = 75
    memory = 60
    disk = 80
    return cpu, memory, disk  # Returns tuple

cpu, mem, disk = get_server_stats("web-01")
print(f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")

# Function with docstring
def deploy_application(env, version):
    """
    Deploy application to specified environment.
    
    Args:
        env (str): Target environment (dev, staging, prod)
        version (str): Application version to deploy
    
    Returns:
        bool: True if deployment successful, False otherwise
    """
    print(f"Deploying version {version} to {env}")
    return True

# Real DevOps example
def validate_port(port):
    """Check if port number is valid"""
    if not isinstance(port, int):
        return False
    if port < 1 or port > 65535:
        return False
    return True

print(validate_port(8080))  # True
print(validate_port(99999))  # False
```

### Common Mistakes

❌ **Mistake 1**: Forgetting to return a value
```python
def calculate_uptime(hours):
    uptime = hours / 24
    # Forgot to return! Function returns None
```

❌ **Mistake 2**: Not calling the function
```python
def check_server():
    print("Checking...")

check_server  # Forgot parentheses! Doesn't execute
```

❌ **Mistake 3**: Wrong number of arguments
```python
def deploy(env, version):
    pass

deploy("prod")  # ERROR! Missing version argument
```

✅ **Fix**: Always return values, use parentheses, provide all arguments
```python
def calculate_uptime(hours):
    return hours / 24

check_server()  # Correct
deploy("prod", "1.0.0")  # Correct
```

---

## 2. Default and Keyword Arguments

### Concept Explanation

**Default arguments** provide default values for parameters.
**Keyword arguments** let you specify arguments by name.

### DevOps Use Case

Default arguments are perfect for:
- Default timeouts and retry counts
- Standard ports (80, 443)
- Default regions or environments
- Common configuration values

### Code Example

```python
# Default arguments
def connect_to_server(host, port=22, timeout=30):
    print(f"Connecting to {host}:{port} (timeout: {timeout}s)")
    return True

# Use defaults
connect_to_server("10.0.1.10")

# Override defaults
connect_to_server("10.0.1.10", 8080)
connect_to_server("10.0.1.10", 8080, 60)

# Keyword arguments (can be in any order)
connect_to_server(host="10.0.1.10", timeout=60, port=8080)
connect_to_server(timeout=60, host="10.0.1.10")

# Mix positional and keyword
connect_to_server("10.0.1.10", timeout=60)

# Real DevOps example
def deploy(environment, version, rollback=True, notify=True, parallel=False):
    """Deploy with configurable options"""
    print(f"Deploying {version} to {environment}")
    print(f"  Rollback enabled: {rollback}")
    print(f"  Notifications: {notify}")
    print(f"  Parallel: {parallel}")

# Use defaults
deploy("prod", "2.0.0")

# Override specific options
deploy("prod", "2.0.0", parallel=True)
deploy("staging", "2.1.0", rollback=False, notify=False)

# Function with *args (variable positional arguments)
def check_servers(*servers):
    """Check health of any number of servers"""
    for server in servers:
        print(f"Checking {server}...")

check_servers("web-01")
check_servers("web-01", "web-02", "web-03")

# Function with **kwargs (variable keyword arguments)
def create_server(**config):
    """Create server with any configuration options"""
    for key, value in config.items():
        print(f"  {key}: {value}")

create_server(name="web-01", cpu=4, memory=8, disk=100)
create_server(name="db-01", cpu=8, memory=16)
```

### Common Mistakes

❌ **Mistake 1**: Mutable default arguments
```python
def add_server(server, servers=[]):
    servers.append(server)
    return servers

# This causes unexpected behavior!
list1 = add_server("web-01")  # ['web-01']
list2 = add_server("web-02")  # ['web-01', 'web-02'] - WRONG!
```

✅ **Fix**: Use None as default
```python
def add_server(server, servers=None):
    if servers is None:
        servers = []
    servers.append(server)
    return servers
```

---

## 3. Lambda Functions

### Concept Explanation

**Lambda functions** are small, anonymous functions defined in one line.

**Syntax:** `lambda arguments: expression`

### DevOps Use Case

Lambdas are useful for:
- Sorting lists by specific criteria
- Filtering data
- Quick transformations
- Callback functions

### Code Example

```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(5, 3))  # 8
print(add_lambda(5, 3))  # 8

# Lambda with sorting
servers = [
    {"name": "web-01", "cpu": 75},
    {"name": "web-02", "cpu": 45},
    {"name": "web-03", "cpu": 90}
]

# Sort by CPU usage
sorted_servers = sorted(servers, key=lambda s: s["cpu"])
print("Sorted by CPU:")
for s in sorted_servers:
    print(f"  {s['name']}: {s['cpu']}%")

# Lambda with filter
high_cpu = list(filter(lambda s: s["cpu"] > 70, servers))
print(f"\nHigh CPU servers: {[s['name'] for s in high_cpu]}")

# Lambda with map
ports = [8080, 8081, 8082]
urls = list(map(lambda p: f"http://localhost:{p}", ports))
print(f"\nURLs: {urls}")

# Real DevOps example
logs = [
    {"level": "ERROR", "message": "Connection failed"},
    {"level": "INFO", "message": "Server started"},
    {"level": "ERROR", "message": "Timeout"},
    {"level": "WARNING", "message": "High memory"}
]

errors = list(filter(lambda log: log["level"] == "ERROR", logs))
print(f"\nErrors found: {len(errors)}")
```

---

## 4. Importing Modules

### Concept Explanation

**Modules** are Python files containing functions, classes, and variables you can reuse. Python has many built-in modules and you can create your own.

**Import methods:**
- `import module` - Import entire module
- `from module import function` - Import specific function
- `import module as alias` - Import with alias
- `from module import *` - Import everything (avoid in production)

### DevOps Use Case

Common modules for DevOps:
- `os` - Operating system operations
- `sys` - System-specific parameters
- `subprocess` - Run shell commands
- `json` - JSON parsing
- `datetime` - Date and time
- `requests` - HTTP requests
- `pathlib` - File paths

### Code Example

```python
# Import entire module
import os
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Import specific function
from os import getcwd
print(f"Current directory: {getcwd()}")

# Import with alias
import datetime as dt
now = dt.datetime.now()
print(f"Current time: {now}")

# Import multiple items
from os import getcwd, listdir, path

# Real DevOps examples
import json
import subprocess
from datetime import datetime

# Parse JSON configuration
config = '{"host": "localhost", "port": 8080}'
parsed = json.loads(config)
print(f"Host: {parsed['host']}")

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Timestamp: {timestamp}")

# Run shell command (we'll cover this more in Module 8)
# result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
# print(result.stdout)
```

---

## 5. Creating Your Own Modules

### Concept Explanation

You can create your own modules by saving functions in a `.py` file and importing them.

### Code Example

**File: server_utils.py**
```python
def check_health(server_name, cpu, memory):
    """Check if server is healthy"""
    if cpu > 90 or memory > 90:
        return f"{server_name}: CRITICAL"
    elif cpu > 80 or memory > 80:
        return f"{server_name}: WARNING"
    else:
        return f"{server_name}: OK"

def format_uptime(hours):
    """Convert hours to days and hours"""
    days = hours // 24
    remaining_hours = hours % 24
    return f"{days}d {remaining_hours}h"

def validate_ip(ip):
    """Basic IP validation"""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    return True
```

**File: main.py**
```python
# Import your module
import server_utils

# Use the functions
status = server_utils.check_health("web-01", 85, 75)
print(status)

uptime = server_utils.format_uptime(72)
print(f"Uptime: {uptime}")

is_valid = server_utils.validate_ip("192.168.1.1")
print(f"Valid IP: {is_valid}")

# Or import specific functions
from server_utils import check_health, validate_ip

status = check_health("web-02", 45, 60)
print(status)
```

---

## 🎯 Mini Exercise 1: Health Check Function

**Task**: Create a function that checks server health.

**Requirements:**
1. Function name: `check_server`
2. Parameters: `name`, `cpu`, `memory`
3. Return "OK" if both < 80, "WARNING" if either >= 80, "CRITICAL" if either >= 90
4. Test with different values

---

## ✅ Solution 1

```python
def check_server(name, cpu, memory):
    if cpu >= 90 or memory >= 90:
        return f"{name}: CRITICAL"
    elif cpu >= 80 or memory >= 80:
        return f"{name}: WARNING"
    else:
        return f"{name}: OK"

# Test
print(check_server("web-01", 45, 60))  # OK
print(check_server("web-02", 85, 70))  # WARNING
print(check_server("web-03", 95, 92))  # CRITICAL
```

---

## 🎯 Mini Exercise 2: Deployment Function

**Task**: Create a deployment function with default arguments.

**Requirements:**
1. Function name: `deploy`
2. Parameters: `environment`, `version`, `rollback=True`, `notify=True`
3. Print deployment details
4. Return True

---

## ✅ Solution 2

```python
def deploy(environment, version, rollback=True, notify=True):
    print(f"Deploying version {version} to {environment}")
    print(f"  Rollback enabled: {rollback}")
    print(f"  Notifications: {notify}")
    return True

# Test
deploy("prod", "2.0.0")
deploy("staging", "2.1.0", rollback=False)
deploy("dev", "2.2.0", notify=False, rollback=False)
```

---

## 📝 Key Takeaways

✅ **Functions make code reusable** - Write once, use many times
✅ **Use descriptive names** - `check_server_health()` not `check()`
✅ **Add docstrings** - Explain what function does
✅ **Use default arguments** - For common values
✅ **Return values** - Don't just print
✅ **Keep functions focused** - One function, one task
✅ **Create modules** - Organize related functions

---

## 🚀 Practice Challenge

Create a module called `devops_utils.py` with:
1. Function to validate port numbers (1-65535)
2. Function to format bytes to human-readable (KB, MB, GB)
3. Function to calculate percentage
4. Function to check if string is valid IP address

Then create a main script that imports and uses these functions.

---

## Next Module

Ready for **Module 5: Working with Files**? Learn to read logs, parse configs, and handle files! 🎯
