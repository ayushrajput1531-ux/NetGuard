import os


def get_scan_history():

    if not os.path.exists("scan_history.txt"):
        return "❌ No Scan History Found."

    with open(
        "scan_history.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()