#!/bin/bash

# Function to determine if a WiFi is secure
is_secure() {
    local security="$1"
    [[ "$security" =~ (WEP|WPA|WPA2) ]] && echo "true" || echo "false"
}

# Scan for WiFi networks using nmcli
wifi_list=$(nmcli --fields SSID,SECURITY device wifi list ifname wlan0) 

# Iterate over each WiFi, generating formatted output
while IFS= read -r line; do
    ssid=$(echo "$line" | awk '{print $1}' | sed 's/--\|WEP\|WPA2//g')  
    security=$(echo "$line" | awk '{print $2}')

    # Skip empty SSIDs and "--" entries
    if [[ -n "$ssid" ]] && [[ "$ssid" != "--" ]]; then
        # Enclose SSID in quotes to preserve spaces
        output_string+="(wifi-element :ssid \"$ssid\" :secure $(is_secure "$security"))"
    fi
done <<< "$wifi_list" 

# Output the formatted string
echo "$output_string"
