#!/usr/bin/env bash -x
set -eu
echo "== Starting queue creation script == "
pip install azure-servicebus
pip install pyyaml
echo "Starting queue creation python script"
python /mount/sb/add_queues.py $1


