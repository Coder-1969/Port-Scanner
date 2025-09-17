import socket
import threading
import concurrent.futures

def tcp_scan(ip, ports, delay=0.5, ipv6=False, max_threads=50):
    output = []
    lock = threading.Lock()

    def scan_port(port):
        family = socket.AF_INET6 if ipv6 else socket.AF_INET
        sock = socket.socket(family, socket.SOCK_STREAM)
        sock.settimeout(delay)
        try:
            result = sock.connect_ex((ip, port))
            state = 'Open' if result == 0 else 'Closed'
        except Exception as e:
            state = f'Error: {str(e)}'
        finally:
            sock.close()

        with lock:
            output.append([port, state, 'TCP'])

    # Limit number of threads to avoid system overload
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan_port, ports)

    return output
