"""
Create/deploy a Lambda Function
"""
from aws_cdk import Duration, Stack, aws_lambda
from constructs import Construct


# Main application stack
class SmileStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = aws_lambda.Function(
            self, "SmileFunction",
            function_name="SmileFunction",
            code=aws_lambda.Code.from_asset("package"),
            handler="handler.main",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            tracing=aws_lambda.Tracing.ACTIVE,
        )
