# Module 4: Functions & Modules - Exercise Solutions

print("=" * 50)
print("MODULE 4 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: Basic Function
print("\nSolution 1: Basic Function")
print("-" * 50)

def ping_server(server_name):
    print(f"Pinging {server_name}...")
    return True

result = ping_server("web-01")
print(f"Result: {result}")

# Solution 2: Function with Return Value
print("\nSolution 2: Function with Return Value")
print("-" * 50)

def check_disk_space(disk_usage):
    if disk_usage < 80:
        return "OK"
    elif disk_usage <= 90:
        return "WARNING"
    else:
        return "CRITICAL"

print(check_disk_space(75))
print(check_disk_space(85))
print(check_disk_space(95))

# Solution 3: Multiple Parameters
print("\nSolution 3: Multiple Parameters")
print("-" * 50)

def check_server(server_name, cpu, memory):
    return f"{server_name}: CPU={cpu}%, Memory={memory}%"

print(check_server("web-01", 75, 60))
print(check_server("web-02", 85, 80))

# Solution 4: Default Arguments
print("\nSolution 4: Default Arguments")
print("-" * 50)

def deploy(environment, version, rollback=True, notify=True):
    print(f"Deploying {version} to {environment}")
    print(f"  Rollback: {rollback}")
    print(f"  Notify: {notify}")

deploy("prod", "2.0.0")
deploy("staging", "2.1.0", rollback=False)
deploy("dev", "2.2.0", notify=False, rollback=False)

# Solution 5: Multiple Return Values
print("\nSolution 5: Multiple Return Values")
print("-" * 50)

def get_metrics(server_name):
    cpu = 75
    memory = 60
    disk = 80
    return cpu, memory, disk

cpu, memory, disk = get_metrics("web-01")
print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

# Solution 6: Lambda Function
print("\nSolution 6: Lambda Function")
print("-" * 50)

servers = [
    {'name': 'web-01', 'cpu': 75},
    {'name': 'web-02', 'cpu': 45},
    {'name': 'web-03', 'cpu': 90}
]

sorted_servers = sorted(servers, key=lambda s: s['cpu'])
print("Sorted by CPU:")
for s in sorted_servers:
    print(f"  {s['name']}: {s['cpu']}%")

# Solution 7: Filter with Lambda
print("\nSolution 7: Filter with Lambda")
print("-" * 50)

high_cpu = list(filter(lambda s: s['cpu'] > 70, servers))
print("Servers with CPU > 70:")
for s in high_cpu:
    print(f"  {s['name']}: {s['cpu']}%")

# Solution 8: Variable Arguments
print("\nSolution 8: Variable Arguments")
print("-" * 50)

def check_ports(*ports):
    for port in ports:
        print(f"Checking port {port}")

check_ports(80, 443, 8080)
check_ports(22)

# Solution 9: Keyword Arguments
print("\nSolution 9: Keyword Arguments")
print("-" * 50)

def create_vm(**config):
    print("Creating VM with config:")
    for key, value in config.items():
        print(f"  {key}: {value}")

create_vm(name='vm-01', cpu=4, memory=8)
create_vm(name='vm-02', cpu=8, memory=16, disk=500)

# Solution 10: Advanced - Validation Function
print("\nSolution 10: Advanced - Validation Function")
print("-" * 50)

def validate_config(environment, version, tests_passed, approval):
    if environment == "production":
        if not tests_passed:
            return (False, "Tests failed")
        if not approval:
            return (False, "No approval")
    
    return (True, "Validation passed")

can_deploy, msg = validate_config("prod", "2.0.0", True, True)
print(f"Production with all checks: {can_deploy} - {msg}")

can_deploy, msg = validate_config("prod", "2.0.0", False, True)
print(f"Production without tests: {can_deploy} - {msg}")

can_deploy, msg = validate_config("dev", "2.0.0", False, False)
print(f"Development: {can_deploy} - {msg}")

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
