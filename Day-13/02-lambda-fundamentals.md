# Lambda Functions Fundamentals (Serverless for DevOps)

## What are Lambda Functions?

- **Category:** Compute service (like EC2) but serverless.

- **Problem Solved:** Provides on-demand compute without managing servers (e.g., no provisioning, scaling, or patching).

- **Serverless Architecture:**
  - AWS auto-creates/tears down compute based on your code.
  - Pay-per-use: Charged only for execution time (e.g., 100ms bursts).
  - Event-driven: Triggered by events (e.g., S3 upload, CloudWatch schedule).

- **EC2 vs. Lambda:**

| Aspect       | EC2 (Serverful)                                                                 | Lambda (Serverless)                                                                 |
|--------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Management** | You provision (AMI, type, keys); manual scale/teardown.                        | AWS auto-scales, provisions, tears down. No IP/subnet control.                       |
| **Use Case**   | Long-running apps; full control.                                               | Short tasks (e.g., payments in food app: create infra on request, teardown after).   |
| **Cost**       | Pay for instance time (even idle).                                             | Pay for execution (ms); auto-scale.                                                  |
| **Access**     | Public/private IP; full visibility.                                            | No IP; function URL for external access (optional).                                  |

- **When to Choose?**
  - Dev/Arch team decides based on app design. 
  - DevOps: Use Lambda for automation (e.g., monitoring).

## DevOps Use Cases for Lambda

- **Primary:** Cost optimization, security/compliance, routine checks.
    - **Cost Optimization:** Scan stale resources (e.g., unused EBS snapshots); delete or notify.
    - **Security/Compliance:** Check for non-compliant resources (e.g., gp2 EBS volumes); notify via SNS.
    - **Monitoring/Alerts:** Daily IAM user checks; trigger on events (S3, CloudWatch).

- **Triggers:** CloudWatch (cron/schedule), S3 (object create), API Gateway (HTTP).

- **Why Lambda Over EC2 for DevOps?**
  - Event-driven: Run script daily (e.g., 10 AM) via CloudWatch cron; auto-teardown after 5 min.
  - No manual instance management; avoids forgotten running instances costing money.

- **Limitations:** Supports Python, Node.js, Go, Java, Ruby (no shell). Max 15-min execution.

---

## Creating a Basic Lambda Function (UI Demo)

1. **AWS Console:** Search "Lambda" > Create Function > Author from Scratch.
    - Name: e.g., `test-lambda`.
    - Runtime: Python 3.x.
    - Advanced: Enable Function URL (for public access; auth: Anyone for demo).
    - Role: Default execution role (or existing IAM role).

2. **Code** (Inline Editor):
    ```python
    def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from AWS Zero to Hero Series!'
    }
    ```
    - **Key:** Function must be named `lambda_handler` (entry point; AWS calls this first). Can call other functions from it.
    - Add files/folders or upload ZIP (from local VS Code).

3. **Configuration:**
    - **Environment Variables:** Edit > Add (e.g., tweak values without code changes).
    - **Triggers/Destinations:** Optional (e.g., CloudWatch for schedule; SNS for output).
    - **Permissions:** Role auto-created; attach policies (e.g., for S3 access) via IAM.
    - **VPC:** Optional (restrict to VPC resources).
    - **Timeout:** Default 3s; increase to 10s+ for complex scripts (affects cost).

4. **Test/Run:**
    - Test: Create event (e.g., `{}`) > Test > View logs/response.
    - Access: If Function URL enabled, paste URL in browser (e.g., returns "Hello...").
    - Manual vs. Event-Driven: Manual for testing; CloudWatch for automation.

5. **Best Practices:**
    - Least privilege IAM roles.
    - Keep execution short to minimize cost.
    - For DevOps: Focus on scripts (not full apps); integrate with Boto3.

## Key Takeaways

- Lambda: Event-driven compute for DevOps automation (cost/security).
- Learn (EC2) for comparison.
- GitHub: Notes on serverless, use cases.