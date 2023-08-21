#!/bin/bash
# download images and recreate containers if images were new or if docker-compose.yml was changed == smart recreation
# can be used in cron
docker-compose pull
docker-compose up -d --build