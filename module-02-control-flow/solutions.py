# Module 2: Control Flow - Exercise Solutions

print("=" * 50)
print("MODULE 2 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: Server Status Checker
print("\nSolution 1: Server Status Checker")
print("-" * 50)

status = "running"

if status == "running":
    print("Server is healthy")
elif status == "stopped":
    print("Server is down")
elif status == "restarting":
    print("Server is restarting")
else:
    print("Unknown status")

# Solution 2: CPU Alert System
print("\nSolution 2: CPU Alert System")
print("-" * 50)

cpu_usage = 85

if cpu_usage < 60:
    alert = "Normal"
elif cpu_usage < 80:
    alert = "Monitor"
elif cpu_usage < 90:
    alert = "Warning"
else:
    alert = "Critical"

print(f"CPU Usage: {cpu_usage}% - Alert Level: {alert}")

# Solution 3: Loop Through Servers
print("\nSolution 3: Loop Through Servers")
print("-" * 50)

servers = ['web-01', 'web-02', 'web-03', 'db-01']

for index, server in enumerate(servers, start=1):
    print(f"{index}. {server}")

# Solution 4: Retry Mechanism
print("\nSolution 4: Retry Mechanism")
print("-" * 50)

max_attempts = 5
success = False

for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt}/{max_attempts}")
    
    if attempt == 3:
        success = True
        print("  ✓ Success!")
        break
    else:
        print("  ✗ Failed")

if not success:
    print("Failed after all attempts")

# Solution 5: Environment Deployment
print("\nSolution 5: Environment Deployment")
print("-" * 50)

environments = ['dev', 'staging', 'prod']
tests_passed = True

for env in environments:
    if env == 'prod' and not tests_passed:
        print(f"✗ Skipping {env} - tests failed")
        continue
    
    print(f"✓ Deploying to {env}")

# Solution 6: Port Scanner
print("\nSolution 6: Port Scanner")
print("-" * 50)

ports = [22, 80, 443, 3306, 8080]
open_ports = [22, 80, 443]

print("Port Scan Results:")
for port in ports:
    if port in open_ports:
        status = "OPEN"
    else:
        status = "CLOSED"
    print(f"  Port {port}: {status}")

# Solution 7: Health Check with Break
print("\nSolution 7: Health Check with Break")
print("-" * 50)

endpoints = ['api.example.com', 'web.example.com', 'db.example.com']
statuses = [200, 200, 500]

print("Checking endpoints:")
for i, endpoint in enumerate(endpoints):
    status = statuses[i]
    print(f"  {endpoint}: {status}")
    
    if status == 500:
        print(f"✗ Error detected at {endpoint}. Stopping checks.")
        break

# Solution 8: Skip Maintenance Servers
print("\nSolution 8: Skip Maintenance Servers")
print("-" * 50)

servers = [
    {'name': 'web-01', 'maintenance': False},
    {'name': 'web-02', 'maintenance': True},
    {'name': 'web-03', 'maintenance': False}
]

print("Processing servers:")
for server in servers:
    if server['maintenance']:
        print(f"  Skipping {server['name']} (maintenance mode)")
        continue
    
    print(f"  ✓ Processing {server['name']}")

# Solution 9: Nested Loop - Multi-Region Deployment
print("\nSolution 9: Nested Loop - Multi-Region Deployment")
print("-" * 50)

regions = ['us-east', 'us-west', 'eu-west']
environments = ['dev', 'prod']

print("Deployment Matrix:")
for env in environments:
    for region in regions:
        print(f"  Deploying to {env}-{region}")

# Solution 10: Advanced - Server Health Monitor
print("\nSolution 10: Advanced - Server Health Monitor")
print("-" * 50)

servers = [
    {'name': 'web-01', 'cpu': 45, 'memory': 60, 'disk': 70},
    {'name': 'web-02', 'cpu': 85, 'memory': 80, 'disk': 65},
    {'name': 'web-03', 'cpu': 95, 'memory': 90, 'disk': 85}
]

print("SERVER HEALTH REPORT")
print("=" * 60)

for server in servers:
    name = server['name']
    cpu = server['cpu']
    memory = server['memory']
    disk = server['disk']
    
    if cpu > 90 or memory > 90 or disk > 90:
        status = "CRITICAL"
        symbol = "✗"
    elif cpu > 80 or memory > 80 or disk > 80:
        status = "WARNING"
        symbol = "⚠"
    else:
        status = "OK"
        symbol = "✓"
    
    print(f"{symbol} {name}: CPU={cpu}% MEM={memory}% DISK={disk}% - {status}")

print("=" * 60)

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
