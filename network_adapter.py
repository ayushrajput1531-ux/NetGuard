import psutil
import socket


def get_network_adapters():

    adapters = []

    addresses = psutil.net_if_addrs()

    for interface, addr_list in addresses.items():

        adapters.append(f"\n🔹 Adapter : {interface}")

        for addr in addr_list:

            if addr.family == socket.AF_INET:
                adapters.append(f"IPv4 Address : {addr.address}")

            elif addr.family == socket.AF_INET6:
                adapters.append(f"IPv6 Address : {addr.address}")

            elif hasattr(psutil, "AF_LINK") and addr.family == psutil.AF_LINK:
                adapters.append(f"MAC Address  : {addr.address}")

    return "\n".join(adapters)