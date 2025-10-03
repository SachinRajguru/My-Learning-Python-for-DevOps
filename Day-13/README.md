# AWS Automation (boto3 basics, Lambda fundamentals, cost optimization project)

## Overview

- Introduction to Boto3 (Python SDK for AWS APIs) for creating/managing resources like S3 buckets and EC2 instances.
- AWS Lambda fundamentals, serverless architecture, differences from EC2, and DevOps use cases (e.g., monitoring, alerts).
- Cloud cost optimization project using Lambda + Boto3 to delete stale EBS snapshots, with demo steps and code.

These notes include explanations, code examples, comparisons, and step-by-step demos. They are designed for revision, interview prep, and hands-on practice. Always clean up AWS resources after demos to avoid costs (use Free Tier where possible).

## Prerequisites

- Basic Python knowledge (variables, loops, functions—from Days 1-10 of the series).
- AWS account (Free Tier recommended) and familiarity with AWS Console (e.g., creating EC2/S3 manually).
- Tools: Python 3.x, Boto3 (`pip install boto3`), AWS CLI (`aws configure` for authentication).
- GitHub Repo: Refer to the original series repo (linked in video descriptions) for full syllabus, day-wise notes, and code.

## Files

This repository/folder contains three modular Markdown files for easy navigation and focused study:

1. **01-boto3.md**  
   Comprehensive notes on Boto3: What it is, setup, syntax (client vs. resource), comparisons (vs. CLI/Terraform/CFT), and examples (e.g., creating S3 buckets, getting ACLs). Includes prerequisites like AWS UI mastery and why Boto3 excels in serverless scripting.

2. **02-lambda-fundamentals.md**  
   Covers Lambda basics: Serverless vs. serverful (EC2 comparison table), event-driven architecture, DevOps use cases (cost optimization, security), and a UI demo for creating/testing a simple function. Explains triggers, roles, and configurations.

3. **03-cost-optimization-project.md**  
   Project-focused notes: Why cost optimization matters, architecture (Lambda + Boto3), problem statement (stale EBS snapshots), full demo steps (setup, code, testing, CloudWatch scheduling), and code walkthrough. Includes tips for extensions (e.g., timestamps, SNS notifications).

## Usage

- **Revision**: Read files sequentially; use headings and code blocks for quick scans.
- **Practice**:
  - Replicate demos in AWS Console (e.g., create Lambda, run Boto3 scripts).
  - Add to Resume: "Automated AWS cost optimization by deleting stale EBS snapshots using Python, Boto3, and Lambda—reduced unused resource costs."
  - Customize: Extend the project to S3/RDS; add 30-day thresholds.
- **Interview Prep**: Explain concepts like "Boto3 abstracts AWS APIs for Python automation" or "Lambda for event-driven DevOps tasks (e.g., daily cost scans via CloudWatch)."
- **Run Code**: Use VS Code or GitHub Codespaces. Authenticate with AWS CLI; test locally before deploying to Lambda.

## Important Notes

- **Costs**: AWS Free Tier covers basics, but monitor usage (e.g., Lambda invocations, EBS snapshots). Delete test resources (EC2, volumes, snapshots) after demos.
- **Best Practices**: Use least-privilege IAM roles; keep Lambda timeouts low (e.g., 10s); enable CloudWatch for automation but disable after testing.
- **Further Reading**:
  - Boto3 Docs: [boto3.amazonaws.com](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
  - AWS Lambda Docs: [docs.aws.amazon.com/lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).