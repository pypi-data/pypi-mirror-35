#!/usr/bin/env python
# coding: utf-8
"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_lambda_event_handler",
    version="0.0.3",
    author='Joris Conijn',
    author_email='joris@conijnonline.nl',
    description="This package provides a decorator for Python Lambda functions handling AWS Lambda Event Records.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nr18/aws-lambda-event-handler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)