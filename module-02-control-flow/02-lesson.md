# Module 2: Control Flow

## 📖 What You'll Learn
- Conditional statements (if, elif, else)
- Loops (for and while)
- Loop control (break, continue, pass)
- Real DevOps automation examples

---

## 1. Conditional Statements (if, elif, else)

### Concept Explanation

**Conditional statements** let your code make decisions based on conditions. Think of it as "if this is true, do that."

**Syntax:**
```python
if condition:
    # code runs if condition is True
elif another_condition:
    # code runs if first is False and this is True
else:
    # code runs if all above are False
```

**Comparison Operators:**
- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

**Logical Operators:**
- `and` - both conditions must be True
- `or` - at least one condition must be True
- `not` - reverses the condition

### DevOps Use Case

Conditional logic is everywhere in DevOps:
- Check if a server is healthy before deploying
- Route traffic based on environment (prod/dev)
- Alert only if CPU usage exceeds threshold
- Decide backup strategy based on day of week
- Validate configuration before applying

### Code Example

```python
# Example 1: Simple if statement
server_status = "running"

if server_status == "running":
    print("Server is healthy")

# Example 2: if-else
cpu_usage = 85

if cpu_usage > 80:
    print("WARNING: High CPU usage!")
else:
    print("CPU usage is normal")

# Example 3: if-elif-else
http_status = 200

if http_status == 200:
    print("Success")
elif http_status == 404:
    print("Not Found")
elif http_status == 500:
    print("Server Error")
else:
    print(f"Unknown status: {http_status}")

# Example 4: Multiple conditions with 'and'
memory_usage = 75
disk_usage = 60

if memory_usage > 80 and disk_usage > 80:
    print("CRITICAL: Both memory and disk high!")
elif memory_usage > 80 or disk_usage > 80:
    print("WARNING: Resource usage high")
else:
    print("System resources OK")

# Example 5: Real DevOps scenario - Deployment check
environment = "production"
tests_passed = True
approval_received = True

if environment == "production":
    if tests_passed and approval_received:
        print("✓ Deploying to production")
    else:
        print("✗ Cannot deploy - missing requirements")
else:
    print("✓ Deploying to dev/staging")
```

### Common Mistakes

❌ **Mistake 1**: Using `=` instead of `==`
```python
if cpu_usage = 80:  # ERROR! This is assignment, not comparison
    print("High CPU")
```

❌ **Mistake 2**: Forgetting the colon
```python
if cpu_usage > 80  # ERROR! Missing colon
    print("High CPU")
```

❌ **Mistake 3**: Wrong indentation
```python
if cpu_usage > 80:
print("High CPU")  # ERROR! Not indented
```

✅ **Fix**: Use `==`, add colon, proper indentation
```python
if cpu_usage == 80:
    print("CPU at 80%")
```

---

## 2. For Loops

### Concept Explanation

A **for loop** repeats code for each item in a sequence (list, string, range, etc.).

**Syntax:**
```python
for item in sequence:
    # code to repeat
```

**Common patterns:**
- `range(5)` - numbers 0 to 4
- `range(1, 6)` - numbers 1 to 5
- `range(0, 10, 2)` - 0, 2, 4, 6, 8 (step by 2)

### DevOps Use Case

For loops are essential for:
- Iterating through server lists
- Processing multiple log files
- Checking health of multiple endpoints
- Deploying to multiple environments
- Running commands on multiple hosts

### Code Example

```python
# Example 1: Loop through a list of servers
servers = ["web-01", "web-02", "web-03"]

for server in servers:
    print(f"Checking {server}...")

# Example 2: Using range
print("Starting deployment in...")
for i in range(5, 0, -1):
    print(i)
print("Deploy!")

# Example 3: Loop with index using enumerate
servers = ["web-01", "web-02", "web-03"]

for index, server in enumerate(servers, start=1):
    print(f"{index}. Deploying to {server}")

# Example 4: Real DevOps scenario - Health check
endpoints = [
    "https://api.example.com/health",
    "https://web.example.com/health",
    "https://db.example.com/health"
]

for endpoint in endpoints:
    print(f"Checking {endpoint}...")
    # In real scenario, you'd make HTTP request here
    status = 200  # Simulated
    if status == 200:
        print(f"  ✓ {endpoint} is healthy")
    else:
        print(f"  ✗ {endpoint} is down!")

# Example 5: Loop through dictionary (we'll learn more in Module 3)
server_ports = {
    "web": 80,
    "api": 8080,
    "db": 5432
}

for service, port in server_ports.items():
    print(f"{service} service runs on port {port}")
```

### Common Mistakes

❌ **Mistake 1**: Modifying list while looping
```python
servers = ["web-01", "web-02", "web-03"]
for server in servers:
    servers.remove(server)  # BAD! Can cause issues
```

❌ **Mistake 2**: Using wrong variable name
```python
for server in servers:
    print(servers)  # Should be 'server', not 'servers'
```

✅ **Fix**: Use correct variable, don't modify during iteration
```python
for server in servers:
    print(server)  # Correct
```

---

## 3. While Loops

### Concept Explanation

A **while loop** repeats code as long as a condition is True. Use it when you don't know how many iterations you need.

**Syntax:**
```python
while condition:
    # code to repeat
    # make sure condition eventually becomes False!
```

⚠️ **Warning**: Always ensure the loop can end, or you'll have an infinite loop!

### DevOps Use Case

While loops are useful for:
- Retrying failed operations
- Waiting for a service to start
- Polling for job completion
- Monitoring until threshold is met
- Connection retry logic

### Code Example

```python
# Example 1: Simple while loop
count = 0
while count < 3:
    print(f"Attempt {count + 1}")
    count += 1

# Example 2: Retry logic
max_retries = 3
attempt = 0
success = False

while attempt < max_retries and not success:
    attempt += 1
    print(f"Deployment attempt {attempt}...")
    
    # Simulated deployment
    deployment_status = "success"  # In reality, this would vary
    
    if deployment_status == "success":
        success = True
        print("✓ Deployment successful!")
    else:
        print(f"✗ Attempt {attempt} failed")

if not success:
    print("Deployment failed after all retries")

# Example 3: Waiting for service to be ready
import time

service_ready = False
timeout = 30
elapsed = 0

print("Waiting for service to start...")
while not service_ready and elapsed < timeout:
    # In real scenario, you'd check actual service status
    print(f"Checking... ({elapsed}s elapsed)")
    time.sleep(5)
    elapsed += 5
    
    # Simulated check
    if elapsed >= 10:
        service_ready = True

if service_ready:
    print("✓ Service is ready!")
else:
    print("✗ Service failed to start within timeout")

# Example 4: User input validation (for scripts)
# Note: This is just an example, won't work in automated scripts
"""
valid_input = False
while not valid_input:
    environment = input("Enter environment (dev/staging/prod): ")
    if environment in ["dev", "staging", "prod"]:
        valid_input = True
        print(f"Deploying to {environment}")
    else:
        print("Invalid environment. Try again.")
"""
```

### Common Mistakes

❌ **Mistake 1**: Infinite loop (condition never becomes False)
```python
count = 0
while count < 5:
    print(count)
    # Forgot to increment count! Infinite loop!
```

❌ **Mistake 2**: Off-by-one errors
```python
retries = 3
while retries > 0:
    print(f"Retry {retries}")
    # Forgot to decrement retries
```

✅ **Fix**: Always update the condition variable
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget this!
```

---

## 4. Loop Control (break, continue, pass)

### Concept Explanation

**Loop control statements** change how loops execute:

- **break**: Exit the loop immediately
- **continue**: Skip rest of current iteration, go to next
- **pass**: Do nothing (placeholder)

### DevOps Use Case

- **break**: Stop checking servers once you find a problem
- **continue**: Skip offline servers, check only online ones
- **pass**: Placeholder for future implementation

### Code Example

```python
# Example 1: break - Stop on first error
servers = ["web-01", "web-02", "web-03", "web-04"]
server_status = {
    "web-01": "healthy",
    "web-02": "healthy",
    "web-03": "down",
    "web-04": "healthy"
}

print("Checking servers...")
for server in servers:
    status = server_status.get(server, "unknown")
    print(f"  {server}: {status}")
    
    if status == "down":
        print(f"✗ Found problem with {server}. Stopping checks.")
        break

# Example 2: continue - Skip certain items
print("\nProcessing only production servers:")
servers = [
    {"name": "web-prod-01", "env": "production"},
    {"name": "web-dev-01", "env": "development"},
    {"name": "web-prod-02", "env": "production"},
    {"name": "web-staging-01", "env": "staging"}
]

for server in servers:
    if server["env"] != "production":
        continue  # Skip non-production servers
    
    print(f"Deploying to {server['name']}")

# Example 3: pass - Placeholder
print("\nChecking services:")
services = ["web", "api", "database", "cache"]

for service in services:
    if service == "cache":
        pass  # TODO: Implement cache check later
    else:
        print(f"Checking {service}...")

# Example 4: Real scenario - Find first available port
print("\nFinding available port:")
ports = [8080, 8081, 8082, 8083, 8084]
used_ports = [8080, 8081, 8082]

available_port = None
for port in ports:
    if port in used_ports:
        print(f"  Port {port} is in use")
        continue
    
    print(f"  Port {port} is available!")
    available_port = port
    break

if available_port:
    print(f"✓ Using port {available_port}")
else:
    print("✗ No available ports found")

# Example 5: Retry with break on success
print("\nRetrying connection:")
max_attempts = 5
for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt}...")
    
    # Simulated connection attempt
    connection_success = (attempt == 3)  # Succeeds on 3rd try
    
    if connection_success:
        print("✓ Connected successfully!")
        break
    else:
        print("  Connection failed, retrying...")
else:
    # This 'else' runs if loop completes without 'break'
    print("✗ Failed to connect after all attempts")
```

### Common Mistakes

❌ **Mistake 1**: Using break outside a loop
```python
if server_down:
    break  # ERROR! Not in a loop
```

❌ **Mistake 2**: Confusing break and continue
```python
for server in servers:
    if server == "skip-me":
        break  # This exits the entire loop!
    # Should use 'continue' to skip just this iteration
```

✅ **Fix**: Use in correct context
```python
for server in servers:
    if server == "skip-me":
        continue  # Skip this one, continue with others
    process_server(server)
```

---

## 5. Nested Loops

### Concept Explanation

**Nested loops** are loops inside loops. The inner loop completes all iterations for each iteration of the outer loop.

### DevOps Use Case

- Check multiple services on multiple servers
- Process multiple files in multiple directories
- Test multiple configurations across multiple environments

### Code Example

```python
# Example 1: Check services on multiple servers
servers = ["web-01", "web-02"]
services = ["nginx", "app", "database"]

print("Health Check Report:")
print("=" * 40)
for server in servers:
    print(f"\n{server}:")
    for service in services:
        # Simulated check
        status = "running"
        print(f"  {service}: {status}")

# Example 2: Deploy to multiple environments and regions
environments = ["dev", "staging", "prod"]
regions = ["us-east", "us-west"]

print("\nDeployment Matrix:")
for env in environments:
    for region in regions:
        print(f"Deploying to {env}-{region}")

# Example 3: Real scenario - Port scanning
print("\nPort Scan Results:")
hosts = ["192.168.1.10", "192.168.1.11"]
ports = [22, 80, 443]

for host in hosts:
    print(f"\nScanning {host}:")
    for port in ports:
        # Simulated port check
        is_open = port in [22, 80]  # Simulate some ports open
        status = "OPEN" if is_open else "CLOSED"
        print(f"  Port {port}: {status}")
```

---

## 🎯 Mini Exercise 1: Server Health Check

**Task**: Write a script that checks server CPU usage and prints appropriate messages.

**Requirements:**
1. Create a list of servers with CPU usage values
2. Loop through each server
3. Print "OK" if CPU < 70%, "WARNING" if 70-90%, "CRITICAL" if > 90%

**Try it yourself!**

---

## ✅ Solution 1

```python
# Server health check
servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 78},
    {"name": "web-03", "cpu": 92},
    {"name": "web-04", "cpu": 55}
]

print("SERVER HEALTH CHECK")
print("=" * 50)

for server in servers:
    name = server["name"]
    cpu = server["cpu"]
    
    if cpu < 70:
        status = "OK"
        symbol = "✓"
    elif cpu <= 90:
        status = "WARNING"
        symbol = "⚠"
    else:
        status = "CRITICAL"
        symbol = "✗"
    
    print(f"{symbol} {name}: CPU {cpu}% - {status}")
```

---

## 🎯 Mini Exercise 2: Deployment Retry Logic

**Task**: Implement retry logic for a deployment.

**Requirements:**
1. Maximum 3 retry attempts
2. Simulate deployment (use a counter to make it succeed on 2nd try)
3. Print attempt number and result
4. Break on success or print failure message after all attempts

---

## ✅ Solution 2

```python
# Deployment retry logic
max_retries = 3
attempt = 0
deployed = False

print("Starting deployment...")
print("-" * 40)

while attempt < max_retries and not deployed:
    attempt += 1
    print(f"\nAttempt {attempt}/{max_retries}...")
    
    # Simulate deployment (succeeds on attempt 2)
    if attempt == 2:
        deployed = True
        print("✓ Deployment successful!")
    else:
        print("✗ Deployment failed")
        if attempt < max_retries:
            print("  Retrying...")

if not deployed:
    print("\n✗ Deployment failed after all retries")
    print("  Please check logs and try again")
```

---

## 🎯 Mini Exercise 3: Multi-Environment Deployment

**Task**: Deploy to multiple environments with validation.

**Requirements:**
1. Environments: dev, staging, prod
2. For production, check if tests_passed = True
3. Skip deployment if validation fails
4. Print deployment status for each environment

---

## ✅ Solution 3

```python
# Multi-environment deployment
environments = ["dev", "staging", "prod"]
tests_passed = True
has_approval = True

print("DEPLOYMENT PIPELINE")
print("=" * 50)

for env in environments:
    print(f"\nDeploying to {env}...")
    
    # Production requires extra checks
    if env == "prod":
        if not tests_passed:
            print("  ✗ Skipped: Tests failed")
            continue
        if not has_approval:
            print("  ✗ Skipped: No approval")
            continue
    
    # Deploy
    print(f"  ✓ Successfully deployed to {env}")
    
    # Add delay between environments
    if env != "prod":
        print("  Waiting before next environment...")

print("\n" + "=" * 50)
print("Deployment pipeline completed!")
```

---

## 📝 Key Takeaways

✅ **Use if/elif/else** for decision making
✅ **Use for loops** when you know the sequence
✅ **Use while loops** for retry logic and polling
✅ **Use break** to exit loops early
✅ **Use continue** to skip iterations
✅ **Always avoid infinite loops** - ensure conditions can become False
✅ **Indent properly** - Python is strict about indentation

---

## 🚀 Practice Challenge

Create a script that:
1. Has a list of 5 servers with names, IPs, and status
2. Loops through and checks each server
3. If status is "down", try to restart (3 attempts max)
4. Print a final report of all servers and their status
5. Count how many servers are healthy vs down

---

## Next Module

Ready for **Module 3: Data Structures**? You'll learn about lists, dictionaries, and more! 🎯
