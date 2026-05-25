# Module 6: Exception Handling - Code Examples

import time
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

print("=" * 50)
print("MODULE 6: EXCEPTION HANDLING - EXAMPLES")
print("=" * 50)

# Example 1: Basic try-except
print("\n1. BASIC TRY-EXCEPT")
print("-" * 50)

try:
    port = int("8080abc")
except ValueError:
    print("Invalid port format, using default")
    port = 8080

print(f"Port: {port}")

# Example 2: Multiple except blocks
print("\n2. MULTIPLE EXCEPT BLOCKS")
print("-" * 50)

def get_config_value(config, key):
    try:
        value = config[key]
        return int(value)
    except KeyError:
        print(f"Key '{key}' not found in config")
        return None
    except ValueError:
        print(f"Invalid value format for '{key}'")
        return None

config = {"host": "localhost", "port": "8080"}
port = get_config_value(config, "port")
timeout = get_config_value(config, "timeout")

# Example 3: File handling with exceptions
print("\n3. FILE HANDLING WITH EXCEPTIONS")
print("-" * 50)

def read_config_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Config file '{filename}' not found, using defaults")
        return "host=localhost\nport=8080"
    except PermissionError:
        print(f"No permission to read '{filename}'")
        return None

config = read_config_file('app.config')
print(f"Config loaded: {len(config) if config else 0} characters")

# Example 4: else clause
print("\n4. ELSE CLAUSE")
print("-" * 50)

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    else:
        print(f"File read successfully: {len(data)} bytes")
        return data

# Create a test file
with open('test_data.txt', 'w') as f:
    f.write("Sample data")

result = process_file('test_data.txt')

# Example 5: finally clause
print("\n5. FINALLY CLAUSE")
print("-" * 50)

def connect_to_server(host):
    connection = None
    try:
        print(f"Connecting to {host}...")
        connection = f"Connection to {host}"
        print("Connected!")
        return connection
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
    finally:
        print("Cleanup completed")

result = connect_to_server("192.168.1.10")

# Example 6: Raising exceptions
print("\n6. RAISING EXCEPTIONS")
print("-" * 50)

def validate_port(port):
    if not isinstance(port, int):
        raise TypeError(f"Port must be integer, got {type(port).__name__}")
    if port < 1 or port > 65535:
        raise ValueError(f"Port {port} out of valid range (1-65535)")
    return True

try:
    validate_port(8080)
    print("Port 8080 is valid")
except (TypeError, ValueError) as e:
    print(f"Validation error: {e}")

try:
    validate_port(99999)
except ValueError as e:
    print(f"Error: {e}")

# Example 7: Custom exceptions
print("\n7. CUSTOM EXCEPTIONS")
print("-" * 50)

class DeploymentError(Exception):
    pass

class ConfigurationError(Exception):
    pass

def deploy_application(env, version):
    if env not in ['dev', 'staging', 'prod']:
        raise ConfigurationError(f"Invalid environment: {env}")
    
    if not version:
        raise DeploymentError("Version cannot be empty")
    
    print(f"Deploying {version} to {env}")
    return True

try:
    deploy_application("production", "2.0.0")
except ConfigurationError as e:
    print(f"Config error: {e}")
except DeploymentError as e:
    print(f"Deployment error: {e}")

# Example 8: Retry logic with exceptions
print("\n8. RETRY LOGIC WITH EXCEPTIONS")
print("-" * 50)

def connect_with_retry(host, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}: Connecting to {host}...")
            
            if attempt < 3:
                raise ConnectionError("Connection failed")
            
            print("Connected successfully!")
            return True
            
        except ConnectionError as e:
            if attempt == max_retries:
                print(f"Failed after {max_retries} attempts")
                raise
            print(f"  Retrying in 1 second...")
            time.sleep(1)

try:
    connect_with_retry("192.168.1.10")
except ConnectionError:
    print("Could not establish connection")

# Example 9: Exception with logging
print("\n9. EXCEPTION WITH LOGGING")
print("-" * 50)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error(f"Division by zero: {a} / {b}")
        return None
    except TypeError as e:
        logging.error(f"Type error in division: {e}")
        return None
    else:
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result

safe_divide(10, 2)
safe_divide(10, 0)

# Example 10: Real DevOps - Server health check
print("\n10. REAL DEVOPS - SERVER HEALTH CHECK")
print("-" * 50)

def check_server_health(server):
    try:
        print(f"Checking {server['name']}...")
        
        if server['status'] == 'down':
            raise ConnectionError(f"Cannot connect to {server['name']}")
        
        if server['cpu'] > 90:
            raise RuntimeError(f"CPU critical: {server['cpu']}%")
        
        return {
            'server': server['name'],
            'status': 'healthy',
            'cpu': server['cpu']
        }
        
    except ConnectionError as e:
        logging.error(f"Connection error: {e}")
        return {'server': server['name'], 'status': 'unreachable'}
    except RuntimeError as e:
        logging.warning(f"Health check warning: {e}")
        return {'server': server['name'], 'status': 'critical'}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {'server': server['name'], 'status': 'unknown'}

servers = [
    {'name': 'web-01', 'status': 'running', 'cpu': 45},
    {'name': 'web-02', 'status': 'down', 'cpu': 0},
    {'name': 'web-03', 'status': 'running', 'cpu': 95}
]

print("\nHealth Check Results:")
for server in servers:
    result = check_server_health(server)
    print(f"  {result['server']}: {result['status']}")

# Example 11: Context manager with exception
print("\n11. CONTEXT MANAGER WITH EXCEPTION")
print("-" * 50)

def process_log_file(filename):
    try:
        with open(filename, 'r') as file:
            error_count = 0
            for line in file:
                if 'ERROR' in line:
                    error_count += 1
            return error_count
    except FileNotFoundError:
        logging.error(f"Log file not found: {filename}")
        return -1
    except Exception as e:
        logging.error(f"Error processing log: {e}")
        return -1

# Create sample log
with open('sample.log', 'w') as f:
    f.write("INFO: Server started\n")
    f.write("ERROR: Connection failed\n")
    f.write("ERROR: Timeout\n")

errors = process_log_file('sample.log')
print(f"Errors found: {errors}")

print("\n" + "=" * 50)
print("END OF MODULE 6 EXAMPLES")
print("=" * 50)
