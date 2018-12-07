#!/usr/bin/python3
import re
import sys
import yaml
from azure.servicebus import ServiceBusService

print("Passed argument: {0}".format(sys.argv[1]))
connection_string = sys.argv[1]
setup_file = '/mount/sb/setup.yaml'

with open(setup_file) as f:
    setup = yaml.load(f.read())
print("Queue setup '{0}'".format(setup))
matchObj = re.match('Endpoint=sb://(.*).servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=(.*)$',
                    connection_string,
                    re.M | re.I)
if matchObj:
    namespace = matchObj.group(1)
    secret = matchObj.group(2)

    sbs = ServiceBusService(namespace,
                            shared_access_key_name='RootManageSharedAccessKey',
                            shared_access_key_value=secret)
    for queue in setup.get('queues'):
        sbs.create_queue(queue)
    sys.exit(0)
else:
    print("Failed to get the right connection string from the service bus {0}".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
