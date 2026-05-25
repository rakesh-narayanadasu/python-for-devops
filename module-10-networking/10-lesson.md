# Module 10: Networking Basics for DevOps

## 📖 What You'll Learn
- Socket programming basics
- Port scanning
- HTTP status codes
- Network connectivity checks
- Basic network automation

---

## 1. Socket Basics

### Concept Explanation

Sockets are endpoints for network communication.

### Code Example

```python
import socket

# Get hostname and IP
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP: {ip_address}")

# Resolve domain to IP
ip = socket.gethostbyname('google.com')
print(f"Google IP: {ip}")

# Check if port is open
def is_port_open(host, port, timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

print(f"Port 80 open: {is_port_open('google.com', 80)}")
print(f"Port 9999 open: {is_port_open('google.com', 9999)}")
```

---

## 2. Port Scanning

### Code Example

```python
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Check if a port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_ports(host, ports):
    """Scan multiple ports"""
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(host, p), ports)
        open_ports = [p for p in results if p is not None]
    return open_ports

# Scan common ports
common_ports = [21, 22, 23, 25, 80, 443, 3306, 5432, 8080]
open_ports = scan_ports('localhost', common_ports)
print(f"Open ports: {open_ports}")
```

---

## 3. HTTP Status Codes

### Code Example

```python
import requests

def check_url_status(url):
    """Check HTTP status of URL"""
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        
        if status == 200:
            return "OK"
        elif status == 301 or status == 302:
            return "Redirect"
        elif status == 404:
            return "Not Found"
        elif status == 500:
            return "Server Error"
        elif status == 503:
            return "Service Unavailable"
        else:
            return f"Status {status}"
    except requests.RequestException as e:
        return f"Error: {e}"

urls = [
    'https://google.com',
    'https://github.com',
    'https://nonexistent-site-12345.com'
]

for url in urls:
    status = check_url_status(url)
    print(f"{url}: {status}")
```

---

## 4. Network Connectivity Checks

### Code Example

```python
import subprocess
import platform

def ping_host(host, count=4):
    """Ping a host"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    try:
        output = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        return output.returncode == 0
    except subprocess.TimeoutExpired:
        return False

# Check connectivity
hosts = ['8.8.8.8', 'google.com', '192.168.1.1']
for host in hosts:
    status = "✓ Reachable" if ping_host(host, 2) else "✗ Unreachable"
    print(f"{host}: {status}")
```

---

## 5. Real DevOps Example: Health Checker

### Code Example

```python
import requests
import socket
import time
from datetime import datetime

class ServiceHealthChecker:
    def __init__(self, services):
        self.services = services
        self.results = []
    
    def check_http(self, url):
        """Check HTTP endpoint"""
        try:
            response = requests.get(url, timeout=5)
            return {
                'status': 'healthy' if response.status_code == 200 else 'unhealthy',
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds()
            }
        except Exception as e:
            return {
                'status': 'down',
                'error': str(e)
            }
    
    def check_port(self, host, port):
        """Check if port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def run_checks(self):
        """Run all health checks"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\nHealth Check Report - {timestamp}")
        print("=" * 60)
        
        for service in self.services:
            name = service['name']
            check_type = service['type']
            
            if check_type == 'http':
                result = self.check_http(service['url'])
                status = result['status']
                print(f"{name}: {status}")
                if 'response_time' in result:
                    print(f"  Response time: {result['response_time']:.3f}s")
            
            elif check_type == 'port':
                is_open = self.check_port(service['host'], service['port'])
                status = "open" if is_open else "closed"
                print(f"{name}: Port {service['port']} is {status}")

# Usage
services = [
    {'name': 'Web Server', 'type': 'http', 'url': 'https://google.com'},
    {'name': 'API Server', 'type': 'http', 'url': 'https://api.github.com'},
    {'name': 'Database', 'type': 'port', 'host': 'localhost', 'port': 5432},
    {'name': 'Redis', 'type': 'port', 'host': 'localhost', 'port': 6379}
]

checker = ServiceHealthChecker(services)
checker.run_checks()
```

---

## 📝 Key Takeaways

✅ **Socket programming** - Low-level network communication
✅ **Port scanning** - Check service availability
✅ **HTTP checks** - Monitor web services
✅ **Ping tests** - Basic connectivity
✅ **Timeouts** - Always set timeouts
✅ **Error handling** - Network operations can fail

---

## Next Module

Ready for **Module 11: Cloud & DevOps Tools**? 🎯
