# Module 12: CI/CD & Automation

## 📖 What You'll Learn
- CI/CD pipeline concepts
- GitHub Actions integration
- Jenkins automation
- Deployment automation scripts

---

## 1. CI/CD Concepts

### Continuous Integration
- Automated testing on code changes
- Build automation
- Code quality checks

### Continuous Deployment
- Automated deployment to environments
- Rollback capabilities
- Zero-downtime deployments

---

## 2. GitHub Actions Integration

### Code Example

```python
# generate_github_workflow.py
import yaml

def create_ci_workflow(project_name, python_version='3.9'):
    """Generate GitHub Actions workflow"""
    workflow = {
        'name': 'CI',
        'on': ['push', 'pull_request'],
        'jobs': {
            'test': {
                'runs-on': 'ubuntu-latest',
                'steps': [
                    {'uses': 'actions/checkout@v2'},
                    {
                        'name': 'Set up Python',
                        'uses': 'actions/setup-python@v2',
                        'with': {'python-version': python_version}
                    },
                    {
                        'name': 'Install dependencies',
                        'run': 'pip install -r requirements.txt'
                    },
                    {
                        'name': 'Run tests',
                        'run': 'pytest'
                    }
                ]
            }
        }
    }
    
    with open('.github/workflows/ci.yml', 'w') as f:
        yaml.dump(workflow, f, default_flow_style=False)

create_ci_workflow('my-project')
```

---

## 3. Deployment Automation

### Code Example

```python
import subprocess
import sys
from datetime import datetime

class DeploymentManager:
    def __init__(self, environment):
        self.environment = environment
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    def run_tests(self):
        """Run test suite"""
        print("Running tests...")
        result = subprocess.run(['pytest'], capture_output=True)
        if result.returncode != 0:
            print("❌ Tests failed!")
            return False
        print("✅ Tests passed")
        return True
    
    def build(self):
        """Build application"""
        print("Building application...")
        result = subprocess.run(['docker', 'build', '-t', 'myapp', '.'])
        return result.returncode == 0
    
    def deploy(self):
        """Deploy to environment"""
        print(f"Deploying to {self.environment}...")
        
        if self.environment == 'production':
            # Production deployment
            result = subprocess.run([
                'kubectl', 'set', 'image',
                'deployment/myapp',
                f'myapp=myapp:{self.timestamp}'
            ])
        else:
            # Dev/staging deployment
            result = subprocess.run([
                'docker-compose', 'up', '-d'
            ])
        
        return result.returncode == 0
    
    def rollback(self):
        """Rollback deployment"""
        print("Rolling back...")
        subprocess.run(['kubectl', 'rollout', 'undo', 'deployment/myapp'])
    
    def execute(self):
        """Execute full deployment pipeline"""
        print(f"Starting deployment to {self.environment}")
        print("=" * 50)
        
        # Run tests
        if not self.run_tests():
            print("Deployment aborted due to test failures")
            return False
        
        # Build
        if not self.build():
            print("Build failed")
            return False
        
        # Deploy
        if not self.deploy():
            print("Deployment failed, rolling back...")
            self.rollback()
            return False
        
        print("✅ Deployment successful!")
        return True

# Usage
if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    deployer = DeploymentManager(env)
    success = deployer.execute()
    sys.exit(0 if success else 1)
```

---

## 4. Jenkins Integration

### Code Example

```python
# jenkins_helper.py
import requests
from requests.auth import HTTPBasicAuth

class JenkinsAPI:
    def __init__(self, url, username, token):
        self.url = url
        self.auth = HTTPBasicAuth(username, token)
    
    def trigger_build(self, job_name, parameters=None):
        """Trigger Jenkins job"""
        url = f"{self.url}/job/{job_name}/buildWithParameters"
        response = requests.post(url, auth=self.auth, data=parameters)
        return response.status_code == 201
    
    def get_build_status(self, job_name, build_number):
        """Get build status"""
        url = f"{self.url}/job/{job_name}/{build_number}/api/json"
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            data = response.json()
            return data['result']
        return None

# Usage
jenkins = JenkinsAPI('http://jenkins.example.com', 'user', 'token')
jenkins.trigger_build('deploy-prod', {'VERSION': '1.2.3'})
```

---

## 📝 Key Takeaways

✅ **Automate everything** - CI/CD pipelines
✅ **Test before deploy** - Catch issues early
✅ **Rollback capability** - Quick recovery
✅ **Environment parity** - Dev matches prod
✅ **Monitoring** - Track deployments

---

## Next Module

Ready for **Module 13: Logging & Monitoring**? 🎯
