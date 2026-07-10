import subprocess
import re


def get_wifi_info():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            encoding="utf-8",
            errors="ignore"
        )

        ssid = "Unknown"
        signal = "Unknown"

        for line in result.splitlines():

            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()

            if "Signal" in line:
                signal = line.split(":")[1].strip()

        return ssid, signal

    except Exception:
        return "Not Connected", "0%"