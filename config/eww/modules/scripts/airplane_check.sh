#!/bin/bash

# Check if airplane mode is on
if nmcli radio all | grep -q "disabled"; then
    echo "true"
else
    echo "false"
fi
