current_ssid=$(iwgetid -r)

if [ -n "$current_ssid" ]; then
    echo "$current_ssid"
else
    echo "Disconnected"
fi
