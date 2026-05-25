# Module 7: Virtual Environments & Packaging

## 📖 What You'll Learn
- What are virtual environments and why they matter
- Creating and activating virtual environments
- Managing packages with pip
- requirements.txt for dependency management
- Best practices for Python projects

---

## 1. Why Virtual Environments?

### Concept Explanation

A **virtual environment** is an isolated Python environment that has its own:
- Python interpreter
- Installed packages
- Dependencies

**Without virtual environments:**
```
System Python
├── Project A needs requests 2.25.0
├── Project B needs requests 2.28.0  ❌ CONFLICT!
└── All packages installed globally
```

**With virtual environments:**
```
System Python
├── venv_project_a/
│   └── requests 2.25.0 ✅
├── venv_project_b/
│   └── requests 2.28.0 ✅
└── Each project isolated
```

### DevOps Use Case

Virtual environments are **essential** for:
- Avoiding dependency conflicts between projects
- Reproducing exact environments
- CI/CD pipelines (consistent builds)
- Docker containers
- Team collaboration (everyone uses same versions)
- Testing different package versions

---

## 2. Creating Virtual Environments

### Concept Explanation

Python 3 includes `venv` module for creating virtual environments.

**Commands:**
```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Linux/Mac)
source myenv/bin/activate

# Deactivate
deactivate
```

### Code Example

```bash
# Create a virtual environment for your project
python -m venv devops_env

# Activate it (Windows PowerShell)
devops_env\Scripts\Activate.ps1

# Activate it (Windows Command Prompt)
devops_env\Scripts\activate.bat

# Your prompt changes to show active environment
(devops_env) C:\Projects\myproject>

# Check Python location (should be in venv)
where python

# Install packages (only in this environment)
pip install requests

# Deactivate when done
deactivate
```

### Real DevOps Example

```bash
# Project structure
my-automation-project/
├── venv/                 # Virtual environment (don't commit!)
├── src/
│   ├── deploy.py
│   └── monitor.py
├── requirements.txt      # Package list
├── README.md
└── .gitignore           # Ignore venv/

# Create and activate environment
cd my-automation-project
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run your scripts
python src/deploy.py
```

---

## 3. Package Management with pip

### Concept Explanation

**pip** is Python's package installer. It downloads packages from PyPI (Python Package Index).

**Common commands:**
```bash
pip install package_name          # Install package
pip install package_name==1.2.3   # Install specific version
pip install package_name>=1.2.0   # Install minimum version
pip uninstall package_name        # Remove package
pip list                          # List installed packages
pip show package_name             # Show package details
pip freeze                        # List all packages with versions
pip install --upgrade package_name # Update package
```

### DevOps Use Case

Common DevOps packages:
- `requests` - HTTP requests for APIs
- `boto3` - AWS SDK
- `paramiko` - SSH connections
- `pyyaml` - YAML parsing
- `docker` - Docker API
- `kubernetes` - Kubernetes API
- `ansible` - Automation (if using Python)
- `pytest` - Testing

### Code Example

```bash
# Activate your virtual environment first
venv\Scripts\activate

# Install single package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install requests pyyaml boto3

# Check what's installed
pip list

# Output:
# Package    Version
# ---------- -------
# boto3      1.26.0
# requests   2.28.0
# PyYAML     6.0

# Show package details
pip show requests

# Output:
# Name: requests
# Version: 2.28.0
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# ...

# Upgrade a package
pip install --upgrade requests

# Uninstall
pip uninstall requests
```

---

## 4. requirements.txt

### Concept Explanation

`requirements.txt` is a file that lists all your project's dependencies. This allows anyone to install the exact same packages.

**Format:**
```
package_name==version
package_name>=min_version
package_name
```

### DevOps Use Case

`requirements.txt` is used in:
- CI/CD pipelines (install dependencies automatically)
- Docker images (reproducible builds)
- Team collaboration (everyone uses same versions)
- Deployment (ensure production matches development)

### Code Example

**Creating requirements.txt:**
```bash
# After installing packages in your venv
pip freeze > requirements.txt
```

**Example requirements.txt:**
```
requests==2.28.0
boto3==1.26.0
PyYAML==6.0
paramiko==3.0.0
python-dotenv==0.21.0
```

**Installing from requirements.txt:**
```bash
# Create new virtual environment
python -m venv new_venv
new_venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# All packages installed with exact versions!
```

**requirements.txt with comments:**
```
# Web requests
requests==2.28.0

# AWS SDK
boto3==1.26.0

# Configuration parsing
PyYAML==6.0

# SSH connections
paramiko>=3.0.0

# Environment variables
python-dotenv==0.21.0
```

---

## 5. Best Practices

### Project Structure

```
my-devops-project/
├── venv/                    # Virtual environment (in .gitignore)
├── src/
│   ├── __init__.py
│   ├── deploy.py
│   └── utils.py
├── tests/
│   └── test_deploy.py
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── .gitignore              # Ignore venv, __pycache__, etc.
├── README.md
└── setup.py                # Optional: for installable packages
```

### .gitignore for Python

```
# Virtual environments
venv/
env/
ENV/
.venv/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Distribution
dist/
build/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp

# Environment variables
.env
.env.local

# OS
.DS_Store
Thumbs.db
```

### requirements-dev.txt

Separate development dependencies:
```
# Include production requirements
-r requirements.txt

# Development tools
pytest==7.2.0
black==22.12.0
flake8==6.0.0
mypy==0.991
```

### Code Example

**Complete workflow:**

```bash
# 1. Create project directory
mkdir my-automation
cd my-automation

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install packages
pip install requests pyyaml

# 5. Create requirements.txt
pip freeze > requirements.txt

# 6. Create .gitignore
echo venv/ > .gitignore
echo __pycache__/ >> .gitignore

# 7. Initialize git
git init
git add .
git commit -m "Initial commit"

# 8. Work on your project
# ... write code ...

# 9. When done, deactivate
deactivate
```

**Sharing with team:**

```bash
# Team member clones repo
git clone https://github.com/yourteam/my-automation.git
cd my-automation

# Create their own virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Ready to work!
```

---

## 6. Real DevOps Scenario

### Example: Deployment Script Project

**Project setup:**

```bash
# Create project
mkdir deployment-automation
cd deployment-automation

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install DevOps packages
pip install boto3 paramiko pyyaml requests python-dotenv

# Create requirements.txt
pip freeze > requirements.txt
```

**requirements.txt:**
```
boto3==1.26.0
botocore==1.29.0
certifi==2022.12.7
charset-normalizer==3.0.1
cryptography==39.0.0
idna==3.4
jmespath==1.0.1
paramiko==3.0.0
PyNaCl==1.5.0
python-dateutil==2.8.2
python-dotenv==0.21.0
PyYAML==6.0
requests==2.28.0
s3transfer==0.6.0
six==1.16.0
urllib3==1.26.14
```

**deploy.py:**
```python
import boto3
import yaml
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# AWS credentials from .env
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Load config
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Deploy to AWS
ec2 = boto3.client('ec2', region_name=config['region'])
# ... deployment logic ...
```

**.env (not in git):**
```
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here
```

**README.md:**
```markdown
# Deployment Automation

## Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create .env file with your credentials

4. Run deployment:
   ```bash
   python deploy.py
   ```
```

---

## 🎯 Mini Exercise 1: Create Virtual Environment

**Task**: Create a virtual environment and install packages.

**Steps:**
1. Create directory `test-project`
2. Create virtual environment `venv`
3. Activate it
4. Install `requests` package
5. Create `requirements.txt`

---

## ✅ Solution 1

```bash
# Create directory
mkdir test-project
cd test-project

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install package
pip install requests

# Create requirements.txt
pip freeze > requirements.txt

# Check contents
type requirements.txt

# Deactivate
deactivate
```

---

## 🎯 Mini Exercise 2: Share Project

**Task**: Create a project structure that can be shared with a team.

**Requirements:**
1. Create virtual environment
2. Install `requests` and `pyyaml`
3. Create `requirements.txt`
4. Create `.gitignore`
5. Create `README.md` with setup instructions

---

## ✅ Solution 2

```bash
# Create project
mkdir shared-project
cd shared-project

# Create venv
python -m venv venv
venv\Scripts\activate

# Install packages
pip install requests pyyaml

# Create requirements.txt
pip freeze > requirements.txt

# Create .gitignore
echo venv/ > .gitignore
echo __pycache__/ >> .gitignore
echo .env >> .gitignore

# Create README.md
echo # Shared Project > README.md
echo. >> README.md
echo ## Setup >> README.md
echo 1. python -m venv venv >> README.md
echo 2. venv\Scripts\activate >> README.md
echo 3. pip install -r requirements.txt >> README.md
```

---

## 📝 Key Takeaways

✅ **Always use virtual environments** - One per project
✅ **Activate before installing** - Packages go in venv
✅ **Create requirements.txt** - For reproducibility
✅ **Add venv/ to .gitignore** - Don't commit environments
✅ **Use pip freeze** - Capture exact versions
✅ **Document setup** - In README.md
✅ **Separate dev dependencies** - requirements-dev.txt

---

## 🚀 Practice Challenge

Create a complete DevOps automation project:
1. Create project directory structure
2. Set up virtual environment
3. Install: requests, pyyaml, boto3
4. Create requirements.txt
5. Create .gitignore
6. Write README.md with setup instructions
7. Create a simple script that uses the packages

---

## Next Module

Ready for **Module 8: OS & System Automation**? Learn to interact with the operating system! 🎯
