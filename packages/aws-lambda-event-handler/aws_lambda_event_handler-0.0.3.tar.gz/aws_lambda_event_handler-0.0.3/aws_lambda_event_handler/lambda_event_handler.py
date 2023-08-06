"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
from .models.sns_message import SNSMessage
from .log import LOG


class LambdaEventHandler:
    """
    AWS Lambda Handler
    """
    def __init__(self):
        self._handlers = dict()

    @staticmethod
    def event_source(record, source=None) -> str:
        """
        Return the event source of the record, The event records not always have consistant casing
        so we check all known variants.
        """
        if 'EventSource' in record:
            source = record['EventSource']
        elif 'eventSource' in record:
            source = record['eventSource']

        return source

    def __call__(self, event, context):
        """
        Handle the invokation of the lambda function and map each record to the record handler.
        """
        def handle_record(record):
            """
            Lookup a registered function that we can use for this record.
            """
            event_source = self.event_source(record)
            func = self.get_handler(event_source)

            if func is not None:
                func(record, context)
            else:
                LOG.info('No handler registered for the %s event source', event_source)

        if 'Records' in event:
            list(map(handle_record, event['Records']))

    def get_handler(self, event_source):
        """
        Return the registered handler
        """
        return self._handlers.get(event_source)

    def sns(self, func):
        """
        Public SNS Decorator
        """
        def sns_handler(func) -> func:
            """
            SNS Handler
            """
            def decorator(record, context):
                """
                SNS Decorator
                """
                func(SNSMessage(record), context)

            return decorator

        self._handlers['aws:sns'] = sns_handler(func)

    def dynamodb(self, func) -> None:
        """
        DynamoDB Decorator
        """
        self._handlers['aws:dynamodb'] = func
