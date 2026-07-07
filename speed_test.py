import subprocess
import json
import os
import sys
import tempfile
import shutil

CREATE_NO_WINDOW = 0x08000000


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def run_speed_test():
    try:
        speedtest_path = os.path.join(
            tempfile.gettempdir(),
            "speedtest.exe"
        )

        if not os.path.exists(speedtest_path):
            shutil.copy(
                resource_path("speedtest.exe"),
                speedtest_path
            )

        result = subprocess.run(
            [
                speedtest_path,
                "--accept-license",
                "--accept-gdpr",
                "--format=json"
            ],
            capture_output=True,
            text=True,
            timeout=120,
            creationflags=CREATE_NO_WINDOW
        )

        for line in result.stdout.splitlines():
            if '"type":"result"' in line:
                data = json.loads(line)

                download = (
                    data["download"]["bandwidth"] * 8 / 1000000
                )
                upload = (
                    data["upload"]["bandwidth"] * 8 / 1000000
                )
                ping = data["ping"]["latency"]

                return download, upload, ping

        return None, None, None

    except Exception as e:
        print("Speed Test Error:", e)
        return None, None, None