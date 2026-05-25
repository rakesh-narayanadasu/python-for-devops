# Module 3: Data Structures

## 📖 What You'll Learn
- Lists (most important for DevOps)
- Tuples (immutable sequences)
- Sets (unique collections)
- Dictionaries (key-value pairs)
- When to use each data structure

---

## 1. Lists

### Concept Explanation

A **list** is an ordered, mutable (changeable) collection of items. Lists can contain any data type and are defined with square brackets `[]`.

**Key Features:**
- Ordered (maintains insertion order)
- Mutable (can be changed)
- Allows duplicates
- Can contain mixed data types

**Common Operations:**
- `append()` - Add item to end
- `insert()` - Add item at position
- `remove()` - Remove specific item
- `pop()` - Remove and return item
- `len()` - Get length
- `sort()` - Sort the list
- Indexing: `list[0]` (first item), `list[-1]` (last item)
- Slicing: `list[1:3]` (items 1 and 2)

### DevOps Use Case

Lists are **everywhere** in DevOps:
- Server lists and hostnames
- Log file entries
- Command output lines
- IP addresses
- Port numbers
- Deployment steps
- Error messages

### Code Example

```python
# Creating lists
servers = ["web-01", "web-02", "web-03"]
ports = [80, 443, 8080, 3306]
mixed = ["server", 8080, True, 3.14]

# Accessing items (0-indexed)
print(servers[0])  # web-01 (first)
print(servers[-1])  # web-03 (last)
print(servers[1:3])  # ['web-02', 'web-03'] (slice)

# Adding items
servers.append("web-04")  # Add to end
servers.insert(0, "web-00")  # Insert at position 0

# Removing items
servers.remove("web-00")  # Remove specific item
last_server = servers.pop()  # Remove and return last item
del servers[0]  # Delete by index

# List operations
print(len(servers))  # Length
print("web-01" in servers)  # Check if exists
servers.sort()  # Sort in place
sorted_servers = sorted(servers)  # Return sorted copy

# Looping through lists
for server in servers:
    print(f"Checking {server}")

# List comprehension (advanced but useful)
# Create new list based on existing one
active_servers = [s for s in servers if "web" in s]
uppercase_servers = [s.upper() for s in servers]

# Real DevOps example: Processing server list
servers = ["web-01", "web-02", "db-01", "cache-01"]
web_servers = []

for server in servers:
    if server.startswith("web"):
        web_servers.append(server)

print(f"Web servers: {web_servers}")

# Joining list items into string
server_string = ", ".join(servers)
print(server_string)  # web-01, web-02, db-01, cache-01

# Splitting string into list
log_line = "ERROR|2024-01-30|Database connection failed"
parts = log_line.split("|")
print(parts)  # ['ERROR', '2024-01-30', 'Database connection failed']
```

### Common Mistakes

❌ **Mistake 1**: Index out of range
```python
servers = ["web-01", "web-02"]
print(servers[5])  # ERROR! IndexError
```

❌ **Mistake 2**: Modifying list while iterating
```python
servers = ["web-01", "web-02", "web-03"]
for server in servers:
    servers.remove(server)  # BAD! Can skip items
```

❌ **Mistake 3**: Confusing append vs extend
```python
servers = ["web-01"]
servers.append(["web-02", "web-03"])  # Adds list as single item
# Result: ["web-01", ["web-02", "web-03"]]

servers.extend(["web-02", "web-03"])  # Adds items individually
# Result: ["web-01", "web-02", "web-03"]
```

✅ **Fix**: Check length, use copy for iteration, use correct method
```python
if len(servers) > 5:
    print(servers[5])

for server in servers.copy():
    if condition:
        servers.remove(server)
```

---

## 2. Tuples

### Concept Explanation

A **tuple** is an ordered, **immutable** (unchangeable) collection. Tuples are defined with parentheses `()`.

**Key Features:**
- Ordered
- Immutable (cannot be changed after creation)
- Allows duplicates
- Faster than lists
- Can be used as dictionary keys

**When to use tuples:**
- Data that shouldn't change (coordinates, config values)
- Function return multiple values
- Dictionary keys
- Performance-critical code

### DevOps Use Case

Tuples are used for:
- Fixed configuration values (host, port)
- Coordinates (latitude, longitude)
- Database connection info
- Return multiple values from functions
- Immutable server configurations

### Code Example

```python
# Creating tuples
server_info = ("web-01", "192.168.1.10", 80)
coordinates = (37.7749, -122.4194)
single_item = ("item",)  # Note the comma!

# Accessing items (same as lists)
hostname = server_info[0]
ip = server_info[1]
port = server_info[2]

# Unpacking tuples
hostname, ip, port = server_info
print(f"Server: {hostname} at {ip}:{port}")

# Tuples are immutable
# server_info[0] = "web-02"  # ERROR! Can't modify

# Tuple methods (only 2!)
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))  # Count occurrences: 3
print(numbers.index(3))  # Find index of first occurrence: 3

# Real DevOps example: Database connections
db_connections = [
    ("postgres", "db-01.example.com", 5432),
    ("mysql", "db-02.example.com", 3306),
    ("redis", "cache-01.example.com", 6379)
]

for db_type, host, port in db_connections:
    print(f"Connecting to {db_type} at {host}:{port}")

# Function returning tuple
def get_server_status(server):
    return ("web-01", "healthy", 45)  # name, status, cpu

name, status, cpu = get_server_status("web-01")
print(f"{name} is {status} with {cpu}% CPU")
```

### Common Mistakes

❌ **Mistake 1**: Trying to modify tuple
```python
server = ("web-01", 80)
server[1] = 443  # ERROR! Tuples are immutable
```

❌ **Mistake 2**: Forgetting comma for single-item tuple
```python
not_a_tuple = ("item")  # This is just a string!
is_a_tuple = ("item",)  # This is a tuple
```

✅ **Fix**: Use lists if you need to modify, remember comma
```python
server = ["web-01", 80]  # Use list if you need to change
server[1] = 443  # Now it works
```

---

## 3. Sets

### Concept Explanation

A **set** is an unordered collection of **unique** items. Sets are defined with curly braces `{}` or `set()`.

**Key Features:**
- Unordered (no indexing)
- No duplicates (automatically removes duplicates)
- Mutable (can add/remove items)
- Fast membership testing
- Mathematical set operations (union, intersection, difference)

### DevOps Use Case

Sets are perfect for:
- Removing duplicate IPs or hostnames
- Finding common servers between environments
- Checking if item exists (very fast)
- Comparing configurations
- Unique error types

### Code Example

```python
# Creating sets
servers = {"web-01", "web-02", "web-03"}
ports = {80, 443, 8080}
empty_set = set()  # Note: {} creates empty dict, not set!

# Adding and removing
servers.add("web-04")
servers.remove("web-01")  # Error if not exists
servers.discard("web-01")  # No error if not exists

# Set operations
prod_servers = {"web-01", "web-02", "db-01"}
staging_servers = {"web-02", "web-03", "db-01"}

# Union (all unique items from both)
all_servers = prod_servers | staging_servers
# or: all_servers = prod_servers.union(staging_servers)

# Intersection (common items)
common = prod_servers & staging_servers
# or: common = prod_servers.intersection(staging_servers)

# Difference (in first but not second)
prod_only = prod_servers - staging_servers
# or: prod_only = prod_servers.difference(staging_servers)

# Symmetric difference (in either but not both)
unique_to_each = prod_servers ^ staging_servers

# Membership testing (very fast!)
if "web-01" in prod_servers:
    print("web-01 is in production")

# Real DevOps example: Remove duplicate IPs
ip_list = ["10.0.1.1", "10.0.1.2", "10.0.1.1", "10.0.1.3", "10.0.1.2"]
unique_ips = list(set(ip_list))
print(f"Unique IPs: {unique_ips}")

# Find servers that need updates
current_servers = {"web-01", "web-02", "web-03", "db-01"}
updated_servers = {"web-01", "web-02"}
needs_update = current_servers - updated_servers
print(f"Servers needing updates: {needs_update}")
```

### Common Mistakes

❌ **Mistake 1**: Trying to index a set
```python
servers = {"web-01", "web-02"}
print(servers[0])  # ERROR! Sets are unordered, no indexing
```

❌ **Mistake 2**: Creating empty set wrong
```python
empty = {}  # This is a dict, not a set!
empty = set()  # Correct way
```

✅ **Fix**: Convert to list for indexing, use set() for empty
```python
servers = {"web-01", "web-02"}
server_list = list(servers)
print(server_list[0])  # Now works
```

---

## 4. Dictionaries

### Concept Explanation

A **dictionary** is an unordered collection of **key-value pairs**. Dictionaries are defined with curly braces `{}` and colons `:`.

**Key Features:**
- Key-value pairs
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any type
- Fast lookup by key
- Mutable

**Common Operations:**
- `dict[key]` - Get value (error if key doesn't exist)
- `dict.get(key, default)` - Get value (return default if not exists)
- `dict[key] = value` - Set value
- `dict.keys()` - Get all keys
- `dict.values()` - Get all values
- `dict.items()` - Get key-value pairs

### DevOps Use Case

Dictionaries are **critical** for DevOps:
- Configuration files (JSON, YAML)
- Server metadata
- API responses
- Environment variables
- Status mappings
- Resource inventories

### Code Example

```python
# Creating dictionaries
server = {
    "name": "web-01",
    "ip": "192.168.1.10",
    "port": 80,
    "status": "running"
}

# Accessing values
print(server["name"])  # web-01
print(server.get("port"))  # 80
print(server.get("region", "us-east"))  # us-east (default)

# Adding/updating values
server["cpu"] = 45
server["status"] = "healthy"

# Removing items
del server["cpu"]
port = server.pop("port")  # Remove and return value

# Dictionary methods
keys = server.keys()  # dict_keys(['name', 'ip', 'status'])
values = server.values()  # dict_values(['web-01', '192.168.1.10', 'healthy'])
items = server.items()  # dict_items([('name', 'web-01'), ...])

# Checking if key exists
if "name" in server:
    print(f"Server name: {server['name']}")

# Looping through dictionaries
for key in server:
    print(f"{key}: {server[key]}")

for key, value in server.items():
    print(f"{key}: {value}")

# Nested dictionaries (very common in DevOps!)
infrastructure = {
    "web_servers": {
        "web-01": {"ip": "10.0.1.10", "cpu": 45},
        "web-02": {"ip": "10.0.1.11", "cpu": 67}
    },
    "databases": {
        "db-01": {"ip": "10.0.2.10", "cpu": 78}
    }
}

# Accessing nested values
web01_cpu = infrastructure["web_servers"]["web-01"]["cpu"]
print(f"web-01 CPU: {web01_cpu}%")

# Real DevOps example: Server inventory
servers = {
    "web-01": {
        "ip": "10.0.1.10",
        "port": 80,
        "status": "running",
        "cpu": 45,
        "memory": 60
    },
    "web-02": {
        "ip": "10.0.1.11",
        "port": 80,
        "status": "running",
        "cpu": 78,
        "memory": 75
    },
    "db-01": {
        "ip": "10.0.2.10",
        "port": 5432,
        "status": "running",
        "cpu": 55,
        "memory": 80
    }
}

# Process inventory
for hostname, details in servers.items():
    cpu = details["cpu"]
    if cpu > 70:
        print(f"⚠ {hostname}: High CPU at {cpu}%")
    else:
        print(f"✓ {hostname}: CPU normal at {cpu}%")

# Dictionary comprehension
high_cpu_servers = {
    name: info["cpu"] 
    for name, info in servers.items() 
    if info["cpu"] > 70
}
print(f"High CPU servers: {high_cpu_servers}")
```

### Common Mistakes

❌ **Mistake 1**: KeyError when key doesn't exist
```python
server = {"name": "web-01"}
print(server["ip"])  # ERROR! KeyError: 'ip'
```

❌ **Mistake 2**: Using mutable objects as keys
```python
bad_dict = {["list"]: "value"}  # ERROR! Lists can't be keys
```

❌ **Mistake 3**: Modifying dict while iterating
```python
for key in server:
    del server[key]  # BAD! RuntimeError
```

✅ **Fix**: Use get(), use immutable keys, iterate over copy
```python
print(server.get("ip", "N/A"))  # Returns "N/A" if not exists

for key in list(server.keys()):
    del server[key]  # Now safe
```

---

## 5. When to Use What?

### Quick Reference

| Data Structure | When to Use | Example Use Case |
|----------------|-------------|------------------|
| **List** | Ordered collection, need to modify | Server list, log entries, deployment steps |
| **Tuple** | Fixed data, can't change | Config values, coordinates, function returns |
| **Set** | Unique items, fast lookup | Remove duplicates, membership testing |
| **Dictionary** | Key-value pairs, fast lookup by key | Server configs, JSON data, API responses |

### Decision Tree

```
Need key-value pairs? → Dictionary
Need unique items only? → Set
Data shouldn't change? → Tuple
Everything else → List (most common)
```

---

## 🎯 Mini Exercise 1: Server Management

**Task**: Create a list of servers and perform operations.

**Requirements:**
1. Create list: `["web-01", "web-02", "db-01"]`
2. Add "cache-01" to the end
3. Insert "lb-01" at the beginning
4. Remove "db-01"
5. Print all servers

---

## ✅ Solution 1

```python
servers = ["web-01", "web-02", "db-01"]
servers.append("cache-01")
servers.insert(0, "lb-01")
servers.remove("db-01")

print("Servers:")
for i, server in enumerate(servers, 1):
    print(f"{i}. {server}")
```

---

## 🎯 Mini Exercise 2: Server Configuration

**Task**: Create a dictionary for server configuration.

**Requirements:**
1. Create dict with: name, ip, port, status, cpu, memory
2. Update CPU to 85
3. Add new key "region" with value "us-east"
4. Print all key-value pairs

---

## ✅ Solution 2

```python
server = {
    "name": "web-01",
    "ip": "10.0.1.10",
    "port": 80,
    "status": "running",
    "cpu": 45,
    "memory": 60
}

server["cpu"] = 85
server["region"] = "us-east"

print("Server Configuration:")
for key, value in server.items():
    print(f"  {key}: {value}")
```

---

## 🎯 Mini Exercise 3: Remove Duplicate IPs

**Task**: Remove duplicate IP addresses from a list.

**Requirements:**
1. Given: `["10.0.1.1", "10.0.1.2", "10.0.1.1", "10.0.1.3"]`
2. Remove duplicates
3. Print unique IPs

---

## ✅ Solution 3

```python
ip_addresses = ["10.0.1.1", "10.0.1.2", "10.0.1.1", "10.0.1.3"]
unique_ips = list(set(ip_addresses))

print("Unique IP addresses:")
for ip in unique_ips:
    print(f"  {ip}")
```

---

## 📝 Key Takeaways

✅ **Lists** - Most common, ordered, mutable
✅ **Tuples** - Immutable, use for fixed data
✅ **Sets** - Unique items, fast membership testing
✅ **Dictionaries** - Key-value pairs, like JSON
✅ **Use `.get()` for dictionaries** - Avoid KeyError
✅ **List comprehensions** - Concise way to create lists
✅ **Choose the right structure** - Performance and clarity matter

---

## 🚀 Practice Challenge

Create a server inventory system:
1. Use a dictionary to store 3 servers
2. Each server has: name, ip, services (list), status
3. Loop through and print each server's details
4. Find all unique services across all servers (use set)
5. Count how many servers are "running"

---

## Next Module

Ready for **Module 4: Functions & Modules**? Learn to organize and reuse your code! 🎯
