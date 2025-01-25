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
                  'sseAlgorithm': 'AES256',
                },
              },
            ],
          },
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
            ],
            'Id': 'PutObjPolicy',
          },
        )
    s3BucketPolicy00aaclsands32024011900Gp3Ut.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN
    s3BucketPolicy00aaclsands32024011900Gp3Ut.cfn_options.update_replace_policy = cdk.CfnDeletionPolicy.RETAIN


