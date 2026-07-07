import subprocess


def get_wifi_info():

    try:

        result = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        data = {}

        for line in result.splitlines():

            if ":" in line:

                key, value = line.split(":", 1)

                data[key.strip()] = value.strip()

        info = (
            f"SSID             : {data.get('SSID', 'N/A')}\n"
            f"Signal           : {data.get('Signal', 'N/A')}\n"
            f"Radio Type       : {data.get('Radio type', 'N/A')}\n"
            f"Authentication   : {data.get('Authentication', 'N/A')}\n"
            f"Channel          : {data.get('Channel', 'N/A')}\n"
            f"Receive Rate     : {data.get('Receive rate (Mbps)', 'N/A')} Mbps\n"
            f"Transmit Rate    : {data.get('Transmit rate (Mbps)', 'N/A')} Mbps\n"
        )

        return info

    except Exception:

        return "Wi-Fi Information Not Available"