#!/usr/bin/env bash
set -eu
pip install azure-servicebus
pip install pyyaml
python add_queues.py $1


