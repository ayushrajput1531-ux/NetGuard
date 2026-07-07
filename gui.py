import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading

import os
import sys

from internet_check import check_internet
from ip_checker import get_private_ip
from dns_checker import dns_lookup
from public_ip import get_public_ip
from ping_test import ping_test, get_packet_loss
from port_scanner import scan_port
from speed_test import run_speed_test
from health_score import calculate_health_score
from pdf_report import save_pdf_report
from wifi_info import get_wifi_info
from network_adapter import get_network_adapters
from scan_history import save_scan_history
from system_info import (
    get_hostname,
    get_os,
    get_os_version,
    get_architecture,
    get_username
)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def update_progress(value):
    progress["value"] = value
    progress_label.config(text=f"{value}%")
    root.update_idletasks()


def run_speed_test_gui():
    output_box.insert(
        tk.END,
        "\n⚡ Running Speed Test...\n"
    )

    download, upload, ping = run_speed_test()

    if download is not None:
        output_box.insert(
            tk.END,
            f"\n⬇ Download Speed : {download:.2f} Mbps\n"
        )

        output_box.insert(
            tk.END,
            f"⬆ Upload Speed   : {upload:.2f} Mbps\n"
        )

        output_box.insert(
            tk.END,
            f"📶 Speed Test Ping : {ping:.2f} ms\n"
        )

        packet_loss = get_packet_loss("google.com")

        output_box.insert(
    tk.END,
    f"📦 Packet Loss : {packet_loss}%\n"
)

        health_score = calculate_health_score(
            True,
            True,
            ping,
            download,
            upload,
            packet_loss
        )
        save_scan_history(
    health_score,
    download,
    upload,
    ping,
    True
)

        output_box.insert(
            tk.END,
            f"\n🏥 Network Health Score : {health_score}/100\n"
        )

        if health_score >= 90:
            status = "🟢 Excellent"
        elif health_score >= 70:
            status = "🟡 Good"
        elif health_score >= 50:
            status = "🟠 Average"
        else:
            status = "🔴 Poor"

        output_box.insert(
            tk.END,
            f"Status : {status}\n"
        )

    else:
        output_box.insert(
            tk.END,
            "\n❌ Speed Test Failed\n"
        )

    update_progress(100)
    output_box.see(tk.END)


def run_scan():
    update_progress(0)
    output_box.delete(1.0, tk.END)

    # Internet Check
    internet = check_internet()
    private_ip = get_private_ip()

    update_progress(15)

    output_box.insert(
        tk.END,
        "========== NetGuard ==========\n\n"
    )

    if internet:
        output_box.insert(
            tk.END,
            "✅ Internet Connected\n"
        )
    else:
        output_box.insert(
            tk.END,
            "❌ No Internet Connection\n"
        )

    output_box.insert(
        tk.END,
        f"\n🌐 Private IP Address : {private_ip}\n"
    )

    # DNS Lookup
    domain_ip = dns_lookup("google.com")

    update_progress(35)

    if domain_ip:
        output_box.insert(
            tk.END,
            f"\n🌍 DNS Lookup:\n"
            f"google.com → {domain_ip}\n"
        )
    else:
        output_box.insert(
            tk.END,
            "\n❌ DNS Lookup Failed\n"
        )

    # Public IP
    public_ip = get_public_ip()

    update_progress(50)

    output_box.insert(
        tk.END,
        f"\n🌍 Public IP Address : {public_ip}\n"
    )
    # System Information
    hostname = get_hostname()
    os_name = get_os()
    os_version = get_os_version()
    architecture = get_architecture()
    username = get_username()

    output_box.insert(
    tk.END,
    "\n💻 System Information\n"
)

    output_box.insert(
    tk.END,
    f"💻 Hostname         : {hostname}\n"
)

    output_box.insert(
    tk.END,
    f"🖥 Operating System : {os_name}\n"
)

    output_box.insert(
    tk.END,
    f"⚙ OS Version       : {os_version}\n"
)

    output_box.insert(
    tk.END,
    f"🏗 Architecture     : {architecture}\n"
)

    output_box.insert(
    tk.END,
    f"👤 Current User     : {username}\n"
)

# Wi-Fi Information
    output_box.insert(
    tk.END,
    "\n📶 Wi-Fi Information\n\n"
)

    wifi_info = get_wifi_info() 
    output_box.insert(
    tk.END,
    wifi_info + "\n"
)

    update_progress(60)
    # Network Adapter Information
    output_box.insert(
    tk.END,
    "\n🌐 Network Adapter Information\n\n"
)

    adapter_info = get_network_adapters()

    output_box.insert(
    tk.END,
    adapter_info + "\n"
)

    update_progress(65)
    # Ping Test
    output_box.insert(
        tk.END,
        "\n📡 Running Ping Test to google.com...\n\n"
    )
  
    ping_result = ping_test("google.com")

    output_box.insert(
        tk.END,
        ping_result + "\n"
    )

    update_progress(70)

    # Port Scanner
    output_box.insert(
        tk.END,
        "\n🔍 Scanning Common Ports...\n\n"
    )

    ports = {
        80: "HTTP",
        443: "HTTPS",
        22: "SSH",
        53: "DNS"
    }

    for port, service in ports.items():
        status = scan_port(
            "127.0.0.1",
            port
        )

    output_box.insert(
            tk.END,
            f"Port {port} ({service}) : {status}\n"
    )

    update_progress(85)

    output_box.insert(
        tk.END,
        "\n========== Basic Scan Complete ==========\n"
    )

    output_box.see(tk.END)

    threading.Thread(
        target=run_speed_test_gui,
        daemon=True
    ).start()

def clear_output():
     output_box.delete(1.0, tk.END)
     update_progress(0)

def toggle_theme():
    global dark_mode

    if not dark_mode:

        root.configure(bg="#2b2b2b")
        button_frame.configure(bg="#2b2b2b")
        frame.configure(bg="#2b2b2b")

        title_label.configure(
            bg="#2b2b2b",
            fg="white"
        )

        progress_label.configure(
            bg="#2b2b2b",
            fg="white"
        )

        output_box.configure(
            bg="#1e1e1e",
            fg="white",
            insertbackground="white"
        )

        dark_mode = True

    else:

        root.configure(bg="SystemButtonFace")
        button_frame.configure(bg="SystemButtonFace")
        frame.configure(bg="SystemButtonFace")

        title_label.configure(
            bg="SystemButtonFace",
            fg="black"
        )

        progress_label.configure(
            bg="SystemButtonFace",
            fg="black"
        )

        output_box.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        dark_mode = False


def save_report():

    report = output_box.get(
        1.0,
        tk.END
    )

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[
            ("PDF Files", "*.pdf"),
            ("Text Files", "*.txt")
        ]
    )

    if file_path:

        if file_path.endswith(".pdf"):
            save_pdf_report(
                report,
                file_path
            )

        else:
            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(report)
            from tkinter import messagebox

def show_about():

         messagebox.showinfo(

        "About NetGuard",

        "NetGuard v1.0\n\n"
        "Developer : Ayush Rajput\n\n"
        "A Professional Network Diagnostic Tool\n\n"
        "Features:\n"
        "• Internet Check\n"
        "• DNS Lookup\n"
        "• Private/Public IP\n"
        "• Speed Test\n"
        "• Ping Test\n"
        "• Packet Loss\n"
        "• Port Scanner\n"
        "• Health Score\n"
        "• System Information\n"
        "• Wi-Fi Information\n"
        "• Network Adapter Information\n"
        "• PDF/TXT Report\n\n"
        "© 2026 NetGuard"
    )


# GUI Window
root = tk.Tk()
root.iconbitmap(resource_path("netguard.ico"))
root.title("NetGuard")
root.geometry("750x620")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="NetGuard Network Diagnostic Tool",
    font=("Arial", 18)
)
title_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

scan_button = tk.Button(
    button_frame,
    text="Run Scan",
    font=("Arial", 14),
    command=run_scan
)
scan_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 14),
    command=clear_output
)
clear_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(
    button_frame,
    text="Save Report",
    font=("Arial", 14),
    command=save_report
)
save_button.pack(side=tk.LEFT, padx=10)
theme_button = tk.Button(
    button_frame,
    text="🌙 Dark Mode",
    font=("Arial", 14),
    command=toggle_theme
)

theme_button.pack(
    side=tk.LEFT,
    padx=10
)
about_button = tk.Button(
    button_frame,
    text="About",
    font=("Arial", 14),
    command=show_about
)

about_button.pack(
    side=tk.LEFT,
    padx=10
)

# Progress Bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=500,
    mode="determinate"
)
progress.pack(pady=10)

progress_label = tk.Label(
    root,
    text="0%",
    font=("Arial", 12)
)
progress_label.pack()
version_label = tk.Label(
    root,
    text="NetGuard v1.0",
    font=("Arial", 10),
    fg="gray"
)

version_label.pack(pady=5)

# Output Frame
frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_box = tk.Text(
    frame,
    height=22,
    width=90,
    yscrollcommand=scrollbar.set
)
output_box.pack(side=tk.LEFT)

scrollbar.config(
    command=output_box.yview
)

root.mainloop()