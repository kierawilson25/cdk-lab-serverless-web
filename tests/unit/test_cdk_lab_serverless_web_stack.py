import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lab_serverless_web.cdk_lab_serverless_web_stack import CdkLabServerlessWebStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lab_serverless_web/cdk_lab_serverless_web_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLabServerlessWebStack(app, "cdk-lab-serverless-web")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
