#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_pipeline_demo.aws_cdk_pipeline_demo_stack import AwsCdkPipelineDemoStack


app = cdk.App()
AwsCdkPipelineDemoStack(app, "MyPipelineStack",
    env=cdk.Environment(account="764246084048", region="us-east-1") #update you account and region
)

app.synth()
