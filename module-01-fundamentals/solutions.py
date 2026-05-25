# Module 1: Python Fundamentals - Exercise Solutions

print("=" * 50)
print("MODULE 1 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: Server Configuration
print("\nSolution 1: Server Configuration")
print("-" * 50)

server_name = "web-prod-01"
ip_address = "192.168.1.100"
port = 443
is_active = True
cpu_usage = 67.8

print("SERVER CONFIGURATION")
print("=" * 40)
print(f"Server Name: {server_name}")
print(f"IP Address: {ip_address}")
print(f"Port: {port}")
print(f"Status: {'Active' if is_active else 'Inactive'}")
print(f"CPU Usage: {cpu_usage}%")
print("=" * 40)

# Solution 2: Type Conversion
print("\nSolution 2: Type Conversion")
print("-" * 50)

port = "8080"
max_connections = "100"
timeout = "30.5"

# Convert to proper types
port_int = int(port)
max_connections_int = int(max_connections)
timeout_float = float(timeout)

# Calculate total capacity
total_capacity = max_connections_int * 2
print(f"Total capacity: {total_capacity}")

# Create message using f-strings
message = f"Server on port {port} timeout {timeout}s"
print(message)

# Check if port is 80
if port_int == 80:
    print("Standard HTTP port")
else:
    print(f"Custom port: {port_int}")

# Solution 3: Multiple Servers
print("\nSolution 3: Multiple Servers")
print("-" * 50)

# Server 1
server1_name = "web-01"
server1_ip = "10.0.1.10"
server1_port = 80
server1_active = True

# Server 2
server2_name = "web-02"
server2_ip = "10.0.1.11"
server2_port = 80
server2_active = True

# Server 3
server3_name = "web-03"
server3_ip = "10.0.1.12"
server3_port = 80
server3_active = False

# Count active servers
active_count = 0
if server1_active:
    active_count += 1
if server2_active:
    active_count += 1
if server3_active:
    active_count += 1

print(f"Total active servers: {active_count}")
print()

# Print report for each server
print(f"Server: {server1_name} | IP: {server1_ip} | Port: {server1_port} | Active: {server1_active}")
print(f"Server: {server2_name} | IP: {server2_ip} | Port: {server2_port} | Active: {server2_active}")
print(f"Server: {server3_name} | IP: {server3_ip} | Port: {server3_port} | Active: {server3_active}")

# Solution 4: Configuration Parser
print("\nSolution 4: Configuration Parser")
print("-" * 50)

# Values from config file (as strings)
db_port = "5432"
max_connections = "200"
timeout = "30.0"
enable_ssl = "True"

# Convert to appropriate types
db_port_int = int(db_port)
max_connections_int = int(max_connections)
timeout_float = float(timeout)
enable_ssl_bool = enable_ssl == "True"  # String to boolean

# Calculations
new_port = db_port_int + 1000
half_connections = max_connections_int / 2
timeout_ms = timeout_float * 1000

print(f"Original port: {db_port_int}")
print(f"New port: {new_port}")
print(f"Half connections: {int(half_connections)}")
print(f"Timeout in milliseconds: {timeout_ms}")
print(f"SSL Enabled: {enable_ssl_bool}")

# Solution 5: DevOps Monitoring
print("\nSolution 5: DevOps Monitoring")
print("-" * 50)

# Monitoring variables
app_name = "payment-api"
version = 2.5
num_instances = 5
avg_response_time = 0.234
is_production = True

# Formatted monitoring report
print("""
╔════════════════════════════════════════╗
║       MONITORING REPORT                ║
╚════════════════════════════════════════╝
""")
print(f"Application: {app_name}")
print(f"Version: {version}")
print(f"Instances: {num_instances}")
print(f"Avg Response Time: {avg_response_time}s")
print(f"Environment: {'Production' if is_production else 'Development'}")
print()

# Additional calculations
total_capacity = num_instances * 100  # Assuming 100 req/s per instance
print(f"Total Capacity: {total_capacity} requests/second")

# Status indicator
if avg_response_time < 0.5:
    status = "Excellent"
elif avg_response_time < 1.0:
    status = "Good"
else:
    status = "Needs Attention"

print(f"Performance Status: {status}")

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
