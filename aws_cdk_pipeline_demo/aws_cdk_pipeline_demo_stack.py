from aws_cdk import (
    # Duration,
    Stack,
    pipelines 
)
from constructs import Construct

class AwsCdkPipelineDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  pipelines.CodePipeline(self, "Pipeline",
                        pipeline_name="MyPipeline",
                        synth=pipelines.ShellStep("Synth",
                            input=pipelines.CodePipelineSource.git_hub("OWNER/REPO", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
