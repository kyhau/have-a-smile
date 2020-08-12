"""
Create/deploy a Lambda Function
"""
from aws_cdk.core import Construct, Duration, Stack
from aws_cdk import aws_lambda


# Main application stack
class SmileStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = aws_lambda.Function(
            self, "SmileFunction",
            function_name="SmileFunction",
            code=aws_lambda.Code.asset("package"),
            handler="handler.main",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            tracing=aws_lambda.Tracing.ACTIVE,
        )
