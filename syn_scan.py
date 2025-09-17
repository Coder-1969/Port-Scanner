from scapy.all import IP, IPv6, TCP, sr1, send

import threading

def syn_scan(ip, ports, ipv6=False):
    output = []
    lock = threading.Lock()

    def scan_port(port):
        pkt = (IPv6(dst=ip) if ipv6 else IP(dst=ip)) / TCP(dport=port, flags="S")
        response = sr1(pkt, timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                state = 'Open'
                send((IPv6(dst=ip) if ipv6 else IP(dst=ip)) / TCP(dport=port, flags="R"), verbose=0)
            elif response.getlayer(TCP).flags == 0x14:
                state = 'Closed'
            else:
                state = 'Filtered'
        else:
            state = 'Filtered/No Response'

        output.append([port, state, 'SYN'])

    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return output
