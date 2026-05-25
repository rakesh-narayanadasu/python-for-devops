# Module 11: Cloud & DevOps Tools

## 📖 What You'll Learn
- AWS automation with boto3
- Docker automation concepts
- Kubernetes scripting basics
- Infrastructure as Code concepts

---

## 1. AWS with boto3

### Concept Explanation

boto3 is the AWS SDK for Python, allowing you to interact with AWS services.

### Code Example

```python
import boto3

# Initialize clients
ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3')

# List EC2 instances
def list_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Type: {instance['InstanceType']}")

# List S3 buckets
def list_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']}")

# Upload file to S3
def upload_to_s3(file_path, bucket, key):
    s3.upload_file(file_path, bucket, key)
    print(f"Uploaded {file_path} to s3://{bucket}/{key}")

# Download from S3
def download_from_s3(bucket, key, file_path):
    s3.download_file(bucket, key, file_path)
    print(f"Downloaded s3://{bucket}/{key} to {file_path}")
```

---

## 2. Docker Automation

### Code Example

```python
import subprocess
import json

def docker_ps():
    """List running containers"""
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{json .}}'],
        capture_output=True,
        text=True
    )
    
    containers = []
    for line in result.stdout.strip().split('\n'):
        if line:
            containers.append(json.loads(line))
    return containers

def docker_build(image_name, dockerfile_path='.'):
    """Build Docker image"""
    result = subprocess.run(
        ['docker', 'build', '-t', image_name, dockerfile_path],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def docker_run(image_name, ports=None, env=None):
    """Run Docker container"""
    cmd = ['docker', 'run', '-d']
    
    if ports:
        for host_port, container_port in ports.items():
            cmd.extend(['-p', f'{host_port}:{container_port}'])
    
    if env:
        for key, value in env.items():
            cmd.extend(['-e', f'{key}={value}'])
    
    cmd.append(image_name)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

# Usage
containers = docker_ps()
for container in containers:
    print(f"Container: {container.get('Names')}")
```

---

## 3. Kubernetes Scripting

### Code Example

```python
import subprocess
import yaml

def kubectl_get_pods(namespace='default'):
    """Get pods in namespace"""
    result = subprocess.run(
        ['kubectl', 'get', 'pods', '-n', namespace, '-o', 'json'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        import json
        data = json.loads(result.stdout)
        return data['items']
    return []

def kubectl_apply(manifest_file):
    """Apply Kubernetes manifest"""
    result = subprocess.run(
        ['kubectl', 'apply', '-f', manifest_file],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def create_deployment_manifest(name, image, replicas=3):
    """Generate deployment manifest"""
    manifest = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name},
        'spec': {
            'replicas': replicas,
            'selector': {
                'matchLabels': {'app': name}
            },
            'template': {
                'metadata': {
                    'labels': {'app': name}
                },
                'spec': {
                    'containers': [{
                        'name': name,
                        'image': image,
                        'ports': [{'containerPort': 80}]
                    }]
                }
            }
        }
    }
    
    with open(f'{name}-deployment.yaml', 'w') as f:
        yaml.dump(manifest, f)
    
    return f'{name}-deployment.yaml'

# Usage
pods = kubectl_get_pods()
for pod in pods:
    print(f"Pod: {pod['metadata']['name']}")
    print(f"Status: {pod['status']['phase']}")
```

---

## 4. Infrastructure as Code Concepts

### Code Example

```python
# Example: Generate Terraform configuration
def generate_terraform_config(instances):
    """Generate Terraform config for EC2 instances"""
    config = """
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
"""
    
    for i, instance in enumerate(instances):
        config += f"""
resource "aws_instance" "server_{i}" {{
  ami           = "{instance['ami']}"
  instance_type = "{instance['type']}"
  
  tags = {{
    Name = "{instance['name']}"
  }}
}}
"""
    
    with open('main.tf', 'w') as f:
        f.write(config)
    
    return 'main.tf'

# Usage
instances = [
    {'name': 'web-server-1', 'ami': 'ami-12345', 'type': 't2.micro'},
    {'name': 'web-server-2', 'ami': 'ami-12345', 'type': 't2.micro'}
]

generate_terraform_config(instances)
```

---

## 📝 Key Takeaways

✅ **boto3 for AWS** - Automate cloud operations
✅ **Docker CLI** - Container management
✅ **kubectl** - Kubernetes operations
✅ **IaC** - Infrastructure as Code
✅ **Automation** - Reduce manual work

---

## Next Module

Ready for **Module 12: CI/CD & Automation**? 🎯
