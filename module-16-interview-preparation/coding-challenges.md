# Python DevOps Coding Challenges

## 🎯 Practical Coding Problems for Interviews

These are real-world coding challenges you might encounter in DevOps interviews.

---

## Challenge 1: Log Parser

**Problem:**
Write a function that parses a log file and returns statistics about log levels.

**Input:**
```
2024-01-30 10:15:23 INFO Application started
2024-01-30 10:15:24 ERROR Database connection failed
2024-01-30 10:15:25 WARNING High memory usage
2024-01-30 10:15:26 INFO Request processed
2024-01-30 10:15:27 ERROR Timeout occurred
```

**Expected Output:**
```python
{
    'INFO': 2,
    'ERROR': 2,
    'WARNING': 1,
    'total': 5
}
```

**Solution:**
```python
def parse_log_file(filename):
    """Parse log file and return statistics"""
    stats = {}
    total = 0
    
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                level = parts[2]
                stats[level] = stats.get(level, 0) + 1
                total += 1
    
    stats['total'] = total
    return stats

# Alternative using Counter
from collections import Counter
import re

def parse_log_file_v2(filename):
    """Parse using regex and Counter"""
    levels = []
    
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (\w+)', line)
            if match:
                levels.append(match.group(1))
    
    stats = dict(Counter(levels))
    stats['total'] = len(levels)
    return stats
```

**Follow-up Questions:**
1. How would you handle very large log files?
2. How would you parse logs in real-time?
3. How would you handle different log formats?

---

## Challenge 2: Server Health Monitor

**Problem:**
Create a class that monitors multiple servers and reports their health status.

**Requirements:**
- Check HTTP endpoints
- Check port availability
- Track response times
- Alert on failures

**Solution:**
```python
import requests
import socket
import time
from datetime import datetime

class ServerHealthMonitor:
    def __init__(self, servers):
        self.servers = servers
        self.results = []
    
    def check_http_endpoint(self, url, timeout=5):
        """Check HTTP endpoint health"""
        try:
            start = time.time()
            response = requests.get(url, timeout=timeout)
            elapsed = time.time() - start
            
            return {
                'status': 'healthy' if response.status_code == 200 else 'unhealthy',
                'status_code': response.status_code,
                'response_time': round(elapsed, 3),
                'timestamp': datetime.now().isoformat()
            }
        except requests.Timeout:
            return {'status': 'timeout', 'error': 'Request timed out'}
        except requests.ConnectionError:
            return {'status': 'unreachable', 'error': 'Connection failed'}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def check_port(self, host, port, timeout=3):
        """Check if port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            
            return {
                'status': 'open' if result == 0 else 'closed',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def run_health_checks(self):
        """Run all configured health checks"""
        results = []
        
        for server in self.servers:
            server_result = {
                'name': server['name'],
                'checks': []
            }
            
            # HTTP check
            if 'url' in server:
                http_result = self.check_http_endpoint(server['url'])
                server_result['checks'].append({
                    'type': 'http',
                    'result': http_result
                })
            
            # Port check
            if 'host' in server and 'port' in server:
                port_result = self.check_port(server['host'], server['port'])
                server_result['checks'].append({
                    'type': 'port',
                    'result': port_result
                })
            
            results.append(server_result)
        
        self.results = results
        return results
    
    def get_unhealthy_servers(self):
        """Get list of unhealthy servers"""
        unhealthy = []
        
        for server in self.results:
            for check in server['checks']:
                if check['result']['status'] not in ['healthy', 'open']:
                    unhealthy.append({
                        'name': server['name'],
                        'check_type': check['type'],
                        'status': check['result']['status']
                    })
        
        return unhealthy
    
    def generate_report(self):
        """Generate health check report"""
        report = ["=" * 60]
        report.append("SERVER HEALTH CHECK REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        for server in self.results:
            report.append(f"\n{server['name']}:")
            for check in server['checks']:
                result = check['result']
                status_icon = "✓" if result['status'] in ['healthy', 'open'] else "✗"
                report.append(f"  {status_icon} {check['type']}: {result['status']}")
                if 'response_time' in result:
                    report.append(f"    Response time: {result['response_time']}s")
        
        return "\n".join(report)

# Usage
servers = [
    {'name': 'Web Server', 'url': 'https://google.com'},
    {'name': 'API Server', 'url': 'https://api.github.com'},
    {'name': 'Database', 'host': 'localhost', 'port': 5432}
]

monitor = ServerHealthMonitor(servers)
monitor.run_health_checks()
print(monitor.generate_report())

unhealthy = monitor.get_unhealthy_servers()
if unhealthy:
    print("\n⚠ ALERTS:")
    for server in unhealthy:
        print(f"  - {server['name']}: {server['status']}")
```

---

## Challenge 3: Configuration File Merger

**Problem:**
Merge multiple YAML configuration files with proper override logic.

**Input Files:**

`base.yaml`:
```yaml
database:
  host: localhost
  port: 5432
  name: myapp

server:
  port: 8080
  workers: 4
```

`production.yaml`:
```yaml
database:
  host: prod-db.example.com
  ssl: true

server:
  workers: 8
```

**Expected Output:**
```yaml
database:
  host: prod-db.example.com  # Overridden
  port: 5432                 # From base
  name: myapp                # From base
  ssl: true                  # New in production

server:
  port: 8080                 # From base
  workers: 8                 # Overridden
```

**Solution:**
```python
import yaml
from pathlib import Path

def deep_merge(base, override):
    """Deep merge two dictionaries"""
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    
    return result

def merge_config_files(*files):
    """Merge multiple YAML config files"""
    merged = {}
    
    for file in files:
        with open(file, 'r') as f:
            config = yaml.safe_load(f) or {}
            merged = deep_merge(merged, config)
    
    return merged

def load_environment_config(base_file, env):
    """Load base config and merge with environment-specific config"""
    configs = [base_file]
    
    env_file = f"{env}.yaml"
    if Path(env_file).exists():
        configs.append(env_file)
    
    return merge_config_files(*configs)

# Usage
config = merge_config_files('base.yaml', 'production.yaml')
print(yaml.dump(config, default_flow_style=False))

# Or load by environment
prod_config = load_environment_config('base.yaml', 'production')
```

---

## Challenge 4: Deployment Rollback System

**Problem:**
Implement a deployment system with rollback capability.

**Requirements:**
- Track deployment history
- Support rollback to any previous version
- Validate before deployment
- Handle failures gracefully

**Solution:**
```python
import json
from datetime import datetime
from pathlib import Path

class DeploymentManager:
    def __init__(self, app_name, history_file='deployment_history.json'):
        self.app_name = app_name
        self.history_file = history_file
        self.history = self._load_history()
    
    def _load_history(self):
        """Load deployment history"""
        if Path(self.history_file).exists():
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_history(self):
        """Save deployment history"""
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def deploy(self, version, environment):
        """Deploy new version"""
        print(f"Deploying {self.app_name} v{version} to {environment}")
        
        # Validate
        if not self._validate_version(version):
            raise ValueError(f"Invalid version: {version}")
        
        # Get current version before deployment
        current = self.get_current_version(environment)
        
        try:
            # Perform deployment
            self._perform_deployment(version, environment)
            
            # Record successful deployment
            deployment_record = {
                'version': version,
                'environment': environment,
                'timestamp': datetime.now().isoformat(),
                'status': 'success',
                'previous_version': current
            }
            self.history.append(deployment_record)
            self._save_history()
            
            print(f"✓ Deployment successful")
            return True
            
        except Exception as e:
            print(f"✗ Deployment failed: {e}")
            
            # Record failed deployment
            deployment_record = {
                'version': version,
                'environment': environment,
                'timestamp': datetime.now().isoformat(),
                'status': 'failed',
                'error': str(e),
                'previous_version': current
            }
            self.history.append(deployment_record)
            self._save_history()
            
            return False
    
    def rollback(self, environment, target_version=None):
        """Rollback to previous or specific version"""
        current = self.get_current_version(environment)
        
        if not current:
            print("No deployment to rollback from")
            return False
        
        # Determine target version
        if target_version is None:
            # Rollback to previous version
            target_version = self._get_previous_version(environment)
        
        if not target_version:
            print("No previous version found")
            return False
        
        print(f"Rolling back from v{current} to v{target_version}")
        
        try:
            self._perform_deployment(target_version, environment)
            
            rollback_record = {
                'version': target_version,
                'environment': environment,
                'timestamp': datetime.now().isoformat(),
                'status': 'rollback',
                'from_version': current
            }
            self.history.append(rollback_record)
            self._save_history()
            
            print(f"✓ Rollback successful")
            return True
            
        except Exception as e:
            print(f"✗ Rollback failed: {e}")
            return False
    
    def get_current_version(self, environment):
        """Get currently deployed version"""
        for record in reversed(self.history):
            if (record['environment'] == environment and 
                record['status'] in ['success', 'rollback']):
                return record['version']
        return None
    
    def _get_previous_version(self, environment):
        """Get previous deployed version"""
        versions = []
        for record in self.history:
            if (record['environment'] == environment and 
                record['status'] in ['success', 'rollback']):
                versions.append(record['version'])
        
        return versions[-2] if len(versions) >= 2 else None
    
    def _validate_version(self, version):
        """Validate version format"""
        import re
        pattern = r'^\d+\.\d+\.\d+$'
        return bool(re.match(pattern, version))
    
    def _perform_deployment(self, version, environment):
        """Actual deployment logic (placeholder)"""
        # In real implementation:
        # - Update Kubernetes deployment
        # - Restart services
        # - Run health checks
        print(f"  Deploying version {version}...")
        import time
        time.sleep(1)  # Simulate deployment
    
    def get_deployment_history(self, environment=None, limit=10):
        """Get deployment history"""
        history = self.history
        
        if environment:
            history = [h for h in history if h['environment'] == environment]
        
        return history[-limit:]
    
    def print_history(self, environment=None):
        """Print deployment history"""
        history = self.get_deployment_history(environment)
        
        print("\nDeployment History:")
        print("=" * 80)
        
        for record in reversed(history):
            status_icon = "✓" if record['status'] == 'success' else "↩" if record['status'] == 'rollback' else "✗"
            print(f"{status_icon} v{record['version']} to {record['environment']} - {record['timestamp']}")
            if record['status'] == 'rollback':
                print(f"  Rolled back from v{record.get('from_version')}")

# Usage
manager = DeploymentManager('my-web-app')

# Deploy new version
manager.deploy('1.0.0', 'production')
manager.deploy('1.1.0', 'production')
manager.deploy('1.2.0', 'production')

# Show history
manager.print_history('production')

# Rollback to previous version
manager.rollback('production')

# Rollback to specific version
manager.rollback('production', target_version='1.0.0')
```

---

## Challenge 5: API Rate Limiter

**Problem:**
Implement a rate limiter that allows maximum N requests per time window.

**Requirements:**
- Sliding window algorithm
- Thread-safe
- Configurable limits
- Can be used as decorator

**Solution:**
```python
import time
import threading
from collections import deque
from functools import wraps

class RateLimiter:
    def __init__(self, max_calls, time_window):
        """
        max_calls: Maximum number of calls allowed
        time_window: Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
        self.lock = threading.Lock()
    
    def __call__(self, func):
        """Use as decorator"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.wait_if_needed()
            return func(*args, **kwargs)
        return wrapper
    
    def wait_if_needed(self):
        """Wait if rate limit is exceeded"""
        with self.lock:
            now = time.time()
            
            # Remove calls outside the time window
            while self.calls and self.calls[0] < now - self.time_window:
                self.calls.popleft()
            
            # Check if we need to wait
            if len(self.calls) >= self.max_calls:
                sleep_time = self.time_window - (now - self.calls[0])
                if sleep_time > 0:
                    print(f"Rate limit reached. Waiting {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
                    self.calls.popleft()
            
            # Record this call
            self.calls.append(time.time())
    
    def get_remaining_calls(self):
        """Get number of remaining calls in current window"""
        with self.lock:
            now = time.time()
            
            # Remove old calls
            while self.calls and self.calls[0] < now - self.time_window:
                self.calls.popleft()
            
            return self.max_calls - len(self.calls)

# Usage Example 1: As decorator
rate_limiter = RateLimiter(max_calls=5, time_window=10)

@rate_limiter
def call_api(endpoint):
    print(f"Calling {endpoint} at {time.time():.2f}")
    return f"Response from {endpoint}"

# Make 10 calls - will be rate limited
for i in range(10):
    result = call_api(f"/api/endpoint/{i}")
    print(f"  Remaining calls: {rate_limiter.get_remaining_calls()}")

# Usage Example 2: Manual usage
class APIClient:
    def __init__(self):
        self.rate_limiter = RateLimiter(max_calls=10, time_window=60)
    
    def make_request(self, url):
        self.rate_limiter.wait_if_needed()
        # Make actual request
        import requests
        return requests.get(url)

# Usage Example 3: Per-endpoint rate limiting
class MultiEndpointRateLimiter:
    def __init__(self):
        self.limiters = {}
    
    def get_limiter(self, endpoint, max_calls, time_window):
        """Get or create rate limiter for endpoint"""
        if endpoint not in self.limiters:
            self.limiters[endpoint] = RateLimiter(max_calls, time_window)
        return self.limiters[endpoint]
    
    def call(self, endpoint, func, *args, **kwargs):
        """Call function with rate limiting"""
        limiter = self.get_limiter(endpoint, max_calls=5, time_window=10)
        limiter.wait_if_needed()
        return func(*args, **kwargs)

# Advanced: Token bucket algorithm
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        """
        capacity: Maximum number of tokens
        refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = threading.Lock()
    
    def consume(self, tokens=1):
        """Try to consume tokens"""
        with self.lock:
            self._refill()
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False
    
    def wait_and_consume(self, tokens=1):
        """Wait until tokens available and consume"""
        while not self.consume(tokens):
            time.sleep(0.1)
    
    def _refill(self):
        """Refill tokens based on time elapsed"""
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

# Usage
bucket = TokenBucket(capacity=10, refill_rate=2)  # 2 tokens per second

for i in range(15):
    bucket.wait_and_consume()
    print(f"Request {i+1} processed")
```

---

## Challenge 6: Concurrent File Processor

**Problem:**
Process multiple large files concurrently and aggregate results.

**Requirements:**
- Process files in parallel
- Handle errors gracefully
- Aggregate results
- Show progress

**Solution:**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from pathlib import Path

class ConcurrentFileProcessor:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
        self.results = []
    
    def process_file(self, filepath):
        """Process a single file"""
        try:
            print(f"Processing {filepath}...")
            
            stats = {
                'file': str(filepath),
                'lines': 0,
                'errors': 0,
                'warnings': 0,
                'size': filepath.stat().st_size
            }
            
            with open(filepath, 'r') as f:
                for line in f:
                    stats['lines'] += 1
                    if 'ERROR' in line:
                        stats['errors'] += 1
                    elif 'WARNING' in line:
                        stats['warnings'] += 1
            
            stats['status'] = 'success'
            return stats
            
        except Exception as e:
            return {
                'file': str(filepath),
                'status': 'failed',
                'error': str(e)
            }
    
    def process_files(self, file_list):
        """Process multiple files concurrently"""
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(self.process_file, f): f 
                for f in file_list
            }
            
            # Process completed tasks
            completed = 0
            total = len(file_list)
            
            for future in as_completed(future_to_file):
                filepath = future_to_file[future]
                completed += 1
                
                try:
                    result = future.result()
                    results.append(result)
                    print(f"[{completed}/{total}] Completed {filepath}")
                except Exception as e:
                    print(f"[{completed}/{total}] Failed {filepath}: {e}")
                    results.append({
                        'file': str(filepath),
                        'status': 'failed',
                        'error': str(e)
                    })
        
        self.results = results
        return results
    
    def aggregate_results(self):
        """Aggregate results from all files"""
        total_stats = {
            'total_files': len(self.results),
            'successful': 0,
            'failed': 0,
            'total_lines': 0,
            'total_errors': 0,
            'total_warnings': 0,
            'total_size': 0
        }
        
        for result in self.results:
            if result['status'] == 'success':
                total_stats['successful'] += 1
                total_stats['total_lines'] += result['lines']
                total_stats['total_errors'] += result['errors']
                total_stats['total_warnings'] += result['warnings']
                total_stats['total_size'] += result['size']
            else:
                total_stats['failed'] += 1
        
        return total_stats
    
    def generate_report(self):
        """Generate processing report"""
        stats = self.aggregate_results()
        
        report = ["=" * 60]
        report.append("FILE PROCESSING REPORT")
        report.append("=" * 60)
        report.append(f"Total files: {stats['total_files']}")
        report.append(f"Successful: {stats['successful']}")
        report.append(f"Failed: {stats['failed']}")
        report.append(f"Total lines: {stats['total_lines']:,}")
        report.append(f"Total errors: {stats['total_errors']:,}")
        report.append(f"Total warnings: {stats['total_warnings']:,}")
        report.append(f"Total size: {stats['total_size']:,} bytes")
        
        return "\n".join(report)

# Usage
processor = ConcurrentFileProcessor(max_workers=4)

# Get all log files
log_files = list(Path('.').glob('*.log'))

# Process files
results = processor.process_files(log_files)

# Show report
print("\n" + processor.generate_report())

# Show individual results
print("\nIndividual Results:")
for result in results:
    if result['status'] == 'success':
        print(f"  ✓ {result['file']}: {result['errors']} errors")
    else:
        print(f"  ✗ {result['file']}: {result['error']}")
```

---

## Tips for Solving Coding Challenges

1. **Understand the problem** - Ask clarifying questions
2. **Think out loud** - Explain your approach
3. **Start simple** - Get basic solution working first
4. **Consider edge cases** - Empty inputs, errors, large data
5. **Optimize if needed** - Time and space complexity
6. **Test your code** - Walk through examples
7. **Handle errors** - Don't assume perfect inputs
8. **Write clean code** - Readable and maintainable
9. **Use appropriate data structures** - Lists, dicts, sets
10. **Know standard library** - collections, itertools, functools

---

## Common Patterns to Know

- **File processing**: Line-by-line iteration
- **API calls**: Error handling, retries, rate limiting
- **Data aggregation**: Counter, defaultdict, groupby
- **Concurrency**: ThreadPoolExecutor, multiprocessing
- **Caching**: lru_cache, custom cache
- **Validation**: Regular expressions, type checking
- **Configuration**: YAML/JSON parsing, merging
- **Monitoring**: Health checks, metrics collection

---

**Practice these challenges and you'll be well-prepared! 🚀**
