#!/bin/bash

# Get the Nginx web server's memory usage
nginx_memory_usage=$(ps -aux | grep nginx | awk '{print $4}')

# If the Nginx web server's memory usage exceeds 512MB, restart it
if [[ $nginx_memory_usage -lt 512000 ]]; then
  sudo systemctl restart nginx
fi
