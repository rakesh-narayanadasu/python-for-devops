# Module 4: Functions & Modules - Code Examples

print("=" * 50)
print("MODULE 4: FUNCTIONS & MODULES - EXAMPLES")
print("=" * 50)

# Example 1: Basic Function
print("\n1. BASIC FUNCTION")
print("-" * 50)

def check_server_status(server_name):
    print(f"Checking {server_name}...")
    return "healthy"

status = check_server_status("web-01")
print(f"Status: {status}")

# Example 2: Function with Multiple Parameters
print("\n2. FUNCTION WITH PARAMETERS")
print("-" * 50)

def check_cpu(server, cpu_usage):
    if cpu_usage > 80:
        return f"⚠ {server}: HIGH CPU - {cpu_usage}%"
    else:
        return f"✓ {server}: Normal - {cpu_usage}%"

print(check_cpu("web-01", 45))
print(check_cpu("web-02", 85))

# Example 3: Multiple Return Values
print("\n3. MULTIPLE RETURN VALUES")
print("-" * 50)

def get_server_metrics(server):
    cpu = 75
    memory = 60
    disk = 80
    return cpu, memory, disk

cpu, mem, disk = get_server_metrics("web-01")
print(f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")

# Example 4: Default Arguments
print("\n4. DEFAULT ARGUMENTS")
print("-" * 50)

def connect_server(host, port=22, timeout=30):
    print(f"Connecting to {host}:{port} (timeout: {timeout}s)")
    return True

connect_server("10.0.1.10")
connect_server("10.0.1.10", 8080)
connect_server("10.0.1.10", 8080, 60)

# Example 5: Keyword Arguments
print("\n5. KEYWORD ARGUMENTS")
print("-" * 50)

def deploy(env, version, rollback=True, notify=True):
    print(f"Deploying {version} to {env}")
    print(f"  Rollback: {rollback}, Notify: {notify}")

deploy("prod", "2.0.0")
deploy("staging", "2.1.0", notify=False)
deploy(version="2.2.0", env="dev", rollback=False)

# Example 6: *args - Variable Arguments
print("\n6. VARIABLE ARGUMENTS (*args)")
print("-" * 50)

def check_multiple_servers(*servers):
    print(f"Checking {len(servers)} servers:")
    for server in servers:
        print(f"  ✓ {server}")

check_multiple_servers("web-01")
check_multiple_servers("web-01", "web-02", "web-03")

# Example 7: **kwargs - Keyword Arguments
print("\n7. KEYWORD ARGUMENTS (**kwargs)")
print("-" * 50)

def create_server(**config):
    print("Creating server with config:")
    for key, value in config.items():
        print(f"  {key}: {value}")

create_server(name="web-01", cpu=4, memory=8, disk=100)
create_server(name="db-01", cpu=8, memory=16)

# Example 8: Lambda Functions
print("\n8. LAMBDA FUNCTIONS")
print("-" * 50)

servers = [
    {"name": "web-01", "cpu": 75},
    {"name": "web-02", "cpu": 45},
    {"name": "web-03", "cpu": 90}
]

sorted_by_cpu = sorted(servers, key=lambda s: s["cpu"])
print("Sorted by CPU:")
for s in sorted_by_cpu:
    print(f"  {s['name']}: {s['cpu']}%")

high_cpu = list(filter(lambda s: s["cpu"] > 70, servers))
print(f"\nHigh CPU servers: {[s['name'] for s in high_cpu]}")

# Example 9: Lambda with Map
print("\n9. LAMBDA WITH MAP")
print("-" * 50)

ports = [8080, 8081, 8082]
urls = list(map(lambda p: f"http://localhost:{p}", ports))
print("Generated URLs:")
for url in urls:
    print(f"  {url}")

# Example 10: Built-in Modules
print("\n10. BUILT-IN MODULES")
print("-" * 50)

import os
import json
from datetime import datetime

print(f"Current directory: {os.getcwd()}")

config = {"host": "localhost", "port": 8080}
json_str = json.dumps(config)
print(f"JSON: {json_str}")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Timestamp: {timestamp}")

# Example 11: Real DevOps Function
print("\n11. REAL DEVOPS FUNCTION")
print("-" * 50)

def validate_deployment(env, version, tests_passed, approval):
    """Validate if deployment can proceed"""
    if env == "production":
        if not tests_passed:
            return False, "Tests failed"
        if not approval:
            return False, "No approval"
    
    return True, "Validation passed"

can_deploy, message = validate_deployment("prod", "2.0.0", True, True)
print(f"Can deploy: {can_deploy} - {message}")

can_deploy, message = validate_deployment("prod", "2.0.0", False, True)
print(f"Can deploy: {can_deploy} - {message}")

# Example 12: Function with Docstring
print("\n12. FUNCTION WITH DOCSTRING")
print("-" * 50)

def calculate_uptime_percentage(total_hours, downtime_hours):
    """
    Calculate uptime percentage.
    
    Args:
        total_hours (float): Total hours in period
        downtime_hours (float): Hours of downtime
    
    Returns:
        float: Uptime percentage
    """
    uptime_hours = total_hours - downtime_hours
    percentage = (uptime_hours / total_hours) * 100
    return round(percentage, 2)

uptime = calculate_uptime_percentage(720, 2)
print(f"Uptime: {uptime}%")

print(f"\nFunction docstring:")
print(calculate_uptime_percentage.__doc__)

print("\n" + "=" * 50)
print("END OF MODULE 4 EXAMPLES")
print("=" * 50)
