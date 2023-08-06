"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
import pytest
from aws_lambda_event_handler import SNSMessage
from aws_lambda_event_handler import LambdaHandlerException
from ..fixtures import sns_event

@pytest.mark.parametrize('event, exception', [
    (None, LambdaHandlerException),
    (sns_event(message='{"Foo": "Bar"}', attributes={'myKey': {'Value': 'myValue'}}), None)
])
def test_sns_message(event, exception):
    """
    LambdaHandlerException
    """
    if exception is None:
        message = SNSMessage(event)
        assert message.get_message() == event['Sns']['Message']
        assert message.get_attribute('myKey') == 'myValue'
        assert message.get_attribute('otherKey', 'otherValue') == 'otherValue'
        assert message.get_message_json() == '{"Foo": "Bar"}'
        assert message.get_message_object() == {"Foo": "Bar"}
    else:
        with pytest.raises(exception):
            message = SNSMessage(event)
