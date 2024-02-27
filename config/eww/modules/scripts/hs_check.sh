#!/bin/bash

# Check if hotspot is activated
if nmcli connection show --active | grep -q "Hotspot"; then
    echo "true"
else
    echo "false"
fi
