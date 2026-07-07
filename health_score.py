def calculate_health_score(
    internet_status,
    dns_status,
    ping,
    download_speed,
    upload_speed,
    packet_loss
):
    score = 0

    # Internet Score
    if internet_status:
        score += 25

    # DNS Score
    if dns_status:
        score += 15

    # Ping Score
    if ping <= 50:
        score += 25
    elif ping <= 100:
        score += 15
    elif ping <= 200:
        score += 5

    # Download Speed Score
    if download_speed >= 50:
        score += 15
    elif download_speed >= 20:
        score += 10
    elif download_speed >= 10:
        score += 5

    # Upload Speed Score
    if upload_speed >= 20:
        score += 10
    elif upload_speed >= 10:
        score += 7
    elif upload_speed >= 5:
        score += 4

    # Packet Loss Score
    if packet_loss == 0:
        score += 10
    elif packet_loss <= 2:
        score += 5

    return score