# Day 06: Introduction to DevOps - Complete Guide

## Table of Contents
1. [What is DevOps?](#what-is-devops)
2. [Setting Up Your Development Environment](#setting-up-your-development-environment)
3. [Creating a Simple Django Application](#creating-a-simple-django-application)
4. [Setting Up GitHub Repository](#setting-up-github-repository)
5. [Understanding GitHub Actions](#understanding-github-actions)
6. [Setting Up Self-Hosted Runner](#setting-up-self-hosted-runner)
7. [Understanding Infrastructure as Code with Terraform](#understanding-infrastructure-as-code-with-terraform)
8. [Putting It All Together](#putting-it-all-together)

## What is DevOps?

DevOps is a combination of software development (Dev) and IT operations (Ops). It aims to shorten the development lifecycle and provide continuous delivery with high software quality.

### Key DevOps Concepts:
1. **Continuous Integration (CI)**: Developers frequently merge their code changes into a central repository
2. **Continuous Deployment (CD)**: Automated process of deploying code changes to production
3. **Infrastructure as Code (IaC)**: Managing infrastructure through code instead of manual processes

## Setting Up Your Development Environment

### 1. Install Required Software

#### Windows:
```bash
# Install Git
# Download from: https://git-scm.com/download/win

# Install Python
# Download from: https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation

# Install Terraform
# Download from: https://www.terraform.io/downloads.html
# Extract and add to PATH
```

#### Linux (Ubuntu):
```bash
# Update package list
sudo apt update

# Install Git
sudo apt install git

# Install Python
sudo apt install python3 python3-pip python3-venv

# Install Terraform
sudo apt install wget unzip
wget https://releases.hashicorp.com/terraform/1.5.7/terraform_1.5.7_linux_amd64.zip
unzip terraform_1.5.7_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

### 2. Verify Installations
```bash
# Check Git version
git --version

# Check Python version
python --version
pip --version

# Check Terraform version
terraform --version
```

## Creating a Simple Django Application

### 1. Create Project Directory
```bash
mkdir django-cicd-demo
cd django-cicd-demo
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django and Other Requirements
```bash
pip install django==5.0.2 gunicorn==21.2.0 python-dotenv==1.0.1
```

### 4. Create Django Project
```bash
django-admin startproject hello .
```

### 5. Create a Simple View
Create a new file `hello/views.py`:
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! This is our Django application deployed with CI/CD!")
```

### 6. Update URLs
Edit `hello/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
```

### 7. Test the Application
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser to see the application.

## Setting Up GitHub Repository

### 1. Create a GitHub Account
- Go to https://github.com
- Sign up for a new account

### 2. Create a New Repository
1. Click the "+" button in the top right
2. Select "New repository"
3. Name it "django-cicd-demo"
4. Make it public
5. Don't initialize with README
6. Click "Create repository"

### 3. Push Your Code to GitHub
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/django-cicd-demo.git

# Push to GitHub
git push -u origin main
```

## Understanding GitHub Actions

GitHub Actions is a CI/CD platform that allows you to automate your build, test, and deployment pipeline.

### 1. Create GitHub Actions Workflow
Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy Django Application

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  deploy:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          
      - name: Run Django migrations
        run: |
          python manage.py migrate
          
      - name: Start Gunicorn server
        run: |
          gunicorn hello.wsgi:application --bind 0.0.0.0:8000 --daemon
```

## Setting Up Self-Hosted Runner

### 1. Set Up a Virtual Machine
- Use any cloud provider (AWS, DigitalOcean, etc.)
- Recommended: Ubuntu 20.04 LTS
- Minimum requirements: 2GB RAM, 1 CPU

### 2. Install Required Software on VM
```bash
# Update package list
sudo apt update

# Install required packages
sudo apt install -y python3 python3-pip python3-venv git

# Install Gunicorn
sudo pip3 install gunicorn
```

### 3. Configure GitHub Self-Hosted Runner
1. Go to your GitHub repository
2. Click "Settings" > "Actions" > "Runners"
3. Click "New self-hosted runner"
4. Follow the instructions provided by GitHub
5. Run the commands on your VM

## Understanding Infrastructure as Code with Terraform

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.

### 1. Create Terraform Configuration
Create `terraform/main.tf`:
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "django_app" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu 20.04 LTS
  instance_type = "t2.micro"
  key_name      = "your-key-name"

  tags = {
    Name = "django-cicd-app"
  }
}
```

### 2. Initialize Terraform
```bash
cd terraform
terraform init
```

### 3. Apply Terraform Configuration
```bash
terraform apply
```

## Putting It All Together

### 1. Complete Setup Steps
1. Set up your development environment
2. Create and test the Django application
3. Push code to GitHub
4. Set up self-hosted runner
5. Configure GitHub Actions
6. Set up infrastructure with Terraform

### 2. Test the Pipeline
1. Make a small change to your code
2. Push the change to GitHub
3. Watch the GitHub Actions workflow run
4. Verify the application is deployed

### 3. Troubleshooting Common Issues
1. **GitHub Actions not running**
   - Check if the runner is online
   - Verify workflow file syntax
   - Check repository permissions

2. **Application not accessible**
   - Check security group settings
   - Verify Gunicorn is running
   - Check firewall settings

3. **Terraform errors**
   - Check AWS credentials
   - Verify resource limits
   - Check network connectivity

## Additional Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Django Documentation](https://docs.djangoproject.com)
- [Gunicorn Documentation](https://docs.gunicorn.org)

## Next Steps
1. Add automated testing to your pipeline
2. Implement monitoring and logging
3. Set up staging environment
4. Learn about containerization with Docker
5. Explore more advanced CI/CD patterns 