"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
from aws_lambda_event_handler import LambdaHandlerException

def test_lambda_handler_exception():
    """
    LambdaHandlerException
    """

    exception = LambdaHandlerException('message')

    assert str(exception) == 'message'
