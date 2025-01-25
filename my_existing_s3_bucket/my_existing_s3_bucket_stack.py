from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from constructs import Construct

class MyExistingS3BucketStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Resources
    s3Bucket00aaclsands32024011900pIrkZ = s3.CfnBucket(self, 'S3Bucket00aaclsands32024011900pIrkZ',
          public_access_block_configuration = {
            'restrictPublicBuckets': True,
            'ignorePublicAcls': True,
            'blockPublicPolicy': True,
            'blockPublicAcls': True,
          },
          bucket_name = 'aaclsands320240119',
          ownership_controls = {
            'rules': [
              {
                'objectOwnership': 'BucketOwnerEnforced',
              },
            ],
          },
          bucket_encryption = {
            'serverSideEncryptionConfiguration': [
              {
                'bucketKeyEnabled': True,
                'serverSideEncryptionByDefault': {
                  'sseAlgorithm': 'aws:kms',
                  'kmsMasterKeyId': 'arn:aws:kms:ap-southeast-2:781953648079:alias/aws/s3',
                },
              },
            ],
          },
          versioning_configuration = {
            'status': 'Enabled',
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
              cdk.CfnTag(key='environment', value='production'),
              cdk.CfnTag(key='cost-centre', value='1000')  # New tag added
          ],

        )
    s3Bucket00aaclsands32024011900pIrkZ.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN
    s3Bucket00aaclsands32024011900pIrkZ.cfn_options.update_replace_policy = cdk.CfnDeletionPolicy.RETAIN

    s3BucketPolicy00aaclsands32024011900Gp3Ut = s3.CfnBucketPolicy(self, 'S3BucketPolicy00aaclsands32024011900Gp3Ut',
          bucket = s3Bucket00aaclsands32024011900pIrkZ.ref,
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Condition': {
                  'Bool': {
                    'aws:SecureTransport': 'false',
                  },
                },
                'Resource': [
                  'arn:aws:s3:::aaclsands320240119',
                  'arn:aws:s3:::aaclsands320240119/*',
                ],
                'Action': 's3:*',
                'Effect': 'Deny',
                'Principal': '*',
                'Sid': 'RestrictToTLSRequestsOnly',
              },
              {
                'Condition': {
                  'Null': {
                    's3:x-amz-server-side-encryption-aws-kms-key-id': 'true',
                  },
                },
                'Resource': 'arn:aws:s3:::aaclsands320240119/*',
                'Action': 's3:PutObject',
                'Effect': 'Deny',
                'Principal': '*',
                'Sid': 'DenyObjectsThatAreNotSSEKMS',
              },
            ],
            'Id': 'PutObjPolicy',
          },
 
        )
    s3BucketPolicy00aaclsands32024011900Gp3Ut.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN
    s3BucketPolicy00aaclsands32024011900Gp3Ut.cfn_options.update_replace_policy = cdk.CfnDeletionPolicy.RETAIN


