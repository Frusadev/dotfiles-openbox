#!/bin/bash

output_string='(box :class "acdialog-elements" :orientation "v" :space-evenly "false" :haling "start" '

wifi_list=$(nmcli -f SSID,SECURITY device wifi list | tail -n +2)

while IFS= read -r line; do
    ssid=$(echo "$line" | awk '{print $1}' | sed 's/--\|WEP\|WPA2//g')  
    if [ "$ssid" != "--" ] && [ -n "$ssid" ]; then 
        security=$(echo "$line" | awk '{print $2}')

        is_secure="false"
        if [[ "$security" =~ (WEP|WPA|WPA2) ]]; then
            is_secure="true"
        fi

        output_string+="(wifi-element :ssid \"$ssid\" :secure $is_secure)"
    fi 
done <<< "$wifi_list"

output_string+=")"
echo "$output_string" 
