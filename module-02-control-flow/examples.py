# Module 2: Control Flow - Code Examples

print("=" * 50)
print("MODULE 2: CONTROL FLOW - EXAMPLES")
print("=" * 50)

# Example 1: Basic if-else
print("\n1. BASIC IF-ELSE")
print("-" * 50)
cpu_usage = 85

if cpu_usage > 80:
    print(f"⚠ WARNING: High CPU usage at {cpu_usage}%")
else:
    print(f"✓ CPU usage normal at {cpu_usage}%")

# Example 2: if-elif-else chain
print("\n2. HTTP STATUS CODE CHECKER")
print("-" * 50)
status_codes = [200, 404, 500, 301, 403]

for code in status_codes:
    if code == 200:
        message = "Success"
    elif code == 301:
        message = "Redirect"
    elif code == 404:
        message = "Not Found"
    elif code == 403:
        message = "Forbidden"
    elif code == 500:
        message = "Server Error"
    else:
        message = "Unknown Status"
    
    print(f"Status {code}: {message}")

# Example 3: Multiple conditions
print("\n3. RESOURCE MONITORING")
print("-" * 50)
servers = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 85, "memory": 75},
    {"name": "web-03", "cpu": 90, "memory": 95},
]

for server in servers:
    name = server["name"]
    cpu = server["cpu"]
    memory = server["memory"]
    
    if cpu > 90 and memory > 90:
        status = "CRITICAL"
    elif cpu > 80 or memory > 80:
        status = "WARNING"
    else:
        status = "OK"
    
    print(f"{name}: CPU={cpu}%, MEM={memory}% - {status}")

# Example 4: For loop with range
print("\n4. COUNTDOWN TIMER")
print("-" * 50)
print("Deployment starting in...")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("🚀 Deploying now!")

# Example 5: For loop with enumerate
print("\n5. DEPLOYMENT SEQUENCE")
print("-" * 50)
environments = ["dev", "staging", "production"]

for index, env in enumerate(environments, start=1):
    print(f"Step {index}: Deploying to {env}")

# Example 6: While loop - Retry logic
print("\n6. RETRY LOGIC")
print("-" * 50)
max_retries = 3
attempt = 0
success = False

while attempt < max_retries and not success:
    attempt += 1
    print(f"Attempt {attempt}/{max_retries}...")
    
    if attempt == 2:
        success = True
        print("  ✓ Success!")
    else:
        print("  ✗ Failed, retrying...")

# Example 7: Break statement
print("\n7. BREAK - STOP ON ERROR")
print("-" * 50)
servers = ["web-01", "web-02", "web-03", "web-04"]
statuses = ["healthy", "healthy", "down", "healthy"]

for i, server in enumerate(servers):
    status = statuses[i]
    print(f"Checking {server}: {status}")
    
    if status == "down":
        print(f"✗ ERROR: {server} is down! Stopping checks.")
        break

# Example 8: Continue statement
print("\n8. CONTINUE - SKIP ITEMS")
print("-" * 50)
servers = [
    {"name": "web-prod-01", "env": "production"},
    {"name": "web-dev-01", "env": "development"},
    {"name": "web-prod-02", "env": "production"},
    {"name": "web-test-01", "env": "testing"},
]

print("Processing production servers only:")
for server in servers:
    if server["env"] != "production":
        continue
    print(f"  ✓ Processing {server['name']}")

# Example 9: Nested loops
print("\n9. NESTED LOOPS - SERVICE CHECK")
print("-" * 50)
servers = ["web-01", "web-02"]
services = ["nginx", "app", "redis"]

for server in servers:
    print(f"\n{server}:")
    for service in services:
        print(f"  {service}: running")

# Example 10: Real DevOps scenario
print("\n10. DEPLOYMENT VALIDATION")
print("-" * 50)

deployment_config = {
    "environment": "production",
    "tests_passed": True,
    "approval": True,
    "version": "2.5.0"
}

env = deployment_config["environment"]
tests = deployment_config["tests_passed"]
approval = deployment_config["approval"]

print(f"Environment: {env}")
print(f"Tests Passed: {tests}")
print(f"Approval: {approval}")
print()

if env == "production":
    if not tests:
        print("✗ Cannot deploy: Tests failed")
    elif not approval:
        print("✗ Cannot deploy: No approval")
    else:
        print("✓ All checks passed - Deploying to production")
else:
    print(f"✓ Deploying to {env} (no approval needed)")

# Example 11: Finding available port
print("\n11. FIND AVAILABLE PORT")
print("-" * 50)
ports = [8080, 8081, 8082, 8083, 8084]
used_ports = [8080, 8081, 8082]

available_port = None
for port in ports:
    if port in used_ports:
        continue
    available_port = port
    print(f"✓ Found available port: {port}")
    break

if not available_port:
    print("✗ No available ports found")

# Example 12: Loop with else clause
print("\n12. LOOP WITH ELSE")
print("-" * 50)
print("Searching for healthy server...")
servers = ["web-01", "web-02", "web-03"]
statuses = ["down", "down", "down"]

for i, server in enumerate(servers):
    print(f"  Checking {server}...")
    if statuses[i] == "healthy":
        print(f"  ✓ Found healthy server: {server}")
        break
else:
    print("  ✗ No healthy servers found!")

print("\n" + "=" * 50)
print("END OF MODULE 2 EXAMPLES")
print("=" * 50)
