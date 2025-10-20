#!/bin/bash

# Start server
cd "$(dirname "$0")/app"
python main.py "$@"