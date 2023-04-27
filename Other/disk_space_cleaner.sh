#!/bin/bash

# Set the threshold percentage (e.g., 80% full)
THRESHOLD=80

# Set the target partition (e.g., /dev/sda1)
PARTITION="/dev/sda1"

# Get the current disk usage percentage
CURRENT_USAGE=$(df -h | grep "$PARTITION" | awk '{ print $5 }' | sed 's/%//')

# Check if the current usage is greater than the threshold
if [ "$CURRENT_USAGE" -gt "$THRESHOLD" ]; then
  echo "Disk space is low. Running Docker cleanup..."

  # Remove stopped containers
  docker container prune -f

  # Remove unused images
  docker image prune -a -f

  # Remove unused volumes
  docker volume prune -f

  # Remove unused networks
  docker network prune -f

  echo "Docker cleanup complete."
else
  echo "Disk space is within acceptable limits."
fi
