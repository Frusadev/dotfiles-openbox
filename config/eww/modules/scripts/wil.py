import subprocess

def is_secure(security):
    """Determines if a WiFi network is secure."""
    return security in ("WEP", "WPA", "WPA2")

def get_wifi_list():
    """Scans for WiFi networks using nmcli."""
    result = subprocess.run(
        ["nmcli", "--fields", "SSID,SECURITY", "device", "wifi", "list", "ifname", "wlan0"],
        capture_output=True,
        text=True
    )

    wifi_data = []
    for line in result.stdout.splitlines()[1:]:  # Skip the header line
        ssid, security = line.split()
        if ssid != "--":  # Filter out "--" entries
            wifi_data.append((ssid, security))

    return wifi_data

# Main scanning and output generation
if __name__ == "__main__":
    wifi_list = get_wifi_list()
    wifi_elements = []

    for ssid, security in wifi_list:
        wifi_elements.append(f"(wifi-element :ssid \"{ssid}\" :secure {is_secure(security)})")

    print(wifi_elements)
