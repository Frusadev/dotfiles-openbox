#!/bin/bash

# Check if Bluetooth is activated
if rfkill list bluetooth | grep -q "blocked: yes"; then
    echo "false"
else
    echo "true"
fi
