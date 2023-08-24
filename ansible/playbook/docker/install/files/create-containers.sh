#!/bin/bash
cd "$(dirname "$0")"
docker-compose pull --ignore-pull-failures
docker-compose down
docker-compose up -d