# Module 6: Exception Handling - Exercise Solutions

print("=" * 50)
print("MODULE 6 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: Basic Exception Handling
print("\nSolution 1: Basic Exception Handling")
print("-" * 50)

def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None

print(safe_int_convert("123"))
print(safe_int_convert("abc"))

# Solution 2: File Reading with Exception
print("\nSolution 2: File Reading with Exception")
print("-" * 50)

def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# Create test file
with open('test.txt', 'w') as f:
    f.write("Test content")

print(read_file_safe('test.txt'))
print(read_file_safe('nonexistent.txt'))

# Solution 3: Multiple Exceptions
print("\nSolution 3: Multiple Exceptions")
print("-" * 50)

def get_int_value(data, key):
    try:
        value = data[key]
        return int(value)
    except KeyError:
        print(f"Key '{key}' not found")
        return None
    except ValueError:
        print(f"Cannot convert value to integer")
        return None

config = {"port": "8080", "host": "localhost"}
print(get_int_value(config, "port"))
print(get_int_value(config, "timeout"))
print(get_int_value({"port": "abc"}, "port"))

# Solution 4: else Clause
print("\nSolution 4: else Clause")
print("-" * 50)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Success")
        return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# Solution 5: finally Clause
print("\nSolution 5: finally Clause")
print("-" * 50)

def read_with_cleanup(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found")
        return None
    finally:
        print("Cleanup done")

read_with_cleanup('test.txt')
read_with_cleanup('missing.txt')

# Solution 6: Raising Exceptions
print("\nSolution 6: Raising Exceptions")
print("-" * 50)

def validate_port(port):
    if not isinstance(port, int):
        raise TypeError(f"Port must be integer, got {type(port).__name__}")
    if port < 1 or port > 65535:
        raise ValueError(f"Port {port} out of range (1-65535)")
    return True

try:
    validate_port(8080)
    print("Port 8080 is valid")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

try:
    validate_port("8080")
except TypeError as e:
    print(f"Error: {e}")

try:
    validate_port(99999)
except ValueError as e:
    print(f"Error: {e}")

# Solution 7: Custom Exception
print("\nSolution 7: Custom Exception")
print("-" * 50)

class ServerError(Exception):
    pass

def check_server_status(status):
    if status == "down":
        raise ServerError("Server is down")
    return "Server is running"

try:
    print(check_server_status("running"))
except ServerError as e:
    print(f"Error: {e}")

try:
    print(check_server_status("down"))
except ServerError as e:
    print(f"Error: {e}")

# Solution 8: Retry Logic
print("\nSolution 8: Retry Logic")
print("-" * 50)

def connect_with_retry(max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}...")
            
            if attempt < 3:
                raise ConnectionError("Connection failed")
            
            print("Connected!")
            return True
            
        except ConnectionError as e:
            if attempt == max_retries:
                print(f"Failed after {max_retries} attempts")
                raise
            print("Retrying...")

try:
    connect_with_retry()
except ConnectionError:
    print("Could not connect")

# Solution 9: Exception with Logging
print("\nSolution 9: Exception with Logging")
print("-" * 50)

def read_config_with_logging(filename):
    try:
        with open(filename, 'r') as file:
            config = file.read()
            print(f"INFO: Config loaded from {filename}")
            return config
    except FileNotFoundError:
        print(f"ERROR: Config file {filename} not found")
        return None
    except PermissionError:
        print(f"ERROR: No permission to read {filename}")
        return None

read_config_with_logging('test.txt')
read_config_with_logging('missing.txt')

# Solution 10: Advanced - Server Health Checker
print("\nSolution 10: Advanced - Server Health Checker")
print("-" * 50)

def check_server(server):
    try:
        name = server['name']
        status = server['status']
        cpu = server['cpu']
        
        if status == 'down':
            raise ConnectionError(f"Cannot connect to {name}")
        
        if cpu > 90:
            raise RuntimeError(f"CPU critical on {name}: {cpu}%")
        
        return {'server': name, 'status': 'healthy', 'cpu': cpu}
        
    except ConnectionError as e:
        print(f"Connection error: {e}")
        return {'server': server['name'], 'status': 'unreachable'}
    except RuntimeError as e:
        print(f"Health warning: {e}")
        return {'server': server['name'], 'status': 'critical'}
    except KeyError as e:
        print(f"Missing key in server data: {e}")
        return {'server': 'unknown', 'status': 'error'}

servers = [
    {'name': 'web-01', 'status': 'running', 'cpu': 45},
    {'name': 'web-02', 'status': 'down', 'cpu': 0},
    {'name': 'web-03', 'status': 'running', 'cpu': 95}
]

print("\nServer Health Check Results:")
for server in servers:
    result = check_server(server)
    print(f"  {result['server']}: {result['status']}")

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
