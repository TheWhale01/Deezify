#!/bin/bash

python3 -m pip install -r requirements.txt --break-system-packages
fastapi dev src/main.py --port ${PORT} --host ${HOST}
