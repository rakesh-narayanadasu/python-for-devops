# Module 3: Data Structures - Exercise Solutions

print("=" * 50)
print("MODULE 3 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: List Operations
print("\nSolution 1: List Operations")
print("-" * 50)

servers = ['web-01', 'web-02', 'db-01']
servers.append('cache-01')
servers.insert(0, 'lb-01')
servers.remove('db-01')
print(f"Final list: {servers}")

# Solution 2: List Slicing
print("\nSolution 2: List Slicing")
print("-" * 50)

servers = ['web-01', 'web-02', 'web-03', 'db-01', 'cache-01']
first_three = servers[:3]
last_two = servers[-2:]
web_servers = servers[:3]

print(f"First 3: {first_three}")
print(f"Last 2: {last_two}")
print(f"Web servers: {web_servers}")

# Solution 3: Dictionary Creation
print("\nSolution 3: Dictionary Creation")
print("-" * 50)

server = {
    'name': 'web-01',
    'ip': '10.0.1.10',
    'port': 80,
    'status': 'running',
    'cpu': 45
}

print("Server details:")
for key, value in server.items():
    print(f"  {key}: {value}")

# Solution 4: Remove Duplicates
print("\nSolution 4: Remove Duplicates")
print("-" * 50)

ips = ['10.0.1.1', '10.0.1.2', '10.0.1.1', '10.0.1.3', '10.0.1.2']
unique_ips = list(set(ips))

print(f"Original: {ips}")
print(f"Unique: {unique_ips}")

# Solution 5: Nested Dictionary
print("\nSolution 5: Nested Dictionary")
print("-" * 50)

servers = {
    'web-01': {'ip': '10.0.1.10', 'cpu': 45, 'memory': 60},
    'web-02': {'ip': '10.0.1.11', 'cpu': 78, 'memory': 75}
}

print("Server Details:")
for name, details in servers.items():
    print(f"{name}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# Solution 6: Set Operations
print("\nSolution 6: Set Operations")
print("-" * 50)

prod_servers = {'web-01', 'web-02', 'db-01'}
staging_servers = {'web-02', 'web-03', 'db-01'}

common = prod_servers & staging_servers
prod_only = prod_servers - staging_servers

print(f"Common servers: {common}")
print(f"Production only: {prod_only}")

# Solution 7: List Comprehension
print("\nSolution 7: List Comprehension")
print("-" * 50)

servers = ['web-01', 'web-02', 'db-01', 'cache-01']
web_servers = [s for s in servers if s.startswith('web')]

print(f"Web servers: {web_servers}")

# Solution 8: Dictionary Update
print("\nSolution 8: Dictionary Update")
print("-" * 50)

server = {'name': 'web-01', 'cpu': 45, 'memory': 60}
server['cpu'] = 85
server['status'] = 'warning'
server['region'] = 'us-east'

print("Updated server:")
for key, value in server.items():
    print(f"  {key}: {value}")

# Solution 9: Tuple Unpacking
print("\nSolution 9: Tuple Unpacking")
print("-" * 50)

connections = [
    ('mysql', 'db-01.local', 3306),
    ('redis', 'cache-01.local', 6379),
    ('postgres', 'db-02.local', 5432)
]

print("Database connections:")
for db_type, host, port in connections:
    print(f"  {db_type} at {host}:{port}")

# Solution 10: Advanced - Server Inventory
print("\nSolution 10: Advanced - Server Inventory")
print("-" * 50)

inventory = {
    'web-01': {
        'ip': '10.0.1.10',
        'services': ['nginx', 'app'],
        'cpu': 45
    },
    'web-02': {
        'ip': '10.0.1.11',
        'services': ['nginx', 'app'],
        'cpu': 78
    },
    'db-01': {
        'ip': '10.0.2.10',
        'services': ['postgres', 'backup'],
        'cpu': 55
    }
}

print("Servers with CPU > 70:")
for name, details in inventory.items():
    if details['cpu'] > 70:
        print(f"  {name}: {details['cpu']}%")

all_services = set()
for server in inventory.values():
    all_services.update(server['services'])
print(f"\nUnique services: {all_services}")

print(f"\nTotal servers: {len(inventory)}")

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
