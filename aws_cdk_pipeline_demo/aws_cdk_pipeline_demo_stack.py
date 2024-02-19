from aws_cdk import (
    # Duration,
    Stack,
    pipelines 
)
import aws_cdk as cdk
from constructs import Construct
from aws_cdk_pipeline_demo.my_pipeline_app_stage import MyPipelineAppStage
from aws_cdk.pipelines import ManualApprovalStep

class AwsCdkPipelineDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  pipelines.CodePipeline(self, "Pipeline",
                        pipeline_name="MyPipeline",
                        synth=pipelines.ShellStep("Synth",
                            input=pipelines.CodePipelineSource.git_hub("ayushpandey09/aws_cdk_pipeline_demo", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
        testing_stage = pipeline.add_stage(MyPipelineAppStage(self,"testing",
        env=cdk.Environment(account="764246084048", region="us-east-1")))
        
        testing_stage.add_post(ManualApprovalStep('approval to deploy to prod'))
        
        prod_stage = pipeline.add_stage(MyPipelineAppStage(self,"production",
        env=cdk.Environment(account="764246084048", region="us-east-1")))
        
