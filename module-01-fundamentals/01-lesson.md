# Module 1: Python Fundamentals

## 📖 What You'll Learn
- Python syntax and indentation rules
- How to write comments
- Variables and data types
- Type conversion

---

## 1. Python Syntax & Indentation

### Concept Explanation

Python uses **indentation** (spaces or tabs) to define code blocks, unlike other languages that use curly braces `{}`. This makes Python code clean and readable.

**Key Rules:**
- Use 4 spaces for indentation (industry standard)
- Don't mix tabs and spaces
- Indentation matters - wrong indentation = error

### DevOps Use Case

When writing automation scripts, proper indentation ensures your conditional logic (like checking if a server is up) executes correctly. Messy indentation can cause deployment scripts to fail.

### Code Example

```python
# Correct indentation
if server_status == "running":
    print("Server is healthy")
    log_status("OK")
else:
    print("Server is down")
    send_alert()

# Wrong indentation - will cause IndentationError
if server_status == "running":
print("This will fail")  # Not indented!
```

### Common Mistakes

❌ **Mistake 1**: Mixing tabs and spaces
```python
if True:
    print("Using spaces")
	print("Using tab - ERROR!")
```

❌ **Mistake 2**: Inconsistent indentation
```python
if True:
    print("4 spaces")
      print("6 spaces - ERROR!")
```

✅ **Fix**: Always use 4 spaces consistently

---

## 2. Comments

### Concept Explanation

Comments are notes in your code that Python ignores. They explain what your code does.

**Types:**
- Single-line comments: `#`
- Multi-line comments: `'''` or `"""`

### DevOps Use Case

In DevOps scripts, comments document:
- What the script does
- Why certain configurations exist
- Warnings for other team members
- API endpoints and credentials locations

### Code Example

```python
# This is a single-line comment
# It helps explain what the code does

# Check if backup completed successfully
backup_status = "completed"

'''
This is a multi-line comment.
Use it for longer explanations.
Author: DevOps Team
Purpose: Daily backup verification
'''

"""
You can also use double quotes
for multi-line comments
"""

# TODO: Add email notification feature
# FIXME: Handle timeout errors better
```

### Common Mistakes

❌ **Mistake**: Over-commenting obvious code
```python
# Assign 5 to x
x = 5  # This comment is unnecessary
```

✅ **Better**: Comment the "why", not the "what"
```python
# Using 5-second timeout to prevent hanging on slow networks
timeout = 5
```

---

## 3. Variables and Data Types

### Concept Explanation

A **variable** is a container that stores data. Python has several built-in data types:

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `42`, `-10`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |
| `str` | Text (string) | `"hello"`, `'DevOps'` |
| `bool` | True/False | `True`, `False` |

**Variable Naming Rules:**
- Start with letter or underscore: `server_name`, `_temp`
- Can contain letters, numbers, underscores: `server1`, `db_host_2`
- Case-sensitive: `Server` ≠ `server`
- Use snake_case for readability: `max_retry_count`

### DevOps Use Case

Variables store:
- Server hostnames and IP addresses
- Port numbers and timeouts
- API keys and credentials
- Status codes and error messages
- Configuration values

### Code Example

```python
# Integer - for counts, ports, status codes
server_count = 5
http_port = 8080
status_code = 200
max_retries = 3

# Float - for metrics, percentages, time
cpu_usage = 85.5
response_time = 0.234
disk_usage_percent = 78.9

# String - for names, messages, paths
server_name = "web-server-01"
environment = "production"
log_path = "/var/log/app.log"
error_message = "Connection timeout"

# Boolean - for flags, status checks
is_healthy = True
backup_completed = False
ssl_enabled = True

# Printing variables
print(server_name)  # Output: web-server-01
print("Server count:", server_count)  # Output: Server count: 5
print(f"CPU Usage: {cpu_usage}%")  # Output: CPU Usage: 85.5%
```

### Common Mistakes

❌ **Mistake 1**: Using reserved keywords
```python
# These are Python keywords - don't use as variable names
if = 5  # ERROR!
for = "test"  # ERROR!
class = "web"  # ERROR!
```

❌ **Mistake 2**: Starting with numbers
```python
1server = "web"  # ERROR!
```

❌ **Mistake 3**: Using spaces in names
```python
server name = "web-01"  # ERROR!
```

✅ **Fix**: Use proper naming
```python
server_name = "web-01"
server1 = "web"
web_class = "frontend"
```

---

## 4. Type Conversion

### Concept Explanation

**Type conversion** (or type casting) means changing data from one type to another.

**Common conversions:**
- `int()` - Convert to integer
- `float()` - Convert to decimal
- `str()` - Convert to string
- `bool()` - Convert to boolean

### DevOps Use Case

Type conversion is crucial when:
- Reading port numbers from config files (string → int)
- Formatting metrics for display (int → string)
- Processing user input from scripts
- Parsing environment variables (always strings)

### Code Example

```python
# String to Integer
port_string = "8080"
port_number = int(port_string)
print(port_number + 1)  # Output: 8081

# String to Float
cpu_string = "85.5"
cpu_value = float(cpu_string)
print(cpu_value)  # Output: 85.5

# Integer to String
status_code = 200
message = "Status: " + str(status_code)
print(message)  # Output: Status: 200

# Float to Integer (removes decimal)
response_time = 1.8
rounded_time = int(response_time)
print(rounded_time)  # Output: 1

# Any value to Boolean
# Empty values = False, non-empty = True
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("text"))  # True

# Practical DevOps example
server_count = "5"  # From config file
total_servers = int(server_count) + 3
print(f"Total servers: {total_servers}")  # Output: Total servers: 8
```

### Common Mistakes

❌ **Mistake 1**: Converting invalid strings
```python
port = int("8080abc")  # ERROR! ValueError
```

❌ **Mistake 2**: Concatenating different types
```python
port = 8080
message = "Port: " + port  # ERROR! Can't concatenate str and int
```

✅ **Fix**: Convert before concatenating
```python
port = 8080
message = "Port: " + str(port)  # Correct!
# Or use f-strings (better)
message = f"Port: {port}"  # Correct!
```

---

## 🎯 Mini Exercise 1: Server Configuration

**Task**: Create variables for a web server configuration and print a summary.

**Requirements:**
1. Create variables for:
   - Server name (string)
   - IP address (string)
   - Port number (integer)
   - Is active (boolean)
   - CPU usage (float)
2. Print a formatted summary

**Try it yourself before looking at the solution!**

---

## ✅ Solution 1

```python
# Server configuration variables
server_name = "web-prod-01"
ip_address = "192.168.1.100"
port = 443
is_active = True
cpu_usage = 67.8

# Print summary
print("=" * 40)
print("SERVER CONFIGURATION")
print("=" * 40)
print(f"Server Name: {server_name}")
print(f"IP Address: {ip_address}")
print(f"Port: {port}")
print(f"Status: {'Active' if is_active else 'Inactive'}")
print(f"CPU Usage: {cpu_usage}%")
print("=" * 40)
```

**Output:**
```
========================================
SERVER CONFIGURATION
========================================
Server Name: web-prod-01
IP Address: 192.168.1.100
Port: 443
Status: Active
CPU Usage: 67.8%
========================================
```

---

## 🎯 Mini Exercise 2: Type Conversion Challenge

**Task**: Fix the following code that has type conversion errors.

```python
# This code has errors - fix them!
port = "8080"
max_connections = "100"
timeout = "30.5"

# Calculate total capacity
total_capacity = max_connections * 2  # Should be 200

# Create message
message = "Server running on port " + port + " with timeout " + timeout + "s"

# Check if port is standard HTTP
if port == 80:
    print("Using standard HTTP port")
```

**Try to fix it yourself!**

---

## ✅ Solution 2

```python
# Fixed code with proper type conversions
port = "8080"
max_connections = "100"
timeout = "30.5"

# Convert to appropriate types
port_int = int(port)
max_connections_int = int(max_connections)
timeout_float = float(timeout)

# Calculate total capacity
total_capacity = max_connections_int * 2  # Now works: 200

# Create message using f-strings (best practice)
message = f"Server running on port {port} with timeout {timeout}s"
print(message)

# Check if port is standard HTTP (convert for comparison)
if port_int == 80:
    print("Using standard HTTP port")
else:
    print(f"Using custom port: {port_int}")
```

**Output:**
```
Server running on port 8080 with timeout 30.5s
Using custom port: 8080
```

---

## 📝 Key Takeaways

✅ **Indentation is crucial** - Always use 4 spaces consistently
✅ **Comment the "why"** - Not the obvious "what"
✅ **Use descriptive variable names** - `server_name` not `sn`
✅ **Know your data types** - int, float, str, bool
✅ **Convert types when needed** - Especially when reading configs
✅ **Use f-strings** - Modern and readable string formatting

---

## 🚀 Practice Challenge

Create a script that:
1. Stores information about 3 servers (name, IP, port, status)
2. Converts port numbers from strings to integers
3. Calculates total number of active servers
4. Prints a formatted report

**Hint**: Use the concepts you learned in this module!

---

## Next Module

Ready to move on? Head to **Module 2: Control Flow** to learn about conditions and loops! 🎯
