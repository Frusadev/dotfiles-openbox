#!/bin/bash

# Use the 'nmcli' command to get a list of available Wi-Fi SSIDs without connecting
wifi_list=$(nmcli -t -f SSID device wifi rescan | nmcli -t -f SSID device wifi list)

# Initialize an empty string to store the formatted output
output=""

# Loop through each SSID and append it to the output string in the specified format
for ssid in $wifi_list; do
  output+="(button
              :class \"wifi-li-btn\" 
              :onclick \"eww update wifi_ssid='$ssid' & eww open wifi_connect\" 
              (label :text \"$ssid\"))"
done

# Echo the formatted output on a single line
echo "(box" $output ")"
