# Module 16: Python DevOps Interview Preparation

## 📖 Complete Interview Guide

This module contains real-world interview questions with detailed answers and explanations for Python DevOps roles.

---

## Section 1: Python Fundamentals

### Q1: What is the difference between a list and a tuple in Python?

**Answer:**

**Lists:**
- Mutable (can be modified after creation)
- Defined with square brackets `[]`
- Slower than tuples
- Used when data needs to change

**Tuples:**
- Immutable (cannot be modified after creation)
- Defined with parentheses `()`
- Faster than lists
- Used for fixed data

**Example:**
```python
# List - mutable
servers = ['web-01', 'web-02', 'web-03']
servers.append('web-04')  # Works fine
servers[0] = 'web-05'     # Works fine

# Tuple - immutable
config = ('localhost', 8080, 'production')
config[0] = '127.0.0.1'   # ERROR! Cannot modify
```

**DevOps Use Case:**
- Use **lists** for: server lists, log entries, dynamic configurations
- Use **tuples** for: fixed configs (host, port), database credentials, return multiple values

**Why This Matters:**
- Tuples are hashable (can be dictionary keys)
- Tuples use less memory
- Tuples protect data from accidental modification

---

### Q2: Explain the difference between `==` and `is` in Python.

**Answer:**

**`==` (Equality operator):**
- Compares **values**
- Checks if contents are equal

**`is` (Identity operator):**
- Compares **object identity**
- Checks if both variables point to the same object in memory

**Example:**
```python
# Example 1: Strings
a = "hello"
b = "hello"
print(a == b)  # True (same value)
print(a is b)  # True (Python interns small strings)

# Example 2: Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (same values)
print(list1 is list2)  # False (different objects)

# Example 3: None check
config = None
if config is None:  # Correct way
    print("Config not set")

if config == None:  # Works but not recommended
    print("Config not set")
```

**Best Practice:**
- Use `==` for value comparison
- Use `is` only for `None`, `True`, `False`

**DevOps Scenario:**
```python
def get_config():
    config = load_config()
    if config is None:  # Correct
        return default_config()
    return config
```

---

### Q3: What are Python decorators and how are they used in DevOps?

**Answer:**

**Definition:**
A decorator is a function that modifies the behavior of another function without changing its code.

**Syntax:**
```python
@decorator_name
def function():
    pass
```

**Basic Example:**
```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_execution
def deploy_app(env):
    print(f"Deploying to {env}")

deploy_app('production')
# Output:
# Executing deploy_app
# Deploying to production
# Finished deploy_app
```

**DevOps Use Cases:**

**1. Retry Logic:**
```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed, retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def connect_to_database():
    # Connection logic
    pass
```

**2. Timing Decorator:**
```python
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

@measure_time
def backup_database():
    # Backup logic
    pass
```

**3. Authentication Decorator:**
```python
def require_auth(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def deploy_to_production():
    # Deployment logic
    pass
```

---

## Section 2: Data Structures & Algorithms

### Q4: How do you remove duplicates from a list while preserving order?

**Answer:**

**Method 1: Using dict (Python 3.7+):**
```python
def remove_duplicates(items):
    return list(dict.fromkeys(items))

servers = ['web-01', 'web-02', 'web-01', 'db-01', 'web-02']
unique = remove_duplicates(servers)
print(unique)  # ['web-01', 'web-02', 'db-01']
```

**Method 2: Using set (loses order):**
```python
servers = ['web-01', 'web-02', 'web-01']
unique = list(set(servers))  # Order not preserved
```

**Method 3: Manual iteration:**
```python
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

**DevOps Scenario:**
```python
# Remove duplicate servers from monitoring list
monitored_servers = ['web-01', 'db-01', 'web-01', 'cache-01', 'db-01']
unique_servers = list(dict.fromkeys(monitored_servers))
print(f"Monitoring {len(unique_servers)} unique servers")
```

**Why This Matters:**
- Prevents duplicate monitoring
- Reduces API calls
- Optimizes resource usage

---

### Q5: Explain list comprehension and when to use it.

**Answer:**

**Definition:**
List comprehension is a concise way to create lists based on existing iterables.

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Examples:**

**Basic:**
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]
```

**With Condition:**
```python
# Get only running servers
servers = [
    {'name': 'web-01', 'status': 'running'},
    {'name': 'web-02', 'status': 'stopped'},
    {'name': 'web-03', 'status': 'running'}
]

running = [s['name'] for s in servers if s['status'] == 'running']
# ['web-01', 'web-03']
```

**Nested:**
```python
# Flatten list of lists
logs = [['error1', 'error2'], ['error3'], ['error4', 'error5']]
all_errors = [error for sublist in logs for error in sublist]
# ['error1', 'error2', 'error3', 'error4', 'error5']
```

**DevOps Examples:**

**1. Extract IPs:**
```python
servers = ['web-01:192.168.1.10', 'web-02:192.168.1.11']
ips = [s.split(':')[1] for s in servers]
```

**2. Filter logs:**
```python
logs = ['INFO: Started', 'ERROR: Failed', 'INFO: Done', 'ERROR: Timeout']
errors = [log for log in logs if 'ERROR' in log]
```

**3. Transform data:**
```python
ports = ['80', '443', '8080']
port_numbers = [int(p) for p in ports]
```

**When to Use:**
- ✅ Simple transformations
- ✅ Filtering data
- ✅ Creating new lists from existing ones

**When NOT to Use:**
- ❌ Complex logic (use regular loops)
- ❌ Side effects (printing, file writing)
- ❌ Very long expressions (readability)

---

## Section 3: File Operations & I/O

### Q6: How do you read a large log file efficiently in Python?

**Answer:**

**Problem:**
Reading entire file into memory can crash the application with large files.

**Solution: Read line by line**

**Method 1: Using iteration (Best):**
```python
def process_large_log(filename):
    error_count = 0
    with open(filename, 'r') as f:
        for line in f:  # Reads one line at a time
            if 'ERROR' in line:
                error_count += 1
    return error_count
```

**Method 2: Using readline():**
```python
def process_log_readline(filename):
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            # Process line
```

**Method 3: Reading in chunks:**
```python
def process_in_chunks(filename, chunk_size=1024*1024):  # 1MB chunks
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # Process chunk
```

**Real DevOps Example:**
```python
def analyze_nginx_log(log_file):
    """Analyze nginx access log efficiently"""
    stats = {
        '200': 0,
        '404': 0,
        '500': 0,
        'other': 0
    }
    
    with open(log_file, 'r') as f:
        for line in f:
            if ' 200 ' in line:
                stats['200'] += 1
            elif ' 404 ' in line:
                stats['404'] += 1
            elif ' 500 ' in line:
                stats['500'] += 1
            else:
                stats['other'] += 1
    
    return stats

# Process 10GB log file without loading into memory
stats = analyze_nginx_log('/var/log/nginx/access.log')
print(f"200 OK: {stats['200']}")
print(f"404 Not Found: {stats['404']}")
print(f"500 Errors: {stats['500']}")
```

**Why This Matters:**
- Memory efficient
- Works with files larger than RAM
- Faster processing
- Production-ready

---

### Q7: Explain the difference between `read()`, `readline()`, and `readlines()`.

**Answer:**

**`read()`:**
- Reads **entire file** as a single string
- Returns one string

```python
with open('config.txt', 'r') as f:
    content = f.read()
    print(type(content))  # <class 'str'>
```

**`readline()`:**
- Reads **one line** at a time
- Returns a string
- Moves file pointer to next line

```python
with open('config.txt', 'r') as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
```

**`readlines()`:**
- Reads **all lines** into a list
- Returns list of strings
- Each element is one line

```python
with open('config.txt', 'r') as f:
    lines = f.readlines()
    print(type(lines))  # <class 'list'>
    for line in lines:
        print(line.strip())
```

**Comparison Table:**

| Method | Returns | Memory Usage | Use Case |
|--------|---------|--------------|----------|
| `read()` | String | High | Small files |
| `readline()` | String | Low | Line-by-line processing |
| `readlines()` | List | High | Need all lines as list |
| Iteration | String | Low | Large files (BEST) |

**Best Practice (Iteration):**
```python
# Most efficient for large files
with open('large.log', 'r') as f:
    for line in f:  # Uses iterator
        process(line)
```

**DevOps Example:**
```python
def parse_config_file(filename):
    """Parse key=value config file"""
    config = {}
    
    with open(filename, 'r') as f:
        for line in f:  # Efficient iteration
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=')
                config[key.strip()] = value.strip()
    
    return config

# Usage
config = parse_config_file('app.conf')
print(config['database_host'])
```

---

## Section 4: Exception Handling

### Q8: What is the difference between `except Exception` and `except BaseException`?

**Answer:**

**Exception Hierarchy:**
```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    ├── ValueError
    ├── TypeError
    └── ... (all other exceptions)
```

**`except Exception`:**
- Catches **most** exceptions
- Does NOT catch: SystemExit, KeyboardInterrupt, GeneratorExit
- **Recommended** for general error handling

**`except BaseException`:**
- Catches **ALL** exceptions
- Including system exits and keyboard interrupts
- **Dangerous** - can prevent Ctrl+C from working

**Example:**
```python
# GOOD - except Exception
try:
    result = risky_operation()
except Exception as e:
    print(f"Error: {e}")
    # Ctrl+C still works

# BAD - except BaseException
try:
    result = risky_operation()
except BaseException as e:
    print(f"Error: {e}")
    # Ctrl+C won't work! Dangerous!
```

**DevOps Best Practice:**
```python
def deploy_application():
    try:
        # Deployment logic
        run_tests()
        build_app()
        deploy()
    except KeyboardInterrupt:
        # Handle Ctrl+C specifically
        print("\nDeployment cancelled by user")
        cleanup()
        raise
    except Exception as e:
        # Handle other errors
        print(f"Deployment failed: {e}")
        rollback()
        raise
```

**Specific Exception Handling:**
```python
import requests

def fetch_server_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except requests.Timeout:
        print("Request timed out")
    except requests.ConnectionError:
        print("Connection failed")
    except ValueError:
        print("Invalid JSON response")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Key Points:**
- ✅ Use `except Exception` for general error handling
- ✅ Catch specific exceptions when possible
- ❌ Avoid `except BaseException`
- ❌ Avoid bare `except:` (catches everything)

---

## Section 5: Working with APIs

### Q9: How do you handle API rate limiting in Python?

**Answer:**

**Problem:**
APIs limit the number of requests per time period. Exceeding limits results in errors.

**Solution 1: Simple Retry with Backoff**
```python
import time
import requests

def api_call_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            
            if response.status_code == 429:  # Rate limited
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
            
            response.raise_for_status()
            return response.json()
            
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
    
    raise Exception("Max retries exceeded")
```

**Solution 2: Using Rate Limiter**
```python
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, time_window):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Remove old calls outside time window
            while self.calls and self.calls[0] < now - self.time_window:
                self.calls.popleft()
            
            # Check if we can make a call
            if len(self.calls) >= self.max_calls:
                sleep_time = self.time_window - (now - self.calls[0])
                print(f"Rate limit reached. Sleeping {sleep_time:.2f}s")
                time.sleep(sleep_time)
                self.calls.popleft()
            
            # Make the call
            self.calls.append(time.time())
            return func(*args, **kwargs)
        
        return wrapper

# Usage: Max 10 calls per 60 seconds
@RateLimiter(max_calls=10, time_window=60)
def fetch_github_repo(repo):
    response = requests.get(f'https://api.github.com/repos/{repo}')
    return response.json()

# These calls will be automatically rate-limited
for repo in ['kubernetes/kubernetes', 'docker/docker', 'ansible/ansible']:
    data = fetch_github_repo(repo)
    print(f"{repo}: {data['stargazers_count']} stars")
```

**Solution 3: Check Rate Limit Headers**
```python
def smart_api_call(url):
    response = requests.get(url)
    
    # Check rate limit headers
    remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
    reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
    
    if remaining < 10:
        wait_time = reset_time - time.time()
        print(f"Low on API calls. Waiting {wait_time}s")
        time.sleep(wait_time)
    
    return response.json()
```

**Real DevOps Example:**
```python
class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'token {token}'})
    
    def _check_rate_limit(self):
        """Check current rate limit status"""
        response = self.session.get(f'{self.base_url}/rate_limit')
        data = response.json()
        remaining = data['rate']['remaining']
        reset = data['rate']['reset']
        
        if remaining < 10:
            wait = reset - time.time() + 1
            print(f"Rate limit low. Waiting {wait:.0f}s")
            time.sleep(wait)
    
    def get_repo(self, owner, repo):
        self._check_rate_limit()
        response = self.session.get(f'{self.base_url}/repos/{owner}/{repo}')
        response.raise_for_status()
        return response.json()
```

---

## Section 6: Concurrency & Performance

### Q10: Explain the difference between threading, multiprocessing, and asyncio in Python.

**Answer:**

**1. Threading:**
- Multiple threads in **one process**
- Shares memory
- Limited by GIL (Global Interpreter Lock)
- Good for **I/O-bound** tasks

```python
import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"{url}: {response.status_code}")

urls = ['https://google.com', 'https://github.com', 'https://python.org']

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
```

**2. Multiprocessing:**
- Multiple **separate processes**
- Separate memory
- No GIL limitation
- Good for **CPU-bound** tasks

```python
from multiprocessing import Pool

def process_log_file(filename):
    # CPU-intensive processing
    with open(filename) as f:
        return len([line for line in f if 'ERROR' in line])

log_files = ['app1.log', 'app2.log', 'app3.log', 'app4.log']

with Pool(processes=4) as pool:
    results = pool.map(process_log_file, log_files)

print(f"Total errors: {sum(results)}")
```

**3. Asyncio:**
- Single thread, **event loop**
- Cooperative multitasking
- Very efficient for **I/O-bound** tasks
- Modern approach

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['https://google.com', 'https://github.com', 'https://python.org']
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f"Fetched {len(results)} URLs")

asyncio.run(main())
```

**Comparison:**

| Feature | Threading | Multiprocessing | Asyncio |
|---------|-----------|-----------------|---------|
| **Best for** | I/O-bound | CPU-bound | I/O-bound |
| **Memory** | Shared | Separate | Shared |
| **GIL** | Limited by GIL | No GIL | No GIL issue |
| **Overhead** | Low | High | Very low |
| **Complexity** | Medium | High | Medium |

**DevOps Use Cases:**

**Threading - API calls:**
```python
def check_multiple_servers(servers):
    results = []
    threads = []
    
    def check(server):
        status = ping_server(server)
        results.append((server, status))
    
    for server in servers:
        t = threading.Thread(target=check, args=(server,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    return results
```

**Multiprocessing - Log processing:**
```python
def process_logs_parallel(log_files):
    with Pool(processes=4) as pool:
        results = pool.map(analyze_log, log_files)
    return results
```

**Asyncio - Monitoring:**
```python
async def monitor_endpoints(endpoints):
    async with aiohttp.ClientSession() as session:
        tasks = [check_endpoint(session, ep) for ep in endpoints]
        return await asyncio.gather(*tasks)
```

**When to Use:**
- 🌐 **I/O-bound** (network, files): Threading or Asyncio
- 🔢 **CPU-bound** (calculations, parsing): Multiprocessing
- 📊 **Many concurrent I/O**: Asyncio (most efficient)

---

## Section 7: DevOps-Specific Questions

### Q11: How would you automate server provisioning using Python?

**Answer:**

**Complete Example using boto3 (AWS):**

```python
import boto3
import time

class ServerProvisioner:
    def __init__(self, region='us-east-1'):
        self.ec2 = boto3.client('ec2', region_name=region)
        self.ec2_resource = boto3.resource('ec2', region_name=region)
    
    def create_instance(self, name, instance_type='t2.micro', ami_id=None):
        """Create EC2 instance"""
        if not ami_id:
            # Get latest Amazon Linux 2 AMI
            ami_id = self._get_latest_ami()
        
        # Create instance
        instances = self.ec2_resource.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }],
            UserData=self._get_user_data()
        )
        
        instance = instances[0]
        print(f"Creating instance {instance.id}...")
        
        # Wait for instance to be running
        instance.wait_until_running()
        instance.reload()
        
        print(f"Instance {instance.id} is running")
        print(f"Public IP: {instance.public_ip_address}")
        
        return {
            'id': instance.id,
            'public_ip': instance.public_ip_address,
            'private_ip': instance.private_ip_address,
            'state': instance.state['Name']
        }
    
    def _get_latest_ami(self):
        """Get latest Amazon Linux 2 AMI"""
        response = self.ec2.describe_images(
            Owners=['amazon'],
            Filters=[
                {'Name': 'name', 'Values': ['amzn2-ami-hvm-*-x86_64-gp2']},
                {'Name': 'state', 'Values': ['available']}
            ]
        )
        
        # Sort by creation date
        images = sorted(response['Images'], 
                       key=lambda x: x['CreationDate'], 
                       reverse=True)
        return images[0]['ImageId']
    
    def _get_user_data(self):
        """Bootstrap script for new instances"""
        return '''#!/bin/bash
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user
'''
    
    def provision_web_cluster(self, count=3):
        """Provision multiple web servers"""
        servers = []
        
        for i in range(1, count + 1):
            server = self.create_instance(
                name=f'web-server-{i}',
                instance_type='t2.micro'
            )
            servers.append(server)
            time.sleep(2)  # Rate limiting
        
        return servers
    
    def list_instances(self):
        """List all running instances"""
        instances = self.ec2_resource.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        
        result = []
        for instance in instances:
            name = next((tag['Value'] for tag in instance.tags 
                        if tag['Key'] == 'Name'), 'N/A')
            result.append({
                'id': instance.id,
                'name': name,
                'type': instance.instance_type,
                'public_ip': instance.public_ip_address,
                'state': instance.state['Name']
            })
        
        return result
    
    def terminate_instance(self, instance_id):
        """Terminate an instance"""
        instance = self.ec2_resource.Instance(instance_id)
        instance.terminate()
        print(f"Terminating instance {instance_id}")

# Usage
provisioner = ServerProvisioner(region='us-east-1')

# Create single server
server = provisioner.create_instance('my-web-server')

# Create cluster
cluster = provisioner.provision_web_cluster(count=3)

# List all servers
servers = provisioner.list_instances()
for s in servers:
    print(f"{s['name']}: {s['public_ip']}")
```

**Key Concepts:**
1. **Idempotency** - Can run multiple times safely
2. **Error handling** - Graceful failures
3. **Logging** - Track what's happening
4. **Configuration** - Externalize settings
5. **Cleanup** - Remove resources when done

---

### Q12: How do you implement a deployment pipeline in Python?

**Answer:**

**Complete CI/CD Pipeline Implementation:**

```python
import subprocess
import sys
import os
import json
from datetime import datetime
from pathlib import Path

class DeploymentPipeline:
    def __init__(self, config_file='deploy_config.json'):
        self.config = self._load_config(config_file)
        self.environment = os.getenv('DEPLOY_ENV', 'dev')
        self.version = os.getenv('VERSION', 'latest')
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.deployment_log = []
    
    def _load_config(self, config_file):
        """Load deployment configuration"""
        with open(config_file, 'r') as f:
            return json.load(f)
    
    def _log(self, message, level='INFO'):
        """Log deployment steps"""
        log_entry = f"[{datetime.now()}] [{level}] {message}"
        print(log_entry)
        self.deployment_log.append(log_entry)
    
    def _run_command(self, command, check=True):
        """Run shell command"""
        self._log(f"Running: {command}")
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        
        if check and result.returncode != 0:
            self._log(f"Command failed: {result.stderr}", 'ERROR')
            raise Exception(f"Command failed: {command}")
        
        return result
    
    def validate_environment(self):
        """Validate deployment environment"""
        self._log("Validating environment...")
        
        valid_envs = self.config.get('environments', [])
        if self.environment not in valid_envs:
            raise ValueError(f"Invalid environment: {self.environment}")
        
        # Check required tools
        required_tools = ['git', 'docker', 'kubectl']
        for tool in required_tools:
            result = subprocess.run(['which', tool], capture_output=True)
            if result.returncode != 0:
                raise Exception(f"Required tool not found: {tool}")
        
        self._log("✓ Environment validated")
        return True
    
    def run_tests(self):
        """Run test suite"""
        self._log("Running tests...")
        
        test_command = self.config.get('test_command', 'pytest')
        result = self._run_command(test_command, check=False)
        
        if result.returncode != 0:
            self._log("✗ Tests failed", 'ERROR')
            return False
        
        self._log("✓ All tests passed")
        return True
    
    def build_application(self):
        """Build application"""
        self._log("Building application...")
        
        # Build Docker image
        image_name = f"{self.config['app_name']}:{self.version}"
        build_cmd = f"docker build -t {image_name} ."
        
        self._run_command(build_cmd)
        
        # Tag for registry
        registry = self.config.get('docker_registry')
        if registry:
            tag_cmd = f"docker tag {image_name} {registry}/{image_name}"
            self._run_command(tag_cmd)
        
        self._log(f"✓ Built image: {image_name}")
        return image_name
    
    def push_to_registry(self, image_name):
        """Push Docker image to registry"""
        self._log("Pushing to registry...")
        
        registry = self.config.get('docker_registry')
        if not registry:
            self._log("No registry configured, skipping push")
            return
        
        push_cmd = f"docker push {registry}/{image_name}"
        self._run_command(push_cmd)
        
        self._log("✓ Image pushed to registry")
    
    def deploy_to_kubernetes(self, image_name):
        """Deploy to Kubernetes"""
        self._log(f"Deploying to {self.environment}...")
        
        # Update deployment manifest
        deployment_file = f"k8s/{self.environment}/deployment.yaml"
        
        # Set image in deployment
        kubectl_cmd = f"""kubectl set image deployment/{self.config['app_name']} \
            {self.config['app_name']}={image_name} \
            -n {self.environment}"""
        
        self._run_command(kubectl_cmd)
        
        # Wait for rollout
        rollout_cmd = f"kubectl rollout status deployment/{self.config['app_name']} -n {self.environment}"
        self._run_command(rollout_cmd)
        
        self._log("✓ Deployment successful")
    
    def health_check(self):
        """Perform post-deployment health check"""
        self._log("Running health checks...")
        
        health_url = self.config['environments'][self.environment]['health_url']
        
        import requests
        import time
        
        max_attempts = 10
        for attempt in range(1, max_attempts + 1):
            try:
                response = requests.get(health_url, timeout=5)
                if response.status_code == 200:
                    self._log("✓ Health check passed")
                    return True
            except Exception as e:
                self._log(f"Health check attempt {attempt} failed: {e}")
            
            if attempt < max_attempts:
                time.sleep(10)
        
        self._log("✗ Health check failed", 'ERROR')
        return False
    
    def rollback(self):
        """Rollback to previous version"""
        self._log("Rolling back deployment...", 'WARNING')
        
        rollback_cmd = f"kubectl rollout undo deployment/{self.config['app_name']} -n {self.environment}"
        self._run_command(rollback_cmd)
        
        self._log("✓ Rollback completed")
    
    def send_notification(self, success):
        """Send deployment notification"""
        status = "SUCCESS" if success else "FAILED"
        message = f"""
Deployment {status}
Environment: {self.environment}
Version: {self.version}
Timestamp: {self.timestamp}
"""
        
        # Send to Slack, email, etc.
        self._log(f"Notification: {status}")
        print(message)
    
    def save_deployment_log(self):
        """Save deployment log"""
        log_file = f"deployments/deploy_{self.timestamp}.log"
        Path('deployments').mkdir(exist_ok=True)
        
        with open(log_file, 'w') as f:
            f.write('\n'.join(self.deployment_log))
        
        self._log(f"Log saved to {log_file}")
    
    def execute(self):
        """Execute full deployment pipeline"""
        success = False
        
        try:
            print("=" * 60)
            print(f"Starting Deployment Pipeline")
            print(f"Environment: {self.environment}")
            print(f"Version: {self.version}")
            print("=" * 60)
            
            # Step 1: Validate
            self.validate_environment()
            
            # Step 2: Test
            if not self.run_tests():
                raise Exception("Tests failed")
            
            # Step 3: Build
            image_name = self.build_application()
            
            # Step 4: Push
            self.push_to_registry(image_name)
            
            # Step 5: Deploy
            self.deploy_to_kubernetes(image_name)
            
            # Step 6: Health check
            if not self.health_check():
                raise Exception("Health check failed")
            
            success = True
            self._log("🎉 Deployment completed successfully!")
            
        except Exception as e:
            self._log(f"Deployment failed: {e}", 'ERROR')
            
            # Rollback on failure
            if self.config.get('auto_rollback', True):
                self.rollback()
        
        finally:
            # Always send notification and save log
            self.send_notification(success)
            self.save_deployment_log()
        
        return success

# Usage
if __name__ == '__main__':
    pipeline = DeploymentPipeline('deploy_config.json')
    success = pipeline.execute()
    sys.exit(0 if success else 1)
```

**Configuration File (deploy_config.json):**
```json
{
  "app_name": "my-web-app",
  "docker_registry": "myregistry.azurecr.io",
  "environments": ["dev", "staging", "production"],
  "test_command": "pytest tests/",
  "auto_rollback": true,
  "environments": {
    "dev": {
      "health_url": "http://dev.example.com/health"
    },
    "production": {
      "health_url": "https://example.com/health"
    }
  }
}
```

**Key Features:**
1. ✅ Automated testing
2. ✅ Docker build and push
3. ✅ Kubernetes deployment
4. ✅ Health checks
5. ✅ Automatic rollback
6. ✅ Logging and notifications
7. ✅ Environment validation

---

## Section 8: Best Practices & Patterns

### Q13: What are Python context managers and how are they used in DevOps?

**Answer:**

**Definition:**
Context managers ensure proper resource management using `with` statement.

**Basic Usage:**
```python
# Without context manager (BAD)
file = open('config.txt', 'r')
data = file.read()
file.close()  # Easy to forget!

# With context manager (GOOD)
with open('config.txt', 'r') as file:
    data = file.read()
# File automatically closed
```

**Creating Custom Context Managers:**

**Method 1: Using Class:**
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Connecting to {self.host}:{self.port}")
        self.connection = self._connect()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.connection:
            print("Closing connection")
            self.connection.close()
        
        # Return False to propagate exceptions
        return False
    
    def _connect(self):
        # Actual connection logic
        return {"connected": True}

# Usage
with DatabaseConnection('localhost', 5432) as conn:
    # Use connection
    print(f"Connected: {conn}")
# Connection automatically closed
```

**Method 2: Using @contextmanager decorator:**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Time a block of code"""
    start = time.time()
    print(f"Starting {name}...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.2f}s")

# Usage
with timer("Database backup"):
    # Backup logic
    time.sleep(2)
# Output: Database backup took 2.00s
```

**DevOps Examples:**

**1. SSH Connection Manager:**
```python
from contextlib import contextmanager
import paramiko

@contextmanager
def ssh_connection(host, username, key_file):
    """Manage SSH connection"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(host, username=username, key_filename=key_file)
        yield client
    finally:
        client.close()

# Usage
with ssh_connection('server.example.com', 'admin', '/path/to/key') as ssh:
    stdin, stdout, stderr = ssh.exec_command('uptime')
    print(stdout.read().decode())
```

**2. Temporary Directory:**
```python
import tempfile
import shutil
from pathlib import Path

@contextmanager
def temporary_directory():
    """Create and cleanup temporary directory"""
    temp_dir = tempfile.mkdtemp()
    try:
        yield Path(temp_dir)
    finally:
        shutil.rmtree(temp_dir)

# Usage
with temporary_directory() as temp_dir:
    # Work with temporary directory
    (temp_dir / 'test.txt').write_text('data')
    # Process files
# Directory automatically deleted
```

**3. Lock Manager:**
```python
import fcntl

@contextmanager
def file_lock(filename):
    """Ensure only one process runs at a time"""
    lock_file = open(f'/tmp/{filename}.lock', 'w')
    try:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    except IOError:
        raise Exception("Another instance is running")
    finally:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        lock_file.close()

# Usage
with file_lock('deployment'):
    # Only one deployment at a time
    deploy_application()
```

**4. Environment Variables:**
```python
import os

@contextmanager
def environment_variables(**kwargs):
    """Temporarily set environment variables"""
    old_environ = dict(os.environ)
    try:
        os.environ.update(kwargs)
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)

# Usage
with environment_variables(AWS_REGION='us-east-1', DEBUG='true'):
    # Code runs with these env vars
    run_aws_command()
# Original env vars restored
```

**Why Use Context Managers:**
- ✅ Automatic cleanup
- ✅ Exception safe
- ✅ Cleaner code
- ✅ Resource management
- ✅ Prevents leaks

---

## Quick Reference: Common Interview Topics

### Python Basics
- ✅ Data types and structures
- ✅ List vs Tuple vs Set vs Dict
- ✅ List comprehensions
- ✅ Decorators
- ✅ Context managers
- ✅ Generators vs Iterators

### File & I/O
- ✅ Reading large files
- ✅ File modes (r, w, a, x)
- ✅ Context managers
- ✅ JSON/YAML parsing
- ✅ Log file processing

### Error Handling
- ✅ try/except/else/finally
- ✅ Exception hierarchy
- ✅ Custom exceptions
- ✅ Logging vs print

### APIs & Networking
- ✅ requests library
- ✅ Rate limiting
- ✅ Authentication
- ✅ Error handling
- ✅ Async requests

### DevOps Tools
- ✅ boto3 (AWS)
- ✅ Docker SDK
- ✅ Kubernetes client
- ✅ subprocess module
- ✅ os and pathlib

### Concurrency
- ✅ Threading vs Multiprocessing
- ✅ asyncio
- ✅ GIL understanding
- ✅ When to use what

### Best Practices
- ✅ Virtual environments
- ✅ requirements.txt
- ✅ Logging
- ✅ Testing (pytest)
- ✅ Code organization

---

## Interview Tips

1. **Explain your thinking** - Talk through your approach
2. **Ask clarifying questions** - Understand requirements
3. **Consider edge cases** - What could go wrong?
4. **Discuss trade-offs** - Why choose one approach over another
5. **Write clean code** - Even in interviews
6. **Test your code** - Walk through examples
7. **Know the basics** - Data structures, algorithms
8. **Real-world experience** - Share actual projects
9. **Stay current** - Know modern Python features
10. **Practice coding** - Use platforms like LeetCode, HackerRank

---

**Good luck with your interviews! 🎯**
