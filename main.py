from port_scanner import scan_port
from speed_test import run_speed_test
from health_score import calculate_health_score
from public_ip import get_public_ip
from dns_checker import dns_lookup
from internet_check import check_internet
from ip_checker import get_private_ip
from ping_test import ping_test

print("========== NetGuard ==========")

# Internet Check
internet_status = check_internet()

if internet_status:
    print("✅ Internet Connected")
else:
    print("❌ No Internet Connection")

# Private IP Address
private_ip = get_private_ip()
print(f"\n🌐 Your Private IP Address: {private_ip}")

# Ping Test
print("\n📡 Running Ping Test to google.com...\n")
result = ping_test("google.com")
print(result)

# DNS Lookup
print("\n🌍 Running DNS Lookup Test...\n")

domain_ip = dns_lookup("google.com")

if domain_ip:
    print(f"google.com resolves to: {domain_ip}")
    dns_status = True
else:
    print("❌ DNS Lookup Failed")
    dns_status = False

# Public IP
print("\n🌍 Detecting Public IP...\n")
public_ip = get_public_ip()
print(f"🌐 Your Public IP Address: {public_ip}")

# Speed Test
packet_loss = 0
print("\n⚡ Running Internet Speed Test...\n")

download, upload, speed_ping = run_speed_test()

if download is not None:
    print(f"⬇ Download Speed : {download:.2f} Mbps")
    print(f"⬆ Upload Speed   : {upload:.2f} Mbps")
    print(f"📶 Speed Test Ping : {speed_ping:.2f} ms")
else:
    print("❌ Speed Test Failed")
    download = 0
    speed_ping = 9999

# Health Score
health_score = calculate_health_score(
    internet_status,
    dns_status,
    speed_ping,
    download,
    upload,
    packet_loss
)

print(f"\n🏥 Network Health Score: {health_score}/100")

if health_score >= 90:
    print("🟢 Status: Excellent")
elif health_score >= 70:
    print("🟡 Status: Good")
elif health_score >= 50:
    print("🟠 Status: Average")
else:
    print("🔴 Status: Poor")

print("\n🔍 Scanning Common Ports on localhost...\n")

common_ports = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    53: "DNS"
}

for port, service in common_ports.items():
    status = scan_port("127.0.0.1", port)
    print(f"Port {port} ({service}) : {status}")
    
print("\n========== Scan Complete ==========")