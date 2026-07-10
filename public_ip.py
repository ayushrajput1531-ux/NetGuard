import requests


def get_public_ip():
    try:
        ip = requests.get(
            "https://api.ipify.org"
        ).text

        geo = requests.get(
            f"http://ip-api.com/json/{ip}"
        ).json()

        return {
            "ip": ip,
            "country": geo.get("country", "N/A"),
            "region": geo.get("regionName", "N/A"),
            "city": geo.get("city", "N/A"),
            "isp": geo.get("isp", "N/A"),
            "timezone": geo.get("timezone", "N/A")
        }

    except Exception:
        return None