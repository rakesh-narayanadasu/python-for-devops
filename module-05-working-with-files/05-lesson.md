# Module 5: Working with Files

## 📖 What You'll Learn
- Reading and writing files
- Working with log files
- Parsing configuration files
- File handling best practices
- Context managers

---

## 1. Reading Files

### Concept Explanation

Python provides several ways to read files. The most common methods:
- `read()` - Read entire file as string
- `readline()` - Read one line
- `readlines()` - Read all lines as list
- Iterate line by line (memory efficient)

### DevOps Use Case

Reading files is essential for:
- Analyzing log files
- Reading configuration files
- Processing deployment manifests
- Parsing CSV/JSON data
- Reading secrets and credentials

### Code Example

```python
# Method 1: Read entire file
with open('server.log', 'r') as file:
    content = file.read()
    print(content)

# Method 2: Read line by line (memory efficient for large files)
with open('server.log', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Method 3: Read all lines as list
with open('server.log', 'r') as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

# Method 4: Read specific number of lines
with open('server.log', 'r') as file:
    first_line = file.readline()
    second_line = file.readline()

# Real DevOps example: Parse log file for errors
with open('application.log', 'r') as file:
    error_count = 0
    for line in file:
        if 'ERROR' in line:
            error_count += 1
            print(line.strip())
    print(f"\nTotal errors: {error_count}")

# Read with encoding
with open('config.txt', 'r', encoding='utf-8') as file:
    content = file.read()
```

### Common Mistakes

❌ **Mistake 1**: Not closing files
```python
file = open('data.txt', 'r')
content = file.read()
# Forgot to close! Resource leak
```

❌ **Mistake 2**: Reading large files into memory
```python
# Bad for large log files
with open('huge.log', 'r') as file:
    content = file.read()  # Loads entire file into memory!
```

✅ **Fix**: Use context manager, iterate line by line
```python
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed

# For large files
with open('huge.log', 'r') as file:
    for line in file:  # Reads one line at a time
        process(line)
```

---

## 2. Writing Files

### Concept Explanation

File modes for writing:
- `'w'` - Write (overwrites existing file)
- `'a'` - Append (adds to end of file)
- `'x'` - Exclusive create (fails if file exists)
- `'r+'` - Read and write

### DevOps Use Case

Writing files for:
- Creating configuration files
- Generating reports
- Writing logs
- Creating deployment scripts
- Saving metrics

### Code Example

```python
# Write to file (overwrites)
with open('output.txt', 'w') as file:
    file.write("Server Status Report\n")
    file.write("=" * 50 + "\n")
    file.write("All servers operational\n")

# Append to file
with open('output.txt', 'a') as file:
    file.write("Additional info\n")

# Write multiple lines
lines = [
    "web-01: healthy\n",
    "web-02: healthy\n",
    "db-01: healthy\n"
]
with open('status.txt', 'w') as file:
    file.writelines(lines)

# Real DevOps example: Generate server report
servers = [
    {"name": "web-01", "cpu": 45, "status": "healthy"},
    {"name": "web-02", "cpu": 78, "status": "warning"},
    {"name": "db-01", "cpu": 55, "status": "healthy"}
]

with open('server_report.txt', 'w') as file:
    file.write("SERVER HEALTH REPORT\n")
    file.write("=" * 50 + "\n\n")
    
    for server in servers:
        line = f"{server['name']}: CPU {server['cpu']}% - {server['status']}\n"
        file.write(line)
    
    file.write("\n" + "=" * 50 + "\n")
    file.write(f"Total servers: {len(servers)}\n")

print("Report generated: server_report.txt")

# Create file only if it doesn't exist
try:
    with open('new_config.txt', 'x') as file:
        file.write("Initial configuration\n")
except FileExistsError:
    print("File already exists!")
```

---

## 3. Working with Log Files

### Concept Explanation

Log files are crucial in DevOps. Common tasks:
- Filter by log level (ERROR, WARNING, INFO)
- Extract timestamps
- Count occurrences
- Find patterns

### Code Example

```python
# Example log format:
# 2024-01-30 10:15:23 ERROR Database connection failed
# 2024-01-30 10:15:24 INFO Server started
# 2024-01-30 10:15:25 WARNING High memory usage

# Parse log file
def analyze_logs(log_file):
    stats = {
        'ERROR': 0,
        'WARNING': 0,
        'INFO': 0
    }
    
    errors = []
    
    with open(log_file, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Count by level
            if 'ERROR' in line:
                stats['ERROR'] += 1
                errors.append(line)
            elif 'WARNING' in line:
                stats['WARNING'] += 1
            elif 'INFO' in line:
                stats['INFO'] += 1
    
    return stats, errors

# Usage
stats, errors = analyze_logs('application.log')
print("Log Statistics:")
for level, count in stats.items():
    print(f"  {level}: {count}")

print("\nErrors found:")
for error in errors:
    print(f"  {error}")

# Extract specific information
def extract_failed_requests(log_file):
    failed_requests = []
    
    with open(log_file, 'r') as file:
        for line in file:
            if 'HTTP 500' in line or 'HTTP 404' in line:
                failed_requests.append(line.strip())
    
    return failed_requests

# Filter logs by date
def filter_logs_by_date(log_file, target_date):
    """Filter logs for specific date (format: 2024-01-30)"""
    matching_logs = []
    
    with open(log_file, 'r') as file:
        for line in file:
            if line.startswith(target_date):
                matching_logs.append(line.strip())
    
    return matching_logs

# Real example: Find top errors
def find_top_errors(log_file, top_n=5):
    error_counts = {}
    
    with open(log_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                # Extract error message (simplified)
                parts = line.split('ERROR')
                if len(parts) > 1:
                    error_msg = parts[1].strip()
                    error_counts[error_msg] = error_counts.get(error_msg, 0) + 1
    
    # Sort by count
    sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_errors[:top_n]
```

---

## 4. Parsing Configuration Files

### Concept Explanation

Configuration files come in various formats:
- Plain text (key=value)
- INI files
- Properties files
- Simple custom formats

### Code Example

```python
# Parse simple config file (key=value format)
def parse_config(config_file):
    config = {}
    
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Parse key=value
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    
    return config

# Example config file content:
# host=localhost
# port=8080
# timeout=30
# # This is a comment
# debug=true

config = parse_config('app.config')
print(f"Host: {config.get('host')}")
print(f"Port: {config.get('port')}")

# Write configuration file
def write_config(config_file, config_dict):
    with open(config_file, 'w') as file:
        file.write("# Application Configuration\n")
        file.write(f"# Generated: {datetime.now()}\n\n")
        
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")

config = {
    'host': 'localhost',
    'port': 8080,
    'timeout': 30,
    'debug': True
}
write_config('app.config', config)

# Parse hosts file format
def parse_hosts_file(hosts_file):
    """Parse /etc/hosts style file"""
    hosts = []
    
    with open(hosts_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split()
            if len(parts) >= 2:
                ip = parts[0]
                hostname = parts[1]
                hosts.append({'ip': ip, 'hostname': hostname})
    
    return hosts
```

---

## 5. File Handling Best Practices

### Concept Explanation

**Context Managers (`with` statement)**:
- Automatically closes files
- Handles exceptions properly
- Cleaner code

**Best Practices**:
- Always use `with` statement
- Handle exceptions
- Use appropriate encoding
- Don't load large files entirely into memory
- Close files properly

### Code Example

```python
# ✅ GOOD: Using context manager
with open('file.txt', 'r') as file:
    content = file.read()
# File automatically closed, even if exception occurs

# ❌ BAD: Manual file handling
file = open('file.txt', 'r')
content = file.read()
file.close()  # Might not execute if exception occurs

# Handle file not found
try:
    with open('config.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Config file not found, using defaults")
    content = "default_config"

# Check if file exists before reading
import os

if os.path.exists('config.txt'):
    with open('config.txt', 'r') as file:
        content = file.read()
else:
    print("File doesn't exist")

# Read large file efficiently
def process_large_log(log_file):
    """Process large log file line by line"""
    error_count = 0
    
    with open(log_file, 'r') as file:
        for line in file:  # Reads one line at a time
            if 'ERROR' in line:
                error_count += 1
                # Process line immediately, don't store all
    
    return error_count

# Read and write simultaneously
def filter_logs(input_file, output_file, keyword):
    """Filter logs containing keyword"""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if keyword in line:
                outfile.write(line)

# Real DevOps example: Rotate log file
def rotate_log(log_file, max_lines=1000):
    """Keep only last N lines of log file"""
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    if len(lines) > max_lines:
        # Keep only last max_lines
        with open(log_file, 'w') as file:
            file.writelines(lines[-max_lines:])
        print(f"Rotated log: kept last {max_lines} lines")
```

---

## 6. Working with Paths

### Code Example

```python
import os
from pathlib import Path

# Using os module
current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'logs', 'app.log')
print(f"File path: {file_path}")

# Check if file/directory exists
if os.path.exists(file_path):
    print("File exists")

if os.path.isfile(file_path):
    print("It's a file")

if os.path.isdir('/var/log'):
    print("It's a directory")

# Get file info
if os.path.exists('app.log'):
    size = os.path.getsize('app.log')
    print(f"File size: {size} bytes")

# Using pathlib (modern approach)
log_dir = Path('/var/log')
log_file = log_dir / 'app.log'

if log_file.exists():
    print(f"File exists: {log_file}")
    print(f"Size: {log_file.stat().st_size} bytes")

# Create directory if doesn't exist
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)  # exist_ok=True prevents error if exists

# List files in directory
for file in log_dir.glob('*.log'):
    print(f"Found log file: {file}")
```

---

## 🎯 Mini Exercise 1: Read and Count

**Task**: Read a log file and count ERROR, WARNING, INFO messages.

**Create a sample log file first:**
```
2024-01-30 10:00:00 INFO Server started
2024-01-30 10:00:01 ERROR Database connection failed
2024-01-30 10:00:02 WARNING High CPU usage
2024-01-30 10:00:03 INFO Request processed
2024-01-30 10:00:04 ERROR Timeout
```

---

## ✅ Solution 1

```python
def count_log_levels(log_file):
    counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}
    
    with open(log_file, 'r') as file:
        for line in file:
            for level in counts.keys():
                if level in line:
                    counts[level] += 1
                    break
    
    return counts

counts = count_log_levels('app.log')
for level, count in counts.items():
    print(f"{level}: {count}")
```

---

## 🎯 Mini Exercise 2: Generate Server Report

**Task**: Create a function that writes a server status report to a file.

---

## ✅ Solution 2

```python
def generate_report(servers, output_file):
    with open(output_file, 'w') as file:
        file.write("SERVER STATUS REPORT\n")
        file.write("=" * 50 + "\n\n")
        
        for server in servers:
            line = f"{server['name']}: {server['status']} (CPU: {server['cpu']}%)\n"
            file.write(line)
        
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Total: {len(servers)} servers\n")

servers = [
    {'name': 'web-01', 'status': 'healthy', 'cpu': 45},
    {'name': 'web-02', 'status': 'warning', 'cpu': 85}
]
generate_report(servers, 'report.txt')
```

---

## 📝 Key Takeaways

✅ **Always use `with` statement** - Automatic file closing
✅ **Iterate line by line** - For large files
✅ **Handle exceptions** - FileNotFoundError, PermissionError
✅ **Use appropriate encoding** - Usually 'utf-8'
✅ **Check file existence** - Before operations
✅ **Use pathlib** - Modern path handling
✅ **Close files properly** - Prevent resource leaks

---

## 🚀 Practice Challenge

Create a log analyzer that:
1. Reads a log file
2. Counts ERROR, WARNING, INFO
3. Extracts all error messages
4. Writes a summary report to a new file
5. Handles file not found gracefully

---

## Next Module

Ready for **Module 6: Exception Handling**? Learn to handle errors gracefully! 🎯
