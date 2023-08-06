"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.

Fixtures for the tests
"""
import datetime
from typing import Dict
import uuid
import pytest
TIMESTAMP = datetime.datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'

@pytest.fixture()
def sns_event(message='',
              topic='arn:aws:sns:region:**:Topic',
              attributes=None) -> Dict:
    """
    Fixture to generate a SNS Event
    """
    if attributes is None:
        attributes = {}

    return {
        'EventSource': 'aws:sns',
        "Sns": {
            "Type": "Notification",
            "MessageId": uuid.uuid4(),
            "TopicArn": topic,
            "Subject": "",
            "Message": message,
            "Timestamp": TIMESTAMP,
            "SignatureVersion": "1",
            "Signature": "mysignature",
            "SigningCertUrl": "https://sns.region.amazonaws.com/",
            "UnsubscribeUrl": "https://sns.eu-west-1.amazonaws.com/",
            "MessageAttributes": attributes
        }
    }

@pytest.fixture()
def dynamodb_event() -> Dict:
    """
    Fixture to generate a DynamoDB Event
    """
    return {
        'eventSource': 'aws:dynamodb'
    }

@pytest.fixture()
def custom_event() -> Dict:
    """
    Fixture to generate a Custom Event
    """
    return {
        'eventSource': 'aws:custom'
    }
