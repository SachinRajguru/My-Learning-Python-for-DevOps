# Boto3 (Basics)

## What is Boto3?

- **Definition:** 
  - Boto3 is a Python package (SDK) for interacting with AWS services programmatically.
  - It allows you to create, manage, and query AWS resources (e.g., EC2 instances, S3 buckets) using Python scripts.

- **Use Case:** 
  - Automate AWS API calls. Instead of using the AWS Console (UI) or CLI manually, write Python code to perform tasks like creating an S3 bucket or EC2 instance.

- **Why Boto3?** 
  - Abstracts complex details: Handles authentication, hundreds of APIs, and low-level HTTP requests (e.g., via `requests` module would take 100+ lines; Boto3 does it in 20-30 lines).
  - Ideal for DevOps: Enables scripting for automation, especially in serverless environments like AWS Lambda.

- **One-Line Summary:** 
  - Boto3 is the Python module to talk to AWS APIs and create/manage resources programmatically.

## Prerequisites

- **Master AWS UI First:** 
  - Know how to create resources manually (e.g., EC2 instance via Console) to understand fields like AMI, instance type, key pair, or S3 bucket parameters. Automation succeeds when you know manual steps. 
    - Why? Boto3 mirrors UI fields; without UI knowledge, you'll miss mandatory parameters (e.g., `Bucket` for S3 is required).

- **Common Pitfalls:** 
  - People find Boto3/Terraform hard due to lack of AWS basics. Learn AWS services (e.g., EC2, S3) before scripting.

## Boto3 vs. Other AWS Tools

- **All Tools Create/Manage AWS Resources:**
  - **AWS CLI:** Command-line scripting (e.g., `aws s3 ls`). Quick for simple tasks but uses shell scripting.
  - **Boto3:** Python scripting. Better for complex logic, loops, and integration (e.g., with Lambda).

- **Templating vs. Scripting:**
  - **Terraform/CloudFormation (CFT):** Declarative templating (HCL/JSON files). No programming needed; good for infrastructure as code (IaC) but setup-heavy for quick actions.
  - **AWS CLI/Boto3:** Imperative scripting. Use for dynamic tasks (e.g., conditionals, loops).

- **When to Use Boto3 Over CLI?**
  - **CLI:** Quick one-off commands (e.g., list S3 buckets in <1 min).
  - **Boto3:** Serverless (Lambda) integration; Python's power for DevOps tasks like monitoring/cost optimization. No shell scripting in Lambda—use Python/Node.js/Go.

- **Key Difference:**
  - Templating for static infra; scripting for dynamic/quick actions. Boto3 shines in event-driven, serverless DevOps (e.g., Lambda for alerts/notifications).

## Setup for Boto3

1. **Environment:** Use VS Code, IntelliJ, or GitHub Codespaces.
2. **Install AWS CLI (for authentication):**
  - In Codespaces: Dev Container > Add Config > Select AWS (installs CLI; restart takes 10-15 min).
  - Terminal: Run `aws configure` (enter Access Key ID, Secret Access Key from AWS IAM > Security Credentials > Create Access Key).
    - Default region: e.g., `us-east-1`.
    - Output: `json`.
3. **Install Boto3:** `pip install boto3` (or `pip3 install boto3` if errors).
4. **Authentication:** AWS CLI config handles creds; no need to hardcode in scripts.

## Boto3 Basics and Syntax

- **Import:** `import boto3`.
- **Core Syntax:**
    - **Client Mode** (Recommended; low-level, supports all services):
    ```python
        client = boto3.client('s3')  # Replace 's3' with service (e.g., 'ec2').
    response = client.create_bucket(Bucket='my-unique-bucket-name')
    ```
    - Client specifies the AWS service (e.g., S3, EC2) to interact with APIs.
    - Use for new services; abstracts API calls.
- **Resource Mode** (High-level abstraction; easier but deprecated for new services):
  ```python
      s3 = boto3.resource('s3')
    bucket = s3.create_bucket(Bucket='my-bucket')
    ```
    - Simpler syntax but avoid for future-proofing.
- **Documentation:** 
    - Boto3 Docs: [boto3.amazonaws.com](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). Search service (e.g., S3) > Available Services > Code examples for actions (e.g., `create_bucket`). 
      - Check "Required" fields (e.g., `Bucket for S3`).
- **Error Handling:** 
  - Use `botocore` exceptions (built-in; no need for custom try-except initially). 
    - Example: `from botocore.exceptions import ClientError`.

---

## Examples

1. **Create S3 Bucket (`test.py`):**
  ```python
     import boto3
   client = boto3.client('s3')
   response = client.create_bucket(Bucket='abi-demo-boto3-youtube-123')  # Unique name required.
   print(response)
   ```
  - Run: `python test.py`.
  - Verify: AWS Console > S3 > Buckets.
  - Tip: Bucket names must be globally unique; add random suffix.

2. **Get S3 Bucket ACL:**
  ```python
     import boto3
   client = boto3.client('s3')
   response = client.get_bucket_acl(Bucket='abi-demo-boto3-youtube-123')
   print(response)  # JSON output; parse to dict for actions (e.g., owner info).
   ```
  - Parse JSON: Use loops/dicts (from Day 11 GitHub API notes).

- **General Workflow:**
1. Create client for service.
2. Call API method (e.g., `create_bucket`, `get_bucket_acl`).
3. Handle response (print/JSON parsing).

- **Pro Tip:**
  - For any resource/action, search Boto3 docs > Service > Action > Copy code. Modify parameters based on UI knowledge.

---

## Key Takeaways

- Boto3 simplifies AWS automation; learn AWS UI first.
- Use client mode; integrate with Python fundamentals (loops, functions from Days 1-10).
- Projects: Day 11 (GitHub API), Day 12 (File Ops); Day 13 (AWS resources); Day 14 (CI/CD).