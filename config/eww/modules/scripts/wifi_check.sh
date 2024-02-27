#!/bin/bash

# Check if Wi-Fi is on
if nmcli radio wifi | grep -q "enabled"; then
    echo "true"
else
    echo "false"
fi
