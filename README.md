
# Import Existing AWS Resources into CDK (IaC)

This project demonstrates how to import an **existing S3 bucket** into AWS CDK (Infrastructure-as-Code) for governance and auditability.

For a detailed walkthrough, check out https://youtu.be/GeGcf17QS18 

## Steps

### 1. Prerequisites
- AWS CLI configured with SSO/admin access
- CDK v2+ installed
- Python 3.9+

### 2. Use CloudFormation IaC Generator
1. **Scan resources**: In CloudFormation Console > **IaC Generator**, scan your AWS account.
2. **Create template**:
   - Select the S3 bucket and related resources (e.g., bucket policies)
   - Set **Deletion Policy** and **Update Replace Policy** to `Retain` to avoid data loss.
3. **Import as stack**: Deploy the generated template as `myExistingS3Bucket`.

### 3. Generate CDK Code
```bash
cdk migrate --stack-name myExistingS3Bucket --from-stack --language python
cd myExistingS3Bucket
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4.  Modify Configuration (Example: Enable Versioning)
Update my_existing_s3_bucket_stack.py:

#### Add versioning, encryption, lifecycle policies
```python
bucket = s3.CfnBucket(
    ...,
    versioning_configuration={"status": "Enabled"},
    bucket_encryption = {
            'serverSideEncryptionConfiguration': [
              {
                'bucketKeyEnabled': True,
                'serverSideEncryptionByDefault': {
                  'sseAlgorithm': 'aws:kms',
                  'kmsMasterKeyId': '<s3-kms-arn>',
                },
              },
            ],
          },

  lifecycle_configuration = {
            'transitionDefaultMinimumObjectSize': 'all_storage_classes_128K',
            'rules': [
              {
                'status': 'Enabled',
                'id': 'expire_objects',
                'noncurrentVersionExpiration': {
                  'noncurrentDays': 1,
                },
                'expirationInDays': 30,
              },
            ],
          },
    tags=[
              cdk.CfnTag(key='environment', value='dev'),
              cdk.CfnTag(key='cost-centre', value='1000') 
          ],
)
```
### 5. Deploy & Validate
```bash
cdk diff  # Review changes
cdk deploy
```
### 6. Push to Git
```bash
git init
git add .
git commit -m "Initial IaC import"
git remote add origin <https://your-remote-git-repo>
git push -u origin main
```

## Best Practices

- Always review `cdk diff` output before deploying
- Test changes in a non-production environment first
- Use meaningful commit messages for better version control

## Contributing
PRs welcome! 
