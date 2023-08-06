"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
import json
from typing import Dict
from ..log import LOG
from ..exceptions import LambdaHandlerException

class SNSMessage:
    """
    SNSMessage
    """
    _attributes: Dict[str, str] = {}
    _message: str = {}

    def __init__(self, message=None):
        """
        Constructor
        """
        LOG.debug('Received message: %s', message)

        def parse_attributes(key):
            """
            Parse the attributes in the SNS Message
            """
            self._attributes[key] = message['Sns']['MessageAttributes'][key]['Value']

        try:
            # Read the message
            self._message = message['Sns']['Message']

            # Read the message attributes
            list(map(parse_attributes, message['Sns']['MessageAttributes']))


        except Exception as err:
            raise LambdaHandlerException(err)

    def get_attribute(self, name, value=None) -> str:
        """
        Return the value of the given attribute
        """
        if name in self._attributes:
            return self._attributes[name]

        return value

    def get_message(self):
        """
        Returns the payload as a string
        """
        return self._message

    def get_message_object(self):
        """
        Returns the payload as a object
        """
        return json.loads(self.get_message())

    def get_message_json(self):
        """
        Returns the payload as a JSON string
        """
        return json.dumps(self.get_message_object())
