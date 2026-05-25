# Module 6: Exception Handling

## 📖 What You'll Learn
- Understanding exceptions
- try, except, else, finally blocks
- Handling specific exceptions
- Raising exceptions
- Best practices for error handling in DevOps

---

## 1. Understanding Exceptions

### Concept Explanation

An **exception** is an error that occurs during program execution. Instead of crashing, Python allows you to "catch" and handle these errors gracefully.

**Common exceptions:**
- `FileNotFoundError` - File doesn't exist
- `PermissionError` - No permission to access file
- `ValueError` - Invalid value (e.g., int("abc"))
- `TypeError` - Wrong type (e.g., "5" + 5)
- `KeyError` - Dictionary key doesn't exist
- `IndexError` - List index out of range
- `ZeroDivisionError` - Division by zero
- `ConnectionError` - Network connection failed

### DevOps Use Case

Exception handling is **critical** in DevOps for:
- Handling missing configuration files
- Dealing with network timeouts
- Managing API failures
- Handling permission issues
- Graceful degradation of services
- Retry logic for transient failures

### Code Example

```python
# Without exception handling - program crashes
# file = open('nonexistent.txt', 'r')  # FileNotFoundError!

# With exception handling - program continues
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found, using default configuration")
    content = "default_config"

print("Program continues...")
```

---

## 2. try-except Blocks

### Concept Explanation

**Syntax:**
```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Handle the exception
    handle_error()
```

### Code Example

```python
# Example 1: Basic try-except
try:
    port = int("8080abc")  # ValueError
except ValueError:
    print("Invalid port number")
    port = 8080

# Example 2: Multiple except blocks
try:
    config = {}
    port = config['port']  # KeyError
    port_num = int(port)   # ValueError
except KeyError:
    print("Port not found in config")
    port_num = 8080
except ValueError:
    print("Invalid port format")
    port_num = 8080

# Example 3: Catch multiple exceptions
try:
    result = risky_operation()
except (ValueError, TypeError, KeyError) as e:
    print(f"Error occurred: {e}")

# Example 4: Catch all exceptions (use sparingly!)
try:
    result = risky_operation()
except Exception as e:
    print(f"Unexpected error: {e}")

# Real DevOps example: Read config with fallback
def read_config(config_file):
    try:
        with open(config_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return "host=localhost\nport=8080"
    except PermissionError:
        print(f"No permission to read {config_file}")
        return None

config = read_config('app.config')
```

### Common Mistakes

❌ **Mistake 1**: Catching all exceptions without logging
```python
try:
    critical_operation()
except:
    pass  # Silent failure - very bad!
```

❌ **Mistake 2**: Too broad exception handling
```python
try:
    lots_of_code()
except Exception:
    print("Something went wrong")  # Too vague!
```

✅ **Fix**: Be specific, log errors
```python
try:
    connect_to_database()
except ConnectionError as e:
    print(f"Database connection failed: {e}")
    log_error(e)
```

---

## 3. else and finally Clauses

### Concept Explanation

- **else**: Runs if no exception occurred
- **finally**: Always runs, whether exception occurred or not

**Syntax:**
```python
try:
    risky_operation()
except ExceptionType:
    handle_error()
else:
    # Runs if no exception
    success_action()
finally:
    # Always runs
    cleanup()
```

### DevOps Use Case

- **else**: Log success, send notifications
- **finally**: Close connections, release resources, cleanup

### Code Example

```python
# Example 1: else clause
try:
    with open('config.txt', 'r') as file:
        config = file.read()
except FileNotFoundError:
    print("Config not found")
    config = None
else:
    print("Config loaded successfully")
    # This runs only if no exception

# Example 2: finally clause
file = None
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()  # Always close, even if error
    print("Cleanup completed")

# Example 3: All together
def deploy_application(env):
    connection = None
    try:
        print(f"Connecting to {env}...")
        connection = connect_to_server(env)
        
        print("Deploying application...")
        deploy(connection)
        
    except ConnectionError as e:
        print(f"Connection failed: {e}")
        return False
    except DeploymentError as e:
        print(f"Deployment failed: {e}")
        return False
    else:
        print("Deployment successful!")
        send_notification("Deployment completed")
        return True
    finally:
        if connection:
            connection.close()
        print("Cleaned up resources")

# Real DevOps example: Database operation
def execute_query(query):
    connection = None
    cursor = None
    
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        
    except ConnectionError:
        print("Database connection failed")
        return None
    except Exception as e:
        print(f"Query failed: {e}")
        return None
    else:
        print(f"Query successful, {len(results)} rows")
        return results
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed")
```

---

## 4. Raising Exceptions

### Concept Explanation

You can **raise** exceptions in your code to signal errors.

**Syntax:**
```python
raise ExceptionType("Error message")
```

### DevOps Use Case

Raise exceptions to:
- Validate input parameters
- Enforce business rules
- Signal configuration errors
- Stop execution on critical failures

### Code Example

```python
# Example 1: Raise built-in exception
def validate_port(port):
    if not isinstance(port, int):
        raise TypeError("Port must be an integer")
    if port < 1 or port > 65535:
        raise ValueError(f"Invalid port: {port}. Must be 1-65535")
    return True

try:
    validate_port(99999)
except ValueError as e:
    print(f"Validation error: {e}")

# Example 2: Raise with custom message
def connect_to_server(host, port):
    if not host:
        raise ValueError("Host cannot be empty")
    if port < 1:
        raise ValueError("Invalid port number")
    
    # Connection logic here
    print(f"Connecting to {host}:{port}")

# Example 3: Re-raise exception
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        raise  # Re-raise the same exception

# Real DevOps example: Validate deployment config
def validate_deployment_config(config):
    required_keys = ['environment', 'version', 'region']
    
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required config: {key}")
    
    if config['environment'] not in ['dev', 'staging', 'prod']:
        raise ValueError(f"Invalid environment: {config['environment']}")
    
    return True

try:
    config = {'environment': 'production', 'version': '1.0'}
    validate_deployment_config(config)
except KeyError as e:
    print(f"Configuration error: {e}")
except ValueError as e:
    print(f"Validation error: {e}")
```

---

## 5. Custom Exceptions

### Concept Explanation

Create custom exception classes for specific error types in your application.

### Code Example

```python
# Define custom exceptions
class DeploymentError(Exception):
    """Raised when deployment fails"""
    pass

class ConfigurationError(Exception):
    """Raised when configuration is invalid"""
    pass

class ServerNotFoundError(Exception):
    """Raised when server is not found"""
    pass

# Use custom exceptions
def deploy_to_server(server_name, version):
    if not server_exists(server_name):
        raise ServerNotFoundError(f"Server {server_name} not found")
    
    if not version:
        raise ConfigurationError("Version cannot be empty")
    
    # Deployment logic
    success = perform_deployment(server_name, version)
    
    if not success:
        raise DeploymentError(f"Failed to deploy {version} to {server_name}")
    
    return True

# Handle custom exceptions
try:
    deploy_to_server("web-01", "2.0.0")
except ServerNotFoundError as e:
    print(f"Server error: {e}")
    # Maybe create the server?
except ConfigurationError as e:
    print(f"Config error: {e}")
    # Use default configuration
except DeploymentError as e:
    print(f"Deployment error: {e}")
    # Rollback or retry
```

---

## 6. Best Practices for DevOps

### Code Example

```python
# ✅ GOOD: Specific exception handling with logging
import logging

def read_server_config(config_file):
    try:
        with open(config_file, 'r') as file:
            return parse_config(file.read())
    except FileNotFoundError:
        logging.error(f"Config file not found: {config_file}")
        return get_default_config()
    except PermissionError:
        logging.error(f"No permission to read: {config_file}")
        raise  # Re-raise critical errors
    except Exception as e:
        logging.error(f"Unexpected error reading config: {e}")
        return None

# ✅ GOOD: Retry logic with exception handling
def connect_with_retry(host, port, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            connection = connect(host, port)
            return connection
        except ConnectionError as e:
            if attempt == max_retries:
                logging.error(f"Failed after {max_retries} attempts: {e}")
                raise
            logging.warning(f"Attempt {attempt} failed, retrying...")
            time.sleep(2)

# ✅ GOOD: Validate before risky operations
def deploy_application(config):
    # Validate first
    try:
        validate_config(config)
    except ConfigurationError as e:
        logging.error(f"Invalid configuration: {e}")
        return False
    
    # Then deploy
    try:
        perform_deployment(config)
    except DeploymentError as e:
        logging.error(f"Deployment failed: {e}")
        rollback()
        return False
    else:
        logging.info("Deployment successful")
        return True
    finally:
        cleanup_temp_files()

# ✅ GOOD: Context-specific error messages
def check_server_health(server):
    try:
        response = ping_server(server)
    except ConnectionError:
        return {
            'status': 'down',
            'message': f'Cannot connect to {server}',
            'action': 'Check network connectivity'
        }
    except TimeoutError:
        return {
            'status': 'timeout',
            'message': f'{server} not responding',
            'action': 'Check if server is overloaded'
        }
    else:
        return {
            'status': 'healthy',
            'message': f'{server} is responding',
            'action': None
        }
```

---

## 🎯 Mini Exercise 1: File Reader with Error Handling

**Task**: Create a function that reads a file with proper error handling.

**Requirements:**
1. Try to read the file
2. Handle FileNotFoundError
3. Handle PermissionError
4. Return content or None

---

## ✅ Solution 1

```python
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test
content = safe_read_file('config.txt')
if content:
    print("File read successfully")
else:
    print("Using default configuration")
```

---

## 🎯 Mini Exercise 2: Port Validator

**Task**: Create a function that validates port numbers and raises appropriate exceptions.

---

## ✅ Solution 2

```python
def validate_port(port):
    if not isinstance(port, int):
        raise TypeError(f"Port must be integer, got {type(port).__name__}")
    
    if port < 1 or port > 65535:
        raise ValueError(f"Port {port} out of range (1-65535)")
    
    return True

# Test
try:
    validate_port(8080)
    print("Port is valid")
except (TypeError, ValueError) as e:
    print(f"Validation error: {e}")

try:
    validate_port("8080")
except TypeError as e:
    print(f"Type error: {e}")
```

---

## 📝 Key Takeaways

✅ **Always handle expected exceptions** - Don't let programs crash
✅ **Be specific** - Catch specific exceptions, not generic Exception
✅ **Log errors** - For debugging and monitoring
✅ **Use finally for cleanup** - Close files, connections
✅ **Provide helpful error messages** - For troubleshooting
✅ **Don't silence errors** - Log or re-raise critical issues
✅ **Validate input early** - Fail fast with clear messages

---

## 🚀 Practice Challenge

Create a server health checker that:
1. Tries to connect to a server
2. Handles ConnectionError, TimeoutError
3. Retries 3 times with delays
4. Returns detailed status
5. Uses finally to cleanup
6. Logs all attempts

---

## Next Module

Ready for **Module 7: Virtual Environments & Packaging**? Learn professional Python project management! 🎯
