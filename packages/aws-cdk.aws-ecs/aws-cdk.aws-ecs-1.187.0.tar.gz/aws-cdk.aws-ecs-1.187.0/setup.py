import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-ecs",
    "version": "1.187.0",
    "description": "The CDK Construct Library for AWS::ECS",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_ecs",
        "aws_cdk.aws_ecs._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_ecs._jsii": [
            "aws-ecs@1.187.0.jsii.tgz"
        ],
        "aws_cdk.aws_ecs": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk.aws-applicationautoscaling==1.187.0",
        "aws-cdk.aws-autoscaling-hooktargets==1.187.0",
        "aws-cdk.aws-autoscaling==1.187.0",
        "aws-cdk.aws-certificatemanager==1.187.0",
        "aws-cdk.aws-cloudwatch==1.187.0",
        "aws-cdk.aws-ec2==1.187.0",
        "aws-cdk.aws-ecr-assets==1.187.0",
        "aws-cdk.aws-ecr==1.187.0",
        "aws-cdk.aws-elasticloadbalancing==1.187.0",
        "aws-cdk.aws-elasticloadbalancingv2==1.187.0",
        "aws-cdk.aws-iam==1.187.0",
        "aws-cdk.aws-kms==1.187.0",
        "aws-cdk.aws-lambda==1.187.0",
        "aws-cdk.aws-logs==1.187.0",
        "aws-cdk.aws-route53-targets==1.187.0",
        "aws-cdk.aws-route53==1.187.0",
        "aws-cdk.aws-s3-assets==1.187.0",
        "aws-cdk.aws-s3==1.187.0",
        "aws-cdk.aws-secretsmanager==1.187.0",
        "aws-cdk.aws-servicediscovery==1.187.0",
        "aws-cdk.aws-sns==1.187.0",
        "aws-cdk.aws-sqs==1.187.0",
        "aws-cdk.aws-ssm==1.187.0",
        "aws-cdk.core==1.187.0",
        "aws-cdk.cx-api==1.187.0",
        "constructs>=3.3.69, <4.0.0",
        "jsii>=1.72.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
