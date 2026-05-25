# Module 9: JSON, YAML & APIs

## 📖 What You'll Learn
- Working with JSON data
- Parsing and generating YAML
- Making HTTP requests
- REST API integration
- API authentication

---

## 1. JSON (JavaScript Object Notation)

### Concept Explanation

JSON is a lightweight data format used everywhere in DevOps:
- API responses
- Configuration files
- Docker configs
- Kubernetes manifests
- CI/CD pipelines

### Code Example

```python
import json

# Python dict to JSON string
server = {
    "name": "web-01",
    "ip": "192.168.1.10",
    "port": 80,
    "services": ["nginx", "app"],
    "active": True
}

json_string = json.dumps(server)
print(json_string)
# {"name": "web-01", "ip": "192.168.1.10", ...}

# Pretty print JSON
json_pretty = json.dumps(server, indent=2)
print(json_pretty)

# JSON string to Python dict
json_data = '{"name": "web-01", "port": 80}'
server = json.loads(json_data)
print(server["name"])  # web-01

# Write JSON to file
with open('config.json', 'w') as f:
    json.dump(server, f, indent=2)

# Read JSON from file
with open('config.json', 'r') as f:
    config = json.load(f)

# Real DevOps example: Parse API response
api_response = '''
{
  "servers": [
    {"name": "web-01", "status": "running", "cpu": 45},
    {"name": "web-02", "status": "running", "cpu": 78}
  ],
  "total": 2
}
'''

data = json.loads(api_response)
for server in data["servers"]:
    print(f"{server['name']}: CPU {server['cpu']}%")
```

---

## 2. YAML (YAML Ain't Markup Language)

### Concept Explanation

YAML is human-readable and widely used in DevOps:
- Kubernetes manifests
- Ansible playbooks
- Docker Compose
- CI/CD configs (GitHub Actions, GitLab CI)

### Code Example

```python
import yaml  # pip install pyyaml

# Python dict to YAML
config = {
    "server": {
        "host": "localhost",
        "port": 8080,
        "ssl": True
    },
    "database": {
        "host": "db.example.com",
        "port": 5432,
        "name": "myapp"
    },
    "services": ["web", "api", "worker"]
}

yaml_string = yaml.dump(config, default_flow_style=False)
print(yaml_string)

# Write YAML to file
with open('config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

# Read YAML from file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

print(config["server"]["host"])  # localhost

# Real DevOps example: Kubernetes manifest
k8s_manifest = """
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
"""

pod = yaml.safe_load(k8s_manifest)
print(f"Pod name: {pod['metadata']['name']}")
print(f"Image: {pod['spec']['containers'][0]['image']}")
```

---

## 3. Making HTTP Requests

### Concept Explanation

The `requests` library makes HTTP requests simple.

### Code Example

```python
import requests  # pip install requests

# GET request
response = requests.get('https://api.github.com')
print(f"Status: {response.status_code}")
print(f"Content: {response.text[:100]}")

# GET with parameters
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', 
                       params=params)
data = response.json()  # Parse JSON response

# POST request
data = {"name": "web-01", "status": "running"}
response = requests.post('https://api.example.com/servers', 
                        json=data)

# PUT request (update)
data = {"status": "stopped"}
response = requests.put('https://api.example.com/servers/web-01', 
                       json=data)

# DELETE request
response = requests.delete('https://api.example.com/servers/web-01')

# Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'DevOps-Script/1.0'
}
response = requests.get('https://api.example.com', headers=headers)

# Timeout
try:
    response = requests.get('https://api.example.com', timeout=5)
except requests.Timeout:
    print("Request timed out")

# Check response
response = requests.get('https://api.example.com')
if response.status_code == 200:
    print("Success!")
    data = response.json()
elif response.status_code == 404:
    print("Not found")
else:
    print(f"Error: {response.status_code}")
```

---

## 4. REST API Integration

### Code Example

```python
import requests

class ServerAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def get_servers(self):
        """Get list of all servers"""
        response = requests.get(
            f'{self.base_url}/servers',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def get_server(self, server_id):
        """Get specific server details"""
        response = requests.get(
            f'{self.base_url}/servers/{server_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def create_server(self, name, size, region):
        """Create new server"""
        data = {
            'name': name,
            'size': size,
            'region': region
        }
        response = requests.post(
            f'{self.base_url}/servers',
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
    
    def delete_server(self, server_id):
        """Delete server"""
        response = requests.delete(
            f'{self.base_url}/servers/{server_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return True

# Usage
api = ServerAPI('https://api.example.com/v1', 'your_api_key')

# List servers
servers = api.get_servers()
for server in servers:
    print(f"{server['name']}: {server['status']}")

# Create server
new_server = api.create_server('web-03', 'medium', 'us-east')
print(f"Created: {new_server['id']}")
```

---

## 5. Real DevOps Examples

### Example 1: GitHub API

```python
import requests

def get_repo_info(owner, repo):
    """Get GitHub repository information"""
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'stars': data['stargazers_count'],
            'forks': data['forks_count'],
            'language': data['language'],
            'open_issues': data['open_issues_count']
        }
    return None

info = get_repo_info('kubernetes', 'kubernetes')
print(f"Stars: {info['stars']}")
```

### Example 2: Docker Hub API

```python
import requests

def search_docker_images(query):
    """Search Docker Hub for images"""
    url = 'https://hub.docker.com/v2/search/repositories/'
    params = {'query': query}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for item in data['results'][:5]:
        results.append({
            'name': item['repo_name'],
            'description': item['short_description'],
            'stars': item['star_count']
        })
    
    return results

images = search_docker_images('nginx')
for img in images:
    print(f"{img['name']}: {img['stars']} stars")
```

### Example 3: Slack Webhook

```python
import requests

def send_slack_notification(webhook_url, message):
    """Send notification to Slack"""
    data = {
        'text': message,
        'username': 'DevOps Bot',
        'icon_emoji': ':robot_face:'
    }
    
    response = requests.post(webhook_url, json=data)
    return response.status_code == 200

# Usage
webhook = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
send_slack_notification(webhook, 'Deployment completed successfully!')
```

### Example 4: Monitoring API

```python
import requests
import time

def monitor_endpoint(url, interval=60, max_failures=3):
    """Monitor endpoint and alert on failures"""
    failures = 0
    
    while True:
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✓ {url} is healthy")
                failures = 0
            else:
                failures += 1
                print(f"✗ {url} returned {response.status_code}")
                
                if failures >= max_failures:
                    send_alert(f"{url} is down!")
                    
        except requests.RequestException as e:
            failures += 1
            print(f"✗ Error connecting to {url}: {e}")
            
            if failures >= max_failures:
                send_alert(f"{url} is unreachable!")
        
        time.sleep(interval)

def send_alert(message):
    """Send alert (email, Slack, etc.)"""
    print(f"🚨 ALERT: {message}")
    # Implement actual alerting here
```

---

## 📝 Key Takeaways

✅ **JSON for APIs** - Universal data format
✅ **YAML for configs** - Human-readable
✅ **requests library** - Simple HTTP client
✅ **Handle errors** - Network can fail
✅ **Use timeouts** - Don't hang forever
✅ **Authentication** - API keys, tokens
✅ **Rate limiting** - Respect API limits

---

## 🚀 Practice Challenge

Create a GitHub repository monitor:
1. Use GitHub API
2. Check repository stats
3. Monitor open issues
4. Save data to JSON file
5. Send alert if issues > threshold

---

## Next Module

Ready for **Module 10: Networking Basics**? Learn network programming! 🎯
