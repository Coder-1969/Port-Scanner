import os

def ping_scan(ip, ipv6=False):
    if ipv6:
        response = os.system(f"ping6 -c 1 {ip}" if os.name != "nt" else f"ping -6 -n 1 {ip}")
    else:
        response = os.system(f"ping -c 1 {ip}" if os.name != "nt" else f"ping -n 1 {ip}")
    
    return 'Alive' if response == 0 else 'Unreachable'
