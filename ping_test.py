import subprocess
import platform
import re


def ping_test(host):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", parameter, "4", host]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.stdout


def get_packet_loss(host):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", parameter, "4", host]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    output = result.stdout

    if platform.system().lower() == "windows":
        match = re.search(r"(\d+)% loss", output)
    else:
        match = re.search(r"(\d+(\.\d+)?)% packet loss", output)

    if match:
        return float(match.group(1))

    return 100