# Module 15: Final Projects

## 🎯 Capstone Projects

Apply everything you've learned by building real-world DevOps tools!

---

## Project 1: Log Analyzer Tool

### Requirements
- Read log files
- Parse different log formats
- Count errors, warnings, info
- Generate HTML/text reports
- Support filtering by date/level
- Export to JSON

### Starter Code

```python
import re
from datetime import datetime
from collections import Counter

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.entries = []
    
    def parse_log(self):
        """Parse log file"""
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)'
        
        with open(self.log_file, 'r') as f:
            for line in f:
                match = re.match(pattern, line)
                if match:
                    timestamp, level, message = match.groups()
                    self.entries.append({
                        'timestamp': timestamp,
                        'level': level,
                        'message': message
                    })
    
    def get_statistics(self):
        """Get log statistics"""
        levels = [entry['level'] for entry in self.entries]
        return dict(Counter(levels))
    
    def filter_by_level(self, level):
        """Filter logs by level"""
        return [e for e in self.entries if e['level'] == level]
    
    def generate_report(self):
        """Generate text report"""
        stats = self.get_statistics()
        report = "LOG ANALYSIS REPORT\n"
        report += "=" * 50 + "\n"
        report += f"Total entries: {len(self.entries)}\n\n"
        
        for level, count in stats.items():
            report += f"{level}: {count}\n"
        
        return report

# Usage
analyzer = LogAnalyzer('app.log')
analyzer.parse_log()
print(analyzer.generate_report())
```

---

## Project 2: Server Health Checker

### Requirements
- Check multiple servers
- HTTP endpoint monitoring
- Port scanning
- Response time tracking
- Alert on failures
- Generate status dashboard
- Save history

### Starter Code

```python
import requests
import socket
from datetime import datetime

class HealthChecker:
    def __init__(self, servers):
        self.servers = servers
        self.results = []
    
    def check_http(self, url):
        """Check HTTP endpoint"""
        try:
            start = datetime.now()
            response = requests.get(url, timeout=5)
            elapsed = (datetime.now() - start).total_seconds()
            
            return {
                'status': 'up' if response.status_code == 200 else 'down',
                'status_code': response.status_code,
                'response_time': elapsed
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
        for server in self.servers:
            result = {
                'name': server['name'],
                'timestamp': datetime.now().isoformat()
            }
            
            if 'url' in server:
                result.update(self.check_http(server['url']))
            elif 'host' in server and 'port' in server:
                is_open = self.check_port(server['host'], server['port'])
                result['status'] = 'up' if is_open else 'down'
            
            self.results.append(result)
        
        return self.results
    
    def print_report(self):
        """Print health check report"""
        print("\nHEALTH CHECK REPORT")
        print("=" * 60)
        
        for result in self.results:
            status_icon = "✓" if result['status'] == 'up' else "✗"
            print(f"{status_icon} {result['name']}: {result['status']}")
            if 'response_time' in result:
                print(f"  Response time: {result['response_time']:.3f}s")

# Usage
servers = [
    {'name': 'Google', 'url': 'https://google.com'},
    {'name': 'GitHub', 'url': 'https://github.com'},
    {'name': 'Local DB', 'host': 'localhost', 'port': 5432}
]

checker = HealthChecker(servers)
checker.run_checks()
checker.print_report()
```

---

## Project 3: Automated Deployment Script

### Requirements
- Pre-deployment checks
- Run tests
- Build application
- Deploy to multiple environments
- Rollback capability
- Notification system
- Deployment history

### Starter Code

```python
import subprocess
import sys
from datetime import datetime

class DeploymentPipeline:
    def __init__(self, environment, version):
        self.environment = environment
        self.version = version
        self.timestamp = datetime.now()
        self.success = False
    
    def validate_environment(self):
        """Validate deployment environment"""
        valid_envs = ['dev', 'staging', 'production']
        if self.environment not in valid_envs:
            raise ValueError(f"Invalid environment: {self.environment}")
        return True
    
    def run_tests(self):
        """Run test suite"""
        print("Running tests...")
        result = subprocess.run(['pytest'], capture_output=True)
        if result.returncode != 0:
            print("❌ Tests failed")
            return False
        print("✅ Tests passed")
        return True
    
    def build(self):
        """Build application"""
        print("Building application...")
        # Add your build commands here
        print("✅ Build complete")
        return True
    
    def deploy(self):
        """Deploy to environment"""
        print(f"Deploying to {self.environment}...")
        # Add your deployment commands here
        print("✅ Deployment complete")
        return True
    
    def rollback(self):
        """Rollback deployment"""
        print("Rolling back...")
        # Add rollback logic here
        print("✅ Rollback complete")
    
    def notify(self, message):
        """Send notification"""
        print(f"📢 {message}")
        # Add Slack/email notification here
    
    def execute(self):
        """Execute deployment pipeline"""
        try:
            print(f"\n🚀 Starting deployment to {self.environment}")
            print("=" * 60)
            
            self.validate_environment()
            
            if not self.run_tests():
                self.notify("Deployment aborted: Tests failed")
                return False
            
            if not self.build():
                self.notify("Deployment aborted: Build failed")
                return False
            
            if not self.deploy():
                self.notify("Deployment failed, rolling back")
                self.rollback()
                return False
            
            self.success = True
            self.notify(f"Deployment to {self.environment} successful!")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.notify(f"Deployment error: {e}")
            return False

# Usage
if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    version = sys.argv[2] if len(sys.argv) > 2 else '1.0.0'
    
    pipeline = DeploymentPipeline(env, version)
    success = pipeline.execute()
    sys.exit(0 if success else 1)
```

---

## Project 4: API Monitoring Tool

### Requirements
- Monitor multiple APIs
- Track response times
- Check status codes
- Alert on failures
- Store metrics
- Generate graphs
- API uptime calculation

### Starter Code

```python
import requests
import time
from datetime import datetime
import json

class APIMonitor:
    def __init__(self, apis):
        self.apis = apis
        self.metrics = []
    
    def check_api(self, api):
        """Check single API endpoint"""
        try:
            start = time.time()
            response = requests.get(api['url'], timeout=api.get('timeout', 10))
            elapsed = time.time() - start
            
            return {
                'name': api['name'],
                'url': api['url'],
                'status_code': response.status_code,
                'response_time': elapsed,
                'success': response.status_code == 200,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'name': api['name'],
                'url': api['url'],
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def monitor(self, interval=60, duration=None):
        """Monitor APIs at regular intervals"""
        start_time = time.time()
        
        while True:
            for api in self.apis:
                result = self.check_api(api)
                self.metrics.append(result)
                
                if not result['success']:
                    self.alert(result)
            
            self.save_metrics()
            
            if duration and (time.time() - start_time) >= duration:
                break
            
            time.sleep(interval)
    
    def alert(self, result):
        """Send alert for failed check"""
        print(f"🚨 ALERT: {result['name']} is down!")
        print(f"   URL: {result['url']}")
        if 'error' in result:
            print(f"   Error: {result['error']}")
    
    def save_metrics(self):
        """Save metrics to file"""
        with open('api_metrics.json', 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def calculate_uptime(self, api_name):
        """Calculate uptime percentage"""
        api_metrics = [m for m in self.metrics if m['name'] == api_name]
        if not api_metrics:
            return 0
        
        successful = sum(1 for m in api_metrics if m['success'])
        return (successful / len(api_metrics)) * 100

# Usage
apis = [
    {'name': 'GitHub API', 'url': 'https://api.github.com'},
    {'name': 'Google', 'url': 'https://google.com'},
]

monitor = APIMonitor(apis)
# Run for 5 minutes, check every 30 seconds
monitor.monitor(interval=30, duration=300)
```

---

## 🎓 Congratulations!

You've completed the Python for DevOps course! You now have the skills to:

✅ Write Python scripts for automation
✅ Handle files, APIs, and system operations
✅ Build CI/CD pipelines
✅ Monitor and log applications
✅ Test and debug code
✅ Create production-ready DevOps tools

## 🚀 Next Steps

1. **Build your own projects** - Apply what you learned
2. **Contribute to open source** - DevOps tools on GitHub
3. **Automate your work** - Start small, grow gradually
4. **Keep learning** - Python ecosystem is vast
5. **Share your knowledge** - Help others learn

## 📚 Additional Resources

- Python documentation: https://docs.python.org
- Real Python: https://realpython.com
- DevOps subreddit: r/devops
- Python DevOps books and courses

**Happy automating! 🎉**
