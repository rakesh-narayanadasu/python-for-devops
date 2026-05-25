# Module 1: Python Fundamentals - Code Examples
# Run this file to see all examples in action

print("=" * 50)
print("MODULE 1: PYTHON FUNDAMENTALS - EXAMPLES")
print("=" * 50)

# Example 1: Basic Variables
print("\n1. BASIC VARIABLES")
print("-" * 50)
server_name = "web-server-01"
server_port = 8080
is_active = True
cpu_usage = 75.5

print(f"Server: {server_name}")
print(f"Port: {server_port}")
print(f"Active: {is_active}")
print(f"CPU Usage: {cpu_usage}%")

# Example 2: Different Data Types
print("\n2. DATA TYPES IN DEVOPS")
print("-" * 50)
# Integers
http_status = 200
max_retries = 3
timeout_seconds = 30

# Floats
response_time = 0.245
memory_usage_gb = 4.5
uptime_hours = 168.5

# Strings
environment = "production"
region = "us-east-1"
log_level = "INFO"

# Booleans
ssl_enabled = True
backup_completed = False
maintenance_mode = False

print(f"HTTP Status: {http_status} (type: {type(http_status).__name__})")
print(f"Response Time: {response_time}s (type: {type(response_time).__name__})")
print(f"Environment: {environment} (type: {type(environment).__name__})")
print(f"SSL Enabled: {ssl_enabled} (type: {type(ssl_enabled).__name__})")

# Example 3: Type Conversion
print("\n3. TYPE CONVERSION")
print("-" * 50)
# Reading from config (usually strings)
port_from_config = "8080"
timeout_from_config = "30.5"
max_conn_from_config = "100"

# Convert to proper types
port = int(port_from_config)
timeout = float(timeout_from_config)
max_connections = int(max_conn_from_config)

print(f"Port (converted): {port} - Type: {type(port).__name__}")
print(f"Timeout (converted): {timeout} - Type: {type(timeout).__name__}")
print(f"Max Connections (converted): {max_connections} - Type: {type(max_connections).__name__}")

# Using converted values
new_port = port + 1
print(f"Next available port: {new_port}")

# Example 4: String Formatting
print("\n4. STRING FORMATTING (F-STRINGS)")
print("-" * 50)
server = "db-prod-01"
status = "healthy"
uptime = 99.99

# Old way (avoid)
message1 = "Server " + server + " is " + status
print("Old way:", message1)

# Modern way (use this!)
message2 = f"Server {server} is {status} with {uptime}% uptime"
print("Modern way:", message2)

# Example 5: Real DevOps Scenario
print("\n5. REAL DEVOPS SCENARIO")
print("-" * 50)
# Monitoring script variables
hostname = "api-gateway-prod"
ip_address = "10.0.1.50"
port = 443
protocol = "https"
health_check_interval = 60
last_response_time = 0.123
is_healthy = True
error_count = 0

# Generate monitoring report
print(f"""
MONITORING REPORT
-----------------
Hostname: {hostname}
IP: {ip_address}
Endpoint: {protocol}://{ip_address}:{port}
Health Check Interval: {health_check_interval}s
Last Response Time: {last_response_time}s
Status: {'Healthy' if is_healthy else 'Unhealthy'}
Error Count: {error_count}
""")

# Example 6: Common Mistakes (Commented to avoid errors)
print("\n6. COMMON MISTAKES (EXAMPLES)")
print("-" * 50)
print("These would cause errors if uncommented:")
print("# port = 8080")
print("# message = 'Port: ' + port  # ERROR: Can't concatenate str and int")
print("")
print("Correct way:")
port = 8080
message = f"Port: {port}"  # Using f-string
print(message)

# Example 7: Boolean Conversions
print("\n7. BOOLEAN CONVERSIONS")
print("-" * 50)
print(f"bool(0) = {bool(0)}")  # False
print(f"bool(1) = {bool(1)}")  # True
print(f"bool('') = {bool('')}")  # False (empty string)
print(f"bool('text') = {bool('text')}")  # True
print(f"bool([]) = {bool([])}")  # False (empty list)
print(f"bool([1,2,3]) = {bool([1,2,3])}")  # True

# Practical use
server_count = 0
if server_count:
    print("Servers are running")
else:
    print("No servers running")

print("\n" + "=" * 50)
print("END OF MODULE 1 EXAMPLES")
print("=" * 50)
