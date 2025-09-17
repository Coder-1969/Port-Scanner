import socket

def grab_banner(ip, port, timeout=2):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip, port))

        # First try to directly receive data (useful for SSH, FTP, SMTP)
        try:
            banner = sock.recv(1024).decode().strip()
            if banner:
                sock.close()
                return banner
        except socket.timeout:
            pass

        # For services that need input (e.g., HTTP)
        sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = sock.recv(1024).decode(errors='ignore').strip()
        sock.close()
        return banner if banner else 'No banner'
        
    except Exception as e:
        return f'No banner ({e})'

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    port = int(input("Enter Port: "))
    banner = grab_banner(ip, port)
    print(f"Port {port}: {banner}")
