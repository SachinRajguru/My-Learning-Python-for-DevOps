# Cloud Cost Optimization Project (EBS Stale Snapshots with Lambda + Boto3)

## Why Cost Optimization?

- **Cloud Migration Goals:** Reduce infra overhead (vs. on-premises data centers) + optimize costs.
- **Problem:** Stale resources (forgotten/deleted items) inflate bills.
    - Example: Developer creates EC2 + EBS volume + daily snapshots > Deletes EC2/volume but forgets snapshots > AWS charges for storage.
    - Other: Unused S3 buckets, EKS clusters, Elastic IPs.
- **DevOps Role:** Monitor 200+ AWS services; delete stale items or notify (SNS). Ensures costs decrease post-migration.
- **Thresholds:** Add logic (e.g., delete if >30 days old/unused).

---

## Project: Delete Stale EBS Snapshots

- **Problem Statement:** Fetch EBS snapshots; delete if not associated with a volume or if volume not attached to running EC2 instance.
- **Architecture:**
    1. Lambda Function (Python + Boto3).
    2. Boto3 queries AWS APIs (describe snapshots/volumes/instances).
    3. Filter stale snapshots > Delete.
    4. Trigger: Manual or CloudWatch (cron, e.g., daily 10 AM).
- **Why Lambda?** Event-driven; auto-scale/teardown. Better than EC2 (no manual start/stop).

## Demo Steps (Replicate in AWS Free Tier)

1. **Setup Resources** (for Testing):
    - EC2 Dashboard > Launch Instance: Ubuntu, t2.micro (auto-creates volume, e.g., vol-xxx ending in 545e).
    - Wait for running > Volumes > Note volume ID.
    - Snapshots > Create Snapshot (from volume) > Name: "test-snapshot".
    - (Optional: Create extra volume/snapshot for testing.)

2. **Create Lambda Function:**
    - Lambda > Create > Author from Scratch > Name: `cost-optimization-ebs-snapshot` > Python 3.x > Default role.
    - **Code:**
    ```python
    """
    Day-13: AWS Lambda for EBS Snapshot Cleanup
    -------------------------------------------
    This script is meant to run as an AWS Lambda function.
    It helps reduce AWS costs by automatically deleting
    unused / stale EBS snapshots.
    How it works:
    1. Gets all EBS snapshots owned by the account.
    2. Gets all running EC2 instance IDs.
    3. For each snapshot:
    - Deletes if it has no associated volume.
    - Deletes if its volume exists but is not attached to any running instance.
    - Deletes if its associated volume no longer exists.
    4. Logs every deletion for auditing.
    
    Pre-requisites:
    - Attach IAM role to Lambda with permissions:
    * ec2:DescribeSnapshots
    * ec2:DescribeInstances
    * ec2:DescribeVolumes
    * ec2:DeleteSnapshot
    """
    import boto3
    def lambda_handler(event, context):
        # Initialize EC2 client
        ec2 = boto3.client('ec2')
        
        # Step 1: Get all snapshots owned by this account
        response = ec2.describe_snapshots(OwnerIds=['self'])
        
        # Step 2: Get IDs of all running EC2 instances
        instances_response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        active_instance_ids = set()
        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                active_instance_ids.add(instance['InstanceId'])
        
        print(f" Found  {len(response['Snapshots'])} snapshots and {len(active_instance_ids)} running instances.")
        
        # Step 3: Iterate over snapshots and check conditions
        for snapshot in response['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')
            
            if not volume_id:
                # Case A: Snapshot not attached to any volume
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f" Deleted snapshot {snapshot_id} (no associated volume).")

            else:
                # Case B: Check if the volume still exists
                try:
                    volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                    volume = volume_response['Volumes'][0]
                    
                    # If the volume exists but has no active attachments → delete snapshot
                    if not volume['Attachments']:
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f" Deleted snapshot {snapshot_id} (volume {volume_id} not attached to any instance).")
                        
                except ec2.exceptions.ClientError as e:
                    # Case C: Volume not found (already deleted)
                    if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f" Deleted snapshot {snapshot_id} (associated volume {volume_id} not found).")
                    else:
                        print(f" Could not check volume {volume_id} for snapshot {snapshot_id}: {e}")
        return {"status": "completed"}
    ```
    - Logic:
      - Describe running EC2 > Extract IDs (set for fast lookup).
      - Describe volumes > Filter active (available or attached to running EC2).
      - Describe snapshots > For each: If no volume or volume inactive > Delete (try-except for errors).
      - Save > Deploy.

3. **Configure Lambda:**
    - Runtime Settings > Edit > Timeout: 10s (default 3s too short).
    - Permissions > Execution Role > View > Attach Policies:
      - Create Custom Policies (IAM > Policies > Create):
        - Policy 1: EC2 > Actions: `ec2:DeleteSnapshot`, `ec2:DescribeSnapshots` > All Resources > Name: `cost-optimization-ebs`.
        - Policy 2: EC2 > Actions: `ec2:DescribeVolumes`, `ec2:DescribeInstances` > Name: `ec2-permissions`.
      - Attach both to role.
    - Test: Create event `{}` > Test > Logs show no deletions (snapshot active).

4. **Test Stale Scenario:**
  - EC2 > Terminate instance (deletes volume).
  - Test Lambda: Deletes snapshot (logs: "Deleted... not associated").
  - Verify: Snapshots > Empty.

5. **Extra Tests:**
  - Create detached volume + snapshot > Test: Deletes snapshot (volume inactive).
  - Add Timestamp Filter (Optional): In code, check `snapshot['StartTime']` >30 days old before delete.

6. **Automate with CloudWatch:**
  - CloudWatch > Events > Rules > Create Rule > Schedule (Cron: e.g., `0 10 * * ? *` for daily 10 AM UTC).
  - Target: Select Lambda > cost-optimization-ebs-snapshot.
  - Enable: Runs automatically (disable after demo to avoid costs).

## Code Explanation (Boto3 Walkthrough)

  - **Steps in Plain English (Then Boto3):**
    1. List running EC2 instances (`describe_instances` with filter).
    2. List volumes (`describe_volumes`); filter active.
    3. List snapshots (`describe_snapshots`, Owner='self').
    4. For each snapshot: Check volume ID > If missing/inactive > Delete (`delete_snapshot`).
  - **Boto3 Tips:** Docs provide syntax/response JSON. Parse with loops/sets (Python basics). Use try-except for errors.
  - **Customization:** Add SNS notifications; extend to S3/RDS/EKS. Vary per org (e.g., archive to S3 Glacier instead of delete).

## Key Takeaways

  - **Project Value:** Add to resume (explain: "Automated EBS cost optimization via Lambda/Boto3; reduced stale resource costs").
  - **Costs:** Delete test resources; Lambda charges ms-based (keep timeout low).
  - **Extensions:** 30-day threshold (`datetime` module); multi-service scans.