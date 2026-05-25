# Module 3: Data Structures - Code Examples

print("=" * 50)
print("MODULE 3: DATA STRUCTURES - EXAMPLES")
print("=" * 50)

# Example 1: Lists - Server Management
print("\n1. LISTS - SERVER MANAGEMENT")
print("-" * 50)
servers = ["web-01", "web-02", "web-03"]
print(f"Servers: {servers}")

servers.append("web-04")
print(f"After append: {servers}")

servers.insert(0, "lb-01")
print(f"After insert: {servers}")

servers.remove("web-02")
print(f"After remove: {servers}")

last = servers.pop()
print(f"Popped: {last}, Remaining: {servers}")

# Example 2: List Slicing and Indexing
print("\n2. LIST SLICING")
print("-" * 50)
servers = ["web-01", "web-02", "web-03", "db-01", "cache-01"]
print(f"All servers: {servers}")
print(f"First server: {servers[0]}")
print(f"Last server: {servers[-1]}")
print(f"First 3: {servers[:3]}")
print(f"Last 2: {servers[-2:]}")
print(f"Middle: {servers[1:4]}")

# Example 3: List Comprehension
print("\n3. LIST COMPREHENSION")
print("-" * 50)
servers = ["web-01", "web-02", "db-01", "cache-01"]

web_servers = [s for s in servers if s.startswith("web")]
print(f"Web servers: {web_servers}")

uppercase = [s.upper() for s in servers]
print(f"Uppercase: {uppercase}")

ports = [8080, 8081, 8082]
urls = [f"http://localhost:{port}" for port in ports]
print(f"URLs: {urls}")

# Example 4: Tuples - Fixed Configuration
print("\n4. TUPLES - FIXED CONFIGURATION")
print("-" * 50)
db_config = ("postgres", "db.example.com", 5432, "production")
db_type, host, port, env = db_config
print(f"Database: {db_type} at {host}:{port} ({env})")

connections = [
    ("mysql", "db-01.local", 3306),
    ("redis", "cache-01.local", 6379),
    ("postgres", "db-02.local", 5432)
]

for db, host, port in connections:
    print(f"  {db}: {host}:{port}")

# Example 5: Sets - Unique Items
print("\n5. SETS - UNIQUE ITEMS")
print("-" * 50)
ip_list = ["10.0.1.1", "10.0.1.2", "10.0.1.1", "10.0.1.3", "10.0.1.2"]
unique_ips = set(ip_list)
print(f"Original: {ip_list}")
print(f"Unique: {unique_ips}")

# Example 6: Set Operations
print("\n6. SET OPERATIONS")
print("-" * 50)
prod_servers = {"web-01", "web-02", "db-01", "cache-01"}
staging_servers = {"web-02", "web-03", "db-01"}

print(f"Production: {prod_servers}")
print(f"Staging: {staging_servers}")
print(f"Union (all): {prod_servers | staging_servers}")
print(f"Intersection (common): {prod_servers & staging_servers}")
print(f"Difference (prod only): {prod_servers - staging_servers}")
print(f"Symmetric diff: {prod_servers ^ staging_servers}")

# Example 7: Dictionaries - Server Info
print("\n7. DICTIONARIES - SERVER INFO")
print("-" * 50)
server = {
    "name": "web-01",
    "ip": "10.0.1.10",
    "port": 80,
    "status": "running",
    "cpu": 45,
    "memory": 60
}

print(f"Server name: {server['name']}")
print(f"CPU usage: {server['cpu']}%")
print(f"Region: {server.get('region', 'us-east')}")

server["region"] = "us-west"
server["cpu"] = 78

print("\nAll server details:")
for key, value in server.items():
    print(f"  {key}: {value}")

# Example 8: Nested Dictionaries
print("\n8. NESTED DICTIONARIES")
print("-" * 50)
infrastructure = {
    "web": {
        "web-01": {"ip": "10.0.1.10", "cpu": 45},
        "web-02": {"ip": "10.0.1.11", "cpu": 67}
    },
    "database": {
        "db-01": {"ip": "10.0.2.10", "cpu": 55}
    }
}

for tier, servers in infrastructure.items():
    print(f"\n{tier.upper()} Tier:")
    for name, details in servers.items():
        print(f"  {name}: {details['ip']} (CPU: {details['cpu']}%)")

# Example 9: Real DevOps - Server Inventory
print("\n9. REAL DEVOPS - SERVER INVENTORY")
print("-" * 50)
inventory = {
    "web-01": {
        "ip": "10.0.1.10",
        "services": ["nginx", "app"],
        "status": "running",
        "cpu": 45
    },
    "web-02": {
        "ip": "10.0.1.11",
        "services": ["nginx", "app"],
        "status": "running",
        "cpu": 78
    },
    "db-01": {
        "ip": "10.0.2.10",
        "services": ["postgres"],
        "status": "running",
        "cpu": 55
    }
}

print("SERVER HEALTH CHECK")
print("=" * 50)
for hostname, details in inventory.items():
    cpu = details["cpu"]
    status = "⚠ WARNING" if cpu > 70 else "✓ OK"
    print(f"{status} {hostname}: CPU {cpu}%")

all_services = set()
for server in inventory.values():
    all_services.update(server["services"])
print(f"\nUnique services: {all_services}")

# Example 10: Dictionary Comprehension
print("\n10. DICTIONARY COMPREHENSION")
print("-" * 50)
servers = ["web-01", "web-02", "web-03"]
server_status = {server: "running" for server in servers}
print(f"Server status: {server_status}")

cpu_values = {"web-01": 45, "web-02": 78, "web-03": 92}
high_cpu = {name: cpu for name, cpu in cpu_values.items() if cpu > 70}
print(f"High CPU servers: {high_cpu}")

# Example 11: Combining Data Structures
print("\n11. COMBINING DATA STRUCTURES")
print("-" * 50)
deployment_plan = {
    "environments": ["dev", "staging", "prod"],
    "regions": {"us-east", "us-west", "eu-west"},
    "config": {
        "timeout": 30,
        "retries": 3,
        "parallel": True
    },
    "servers": [
        ("web-01", "10.0.1.10"),
        ("web-02", "10.0.1.11")
    ]
}

print("Deployment Plan:")
print(f"  Environments: {', '.join(deployment_plan['environments'])}")
print(f"  Regions: {', '.join(deployment_plan['regions'])}")
print(f"  Timeout: {deployment_plan['config']['timeout']}s")
print(f"  Servers: {len(deployment_plan['servers'])}")

print("\n" + "=" * 50)
print("END OF MODULE 3 EXAMPLES")
print("=" * 50)
