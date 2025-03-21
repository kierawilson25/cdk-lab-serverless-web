from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    # aws_sqs as sqs,
)

from cdk_dynamo_table_view import TableViewer
from constructs import Construct

from .hitcounter import HitCounter

class CdkLabServerlessWebStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        #Create an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )
        
        #instantiate the hit counter with my_lambda as the downstream function
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter', 
            downstream=my_lambda
        )
        
        #defines an API Gateway REST API resource backed by our "hello" function.
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )
        
        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_counter.table,
        )
        

        
