import urllib.request

def get_public_ip():
    try:
        public_ip = urllib.request.urlopen(
            "https://api.ipify.org"
        ).read().decode("utf8")

        return public_ip

    except:
        return "Unable to fetch Public IP"