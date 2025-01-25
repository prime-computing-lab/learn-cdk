import aws_cdk as core
import aws_cdk.assertions as assertions

from my_existing_s3_bucket.my_existing_s3_bucket_stack import MyExistingS3BucketStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_existing_s3_bucket/my_existing_s3_bucket_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyExistingS3BucketStack(app, "my-existing-s3-bucket")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
