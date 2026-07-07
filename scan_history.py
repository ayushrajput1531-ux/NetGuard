from datetime import datetime


def save_scan_history(
    health_score,
    download_speed,
    upload_speed,
    ping,
    internet_status
):

    now = datetime.now()

    history = (
        f"\n{'=' * 50}\n"
        f"Date : {now.strftime('%d-%m-%Y')}\n"
        f"Time : {now.strftime('%I:%M:%S %p')}\n"
        f"Internet : {'Connected' if internet_status else 'Disconnected'}\n"
        f"Health Score : {health_score}/100\n"
        f"Download : {download_speed:.2f} Mbps\n"
        f"Upload : {upload_speed:.2f} Mbps\n"
        f"Ping : {ping:.2f} ms\n"
    )

    with open(
        "scan_history.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(history)