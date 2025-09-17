import socket
import threading
import concurrent.futures

def udp_scan(ip, ports, ipv6=False, max_threads=50):
    output = []
    lock = threading.Lock()

    def scan_port(port):
        family = socket.AF_INET6 if ipv6 else socket.AF_INET
        sock = socket.socket(family, socket.SOCK_DGRAM)
        sock.settimeout(1)
        try:
            sock.sendto(b"\x00", (ip, port))
            sock.recvfrom(1024)
            state = 'Open'
        except socket.timeout:
            state = 'Filtered/Closed'
        except Exception as e:
            state = f'Error: {str(e)}'
        finally:
            sock.close()

        with lock:
            output.append([port, state, 'UDP'])

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan_port, ports)

    return output
