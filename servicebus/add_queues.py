#!/usr/bin/python3
import re
import sys
import yaml
from azure.servicebus import ServiceBusService

print("Passed argument: {0}".format(sys.argv[0]))
setup_file = '/mount/sb/setup.yaml'

with open(setup_file) as f:
    setup = yaml.load(f.read())

print("Queue setup '{0}'".format(setup))

matchObj = re.match(r'Endpoint=sb://(.*);SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=(.*)$',
                    sys.argv[0],
                    re.M | re.I)
if matchObj:
    namespace = matchObj.group(1)
    secret = matchObj.group(2)

    sbs = ServiceBusService(namespace,
                            shared_access_key_name='RootManageSharedAccessKey',
                            shared_access_key_value=secret)
    for queue in setup.queues:
        sbs.create_queue('queue')
    sys.exit(0)
else:
    print("Failed to get the right connection string from the service bus {0}".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
