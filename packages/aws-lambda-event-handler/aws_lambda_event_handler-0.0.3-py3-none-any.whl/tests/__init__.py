"""
Copyright 2018 Conijn.io. or its affiliates. All Rights Reserved.
"""
import logging

## Enable logging to a file
logging.basicConfig(filename='testing.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
