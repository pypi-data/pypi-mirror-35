"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
import pytest
from aws_lambda_event_handler import LambdaEventHandler, SNSMessage
from tests.fixtures import custom_event, sns_event, dynamodb_event

@pytest.mark.parametrize('event, resolved_source, default_source', [
    (sns_event(), 'aws:sns', None),
    (dynamodb_event(), 'aws:dynamodb', None),
    ({}, 'aws:custom', 'aws:custom'),
])
def test_event_source(event, resolved_source, default_source):
    """
    Test the event Source Conversion
    """
    assert LambdaEventHandler.event_source(event, source=default_source) == resolved_source

def test_handler():
    """
    Test the handler invokation
    """
    handler = LambdaEventHandler()

    @handler.sns
    def my_sns_handler(message, context): #pylint: disable=W0612,W0613
        """
        Mock a function
        """
        pass

    handler({
        'Records': [
            sns_event(),
            dynamodb_event(),
            custom_event()
        ]
    }, {})

def test_lambda_event_handler_sns():
    """
    Test a SNS EventSource
    """
    handler = LambdaEventHandler()

    @handler.sns
    def sns(message: SNSMessage, context) -> str: #pylint: disable=W0612,W0613
        """
        Sample implementation
        """
        assert message.get_message() == 'MyMessage'

    handler.get_handler('aws:sns')(sns_event(message='MyMessage'), {})

def test_lambda_event_handler_dynamodb():
    """
    Test a DynamoDB EventSource
    """
    handler = LambdaEventHandler()
    event = dynamodb_event()

    @handler.dynamodb
    def dynamodb(record, context) -> str: #pylint: disable=W0612,W0613
        """
        Sample implementation
        """
        assert event == record

    handler.get_handler('aws:dynamodb')(event, {})
