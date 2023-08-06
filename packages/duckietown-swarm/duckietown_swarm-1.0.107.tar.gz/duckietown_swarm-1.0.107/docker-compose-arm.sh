#!/bin/bash
set -e
set -x

HOST=tl47.local

docker-compose\
    --host tcp://$HOST:2375 \
    -f docker-compose-arm.yaml \
    pull
    
docker-compose\
    --host tcp://$HOST:2375 \
    -f docker-compose-arm.yaml \
    up
