# 🛒 AWS Grocery App - Terraform Deployment

  📖 Table of Contents 

🚀Getting Started

   ● Introduction
   ● How It's Built (Infrastructure Overview)
   ● Architecture Diagrams

🏗️ Core Infrastructure

   ● Network & Security (VPC & Security Groups)
   ● Application Hosting (EC2, Auto Scaling & Load Balancer)
   ● Data & Storage (Database, S3 & ECR)
   ● Access Control (IAM Roles)
   ● Automation (Lambda & Step Functions)

⚙️ Configuration & Deployment

   ● Terraform Modules
   ● Automated Deployment Workflow
   ● GitHub Secrets Setup
   ● Step-by-Step Deployment Guide

🔧 Operations & Support
   ● Troubleshooting Common Issues
   ● Frequently Asked Questions
   ● Technical Glossary

📈 What's Next?
   ● Future Enhancements 
   ● Lambda Layer Creation Guide

🤝 Community
   ● Contributing Guidelines
   ● License Information

🏁 Introduction
   This project was my capstone for the Cloud Track at Masterschool. The application
   itself was originally built by our fantastic Track Mentor, Alejandro Román — huge thanks 
   to him for the foundation!

   Our goal was to design and deploy the AWS infrastructure for the app, piece by piece.
   Rather than manually clicking through the AWS console, I decided to automate the entire
   process using Terraform and GitHub Actions.

   This approach makes the deployment repeatable, scalable, and much 
   less prone to human error.Everything from provisioning servers to 
   deploying the code is now handled automatically.

   For details on the application's features and how to run it locally, please see the 
   original README by Alejandro. This document focuses specifically on the cloud infrastructure
   and the automation pipeline that brings it all to life.

🏗️ Infrastructure Overview

   This Terraform project deploys a scalable grocery app on AWS. The core setup includes:
     ● Auto-scaling App Servers: EC2 instances in multiple zones, running in Docker.
     ● Managed Database: A secure, multi-AZ PostgreSQL RDS instance for high availability.
     ● Load Balancer: Distributes traffic evenly across the app servers.
     ● Cloud Storage: An S3 bucket for user avatars and backups.
   The architecture is built for security, scalability, and reliability.

🛠️ Terraform configuration
The Terraform configuration is modularized as follows:

/bootstrap
│── main.tf
│── variables.tf
/infrastructure
│── /modules
│   ├── alb
│   ├── asg
│   ├── ec2_launch_template
│   ├── iam_ec2
│   ├── iam_lambda
│   ├── lambda
│   ├── rds
│   ├── s3_bucket
│   ├── security_groups
│   ├── vpc
│── main.tf
│── variables.tf
│── outputs.tf
│── terraform.tfvars
│── lambda_data
│── generate_backend.py

🏢 Infrastructure Components

🏗️ How It All Fits Together

🌐 The Foundation (VPC & Security)
     ● A secure virtual network (VPC) with public areas for web servers and private
        areas for the database
     ● Carefully configured security rules that control exactly how each component 
       can communicate

🖥️ The Application Hosting
     ● Auto-scaling EC2 instances that automatically adjust to traffic demands  
     ● Each server runs our application from a Docker container stored in ECR
     ● A load balancer that smartly distributes traffic and checks server health

🗄️ Data & Storage
     ● A reliable PostgreSQL database running in private, secure subnets
     ● S3 storage for user avatars, database backups, and application files

⚡ The Automation Magic
     ● A clever system that automatically populates the database once everything is ready
     ● Uses Step Functions to coordinate the process and Lambda to execute the setup
     ● Each component has just the right permissions through IAM roles

🔄 How the Database Gets Populated Automatically

   This automated process ensures the database is ready to go as soon 
   as the infrastructure is up. Here's how it works:
   
  1. 🎯 The Trigger
     When the SQL database file is uploaded to S3, an EventBridge rule notices it 
     and starts the Step Function.

   2. 🧭 The Coordinator (Step Function)

     This is the brain of the operation - it checks everything is ready before proceeding:
     ● Waits for the database to be fully available and running
     ● Confirms the SQL file exists in S3 and is ready to use
     ● Only when both are ready does it trigger the Lambda function
     ● Handles any hiccups along the way with clear error messages

  3. ⚡ The Worker (Lambda Function)
  Once triggered, this function does the actual work:
     ● Fetches the SQL file from S3
     ● Connects to the database
     ● Runs the SQL commands to populate the database with all the necessary data

  4. 📝 Monitoring & Safety Nets

     ● Complete visibility through CloudWatch logs for both the Step Function and Lambda
     ● Automatic error handling if anything goes wrong with the database, file, or function
     ● Retry logic that waits and checks again if things aren't ready yet

 🧩 Building Blocks
    This setup uses dedicated Terraform modules to keep the code organized and reusable:

   Our infrastructure is built from reusable, focused modules that each handle 
    a specific part of the system. This makes the code easy to understand, update, 
    and maintain.
     ● vpc & security_groups: The secure network foundation, creating the 
       virtual private cloud and the firewall rules for all components.
     ● rds: The brain of the operation—it sets up the managed PostgreSQL 
       database where all the application data lives.
     ● s3_bucket: Our cloud storage attic, securely holding user avatars,
       database dumps, and code for Lambda functions.
     ● iam_ec2 & iam_lambda: The identity managers, granting just the right 
       permissions to our EC2 instances and Lambda functions.
     ● ec2_launch_template & asg: The app hosting engine. This 
       defines the server blueprint and manages a self-healing, scalable group of 
       instances.

🎯 In Summary

   This Terraform project creates a solid, scalable foundation for the grocery app on AWS.
   By breaking the infrastructure into reusable modules, it's straightforward to maintain 
   and adapt for future needs. We've also automated key processes—like populating the 
   database using Lambda and Step Functions—and leveraged S3 for versatile storage, making 
   the entire system both efficient and robust.

🚀 How Deployment Works

   Our GitHub Actions workflow automatically builds and deploys everything when 
   code is pushed to the main branch. Here's the step-by-step process:

🔐 Secure Setup
     ● Checks out the code and securely connects to AWS using OIDC authentication
     ● Sets up Terraform with secure remote state storage

🏗️ Phase 1: Build the Foundation 
     ● Provisions core AWS infrastructure - the network, database, storage, 
       and security rules 
     ● Creates the container registry (ECR) where we'll store our application image

🐳 Application Preparation
     ● Builds and tags the Docker image with the latest application code
     ● Pushes the image to our private container registry
     ● Sets up configuration by generating the necessary environment files

💾 Database Initialization
     ● Uploads the starter database file to S3, which automatically triggers our
       setup process
     ● The system waits for the database to be ready, then populates it with initial data
     ● This ensures the database is fully prepared before any application servers launch

⚡ Phase 2: Launch the Application
     ● Deploys the remaining infrastructure - including the auto-scaling application servers
     ● Cleans up sensitive files and temporary resources
     ● Verifies everything is running and marks the deployment successful

🎯 Live Deployment Status

   Want to see if everything's running smoothly? Add this badge to your README 
   for real-time status:

   ![Deployment Status](https://github.com/<your-org>/<your-repo>/actions /workflows/
   deployment.yml/badge.svg)

   The badge automatically updates to show whether the latest deployment was successful. ✅

🚀 Quick Start Guide

  1. Set Up AWS
     ● Create an AWS account
     ● Create an IAM user with necessary permissions (EC2, RDS, S3, VPC, IAM, CloudWatch)
     ● Install and configure AWS CLI with your credentials
     ● Create an SSH key pair for EC2 access

  2. Get the Code 
     git clone https://github.com/AbbyconsAWS_grocery_v2.gitcd AWS_grocery_v2           
   
  3. Bootstrap Backend
     ● Navigate to bootstrap directory
     ● Create terraform.tfvars with your region, GitHub org/repo
     ● Run the setup script to create Terraform state storage  

  4. Configure GitHub Secrets
     Add these secrets in your GitHub repo settings:
     ● AWS role ARN and region
     ● Database credentials
     ● S3 bucket name (must be unique)
     ● SSH key name and allowed IP
     ● JWT secret key

  5. Deploy
     Push to main branch - the GitHub Actions workflow will automatically:
     ● Build and push Docker image to ECR
     ● Provision all AWS infrastructure
     ● Set up database with initial data
     ● Launch the application

  6. Access Your App 
     Check the GitHub Actions output for the load balancer URL, then visit it in your browser!

🛑 Clean Up
  Run terraform destroy in both infrastructure and bootstrap directories to remove all resources.

  🔙Need to Rollback?
     ● Use terraform destroy to remove everything
     ● Or manually deploy previous Docker images
     ● Database backups are available in S3

  This automated pipeline ensures secure, repeatable deployments with minimal manual steps!

🛠️ Common Issues & Fixes

🚫 Terraform Plan Fails
     ● Usually means: Missing or incorrect GitHub Secrets
     ● Quick fix: Double-check all required variables are set in your repository secrets

🖥️ EC2 Instances Won't Start
     ● Common causes: Missing IAM permissions or issues with the startup script
     ● What to check: Verify the EC2 IAM role and check system logs for error messages

🗄️Database Not Populating
     ● Likely culprit: Lambda can't access S3 or connect to RDS
     ● Troubleshoot: Confirm the Lambda role has proper S3 permissions and the RDS security
       group allows Lambda connections

💡Tip: Check the GitHub Actions logs - they usually point directly to what's wrong!

❓Frequently Asked Questions

  1. How do I change the instance type?
     Update the instance_type variable in your terraform.tfvars file.
  2. How can I connect to the database?
     Use the RDS endpoint (shown in Terraform outputs) from an EC2 instance.
  3. How do I add new components?
     Create or modify modules in the modules directory.

📖Quick Glossary
     ● VPC: Virtual Private Cloud (your AWS network)
     ● ALB: Application Load Balancer (traffic distributor)
     ● ASG: Auto Scaling Group (self-adjusting servers)
     ● ECR: Elastic Container Registry (Docker image storage)
     ● RDS: Relational Database Service (managed database)
     ● IAM: Identity and Access Management (permissions)
     ● OIDC: OpenID Connect (secure authentication)

🚀What's Next?

  Planned Improvements
       ● Enhanced CI/CD pipelines for smoother deployments

  Recently Completed ✅
       ● AWS Lambda for database migrations
       ● Terraform Remote Backend for state management
       ● Lambda layer for Python dependencies

🛠️Building the Lambda Layer
  We package Python dependencies (boto3 & psycopg2) into a Lambda layer using Docker 
  for AWS compatibility.

  Project Structure
  lambda_layer_docker_project/
  ├── lambda_layer/          # Docker build files
  ├── output/               # Generated layer ZIP
  └── lambda_function/      # Your Lambda code

  Quick Build Commands
# Build the layer container
  docker build -t lambda-layer .

# Generate the ZIP file
  docker run --rm -v $(pwd)/output:/output lambda-layer

  The resulting lambda-layer.zip in the output/ folder is ready for AWS.

  🤝 Contributing
  We love community contributions!

  1. Fork the repository
  2. Create your feature branch (git checkout -b feature/amazing-feature)
  3. Commit your changes (git commit -m 'Add amazing feature')
  4. Push and open a Pull Request

📜 License
   MIT Licensed - free for non-commercial use.





