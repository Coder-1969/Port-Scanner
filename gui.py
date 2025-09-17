import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import tcp_scan
import udp_scan
import syn_scan
import ping_scan
import os_detection
import banner_grabber
import threading
import socket
import csv

root = tk.Tk()
root.title("Port Scanner GUI")
root.geometry("700x500")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Target IP Address:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ip_entry = ttk.Entry(frame, width=30)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Port Range (e.g., 1-100):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
port_range_entry = ttk.Entry(frame, width=15)
port_range_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Scan Type:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
scan_type = ttk.Combobox(frame, values=["TCP Scan", "UDP Scan", "SYN Scan", "Ping Scan", "OS Detection"])
scan_type.grid(row=2, column=1, padx=5, pady=5)
scan_type.current(0)

def is_ipv6(ip):
    try:
        socket.inet_pton(socket.AF_INET6, ip)
        return True
    except socket.error:
        return False

# Start Scan Function
def start_scan():
    ip_input = ip_entry.get().strip()  # Get user input & remove spaces
    scan = scan_type.get()
    ports = port_range_entry.get()

    if not ip_input:
        messagebox.showerror("Error", "Please enter at least one IP address.")
        return

    ip_addresses = [ip.strip() for ip in ip_input.split(",") if ip.strip()]  # Allow multiple IPs

    def is_ipv6(ip):
        try:
            socket.inet_pton(socket.AF_INET6, ip)
            return True
        except socket.error:
            return False

    ports_list = []
    if scan != "OS Detection":
        if not ports:
            messagebox.showerror("Error", "Please enter a valid port range.")
            return
        try:
            port_start, port_end = map(int, ports.split("-"))
            ports_list = list(range(port_start, port_end + 1))
        except ValueError:
            messagebox.showerror("Error", "Invalid port range format. Use 'start-end' (e.g., 1-100).")
            return

    scan_results.delete(*scan_results.get_children())  # Clear previous results

    def perform_scan():
        for ip in ip_addresses:
            ipv6 = is_ipv6(ip)  # Detect IPv4 or IPv6

            try:
                os_results = os_detection.os_detect(ip)
                scan_results.insert("", "end", values=[ip, os_results[0][1], "OS Detection"], tags=("os_detected",))
            except Exception as e:
                scan_results.insert("", "end", values=[ip, f"OS Detection Failed: {e}", "OS Detection"])

            results = []
            if scan == "TCP Scan":
                results = tcp_scan.tcp_scan(ip, ports_list, ipv6=ipv6)
            elif scan == "UDP Scan":
                results = udp_scan.udp_scan(ip, ports_list, ipv6=ipv6)
            elif scan == "SYN Scan":
                results = syn_scan.syn_scan(ip, ports_list, ipv6=ipv6)
            elif scan == "Ping Scan":
                status = ping_scan.ping_scan(ip)
                results = [[ip, status, "Ping"]]
            else:
                results = []

            for res in results:
                try:
                    port, state, protocol = res
                    if isinstance(port, int) and state.lower() == "open":
                        banner = banner_grabber.grab_banner(ip, port)
                        res_with_banner = [port, f"{state} ({banner})", protocol]
                        scan_results.insert("", "end", values=res_with_banner, tags=("open_port",))
                    else:
                        scan_results.insert("", "end", values=res)
                except Exception as e:
                    scan_results.insert("", "end", values=[ip, f"Error: {str(e)}", scan])

    # **Start the thread properly**
    threading.Thread(target=perform_scan, daemon=True).start() 




ttk.Button(frame, text="Start Scan", command=start_scan).grid(row=3, column=1, pady=10)

# Table definition 
columns = ("Port/IP", "State/Service", "Protocol")
scan_results = ttk.Treeview(frame, columns=columns, show="headings")
scan_results.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')
frame.rowconfigure(4, weight=1)
frame.columnconfigure((0,1), weight=1)

for col in columns:
    scan_results.heading(col, text=col)
    scan_results.column(col, width=150, anchor="center")

port_range_entry = ttk.Entry(frame, width=15)
port_range_entry.grid(row=1, column=1, padx=5, pady=5)

# Save Results to File function
def save_results(file_type):
    file = filedialog.asksaveasfilename(defaultextension=f".{file_type}",
                                        filetypes=[(f"{file_type.upper()} files", f"*.{file_type}")])
    if not file:
        return
    with open(file, "w", newline="") as f:
        if file_type == "csv":
            writer = csv.writer(f)
            writer.writerow(["Port/IP", "State/OS", "Protocol"])
            for row in scan_results.get_children():
                writer.writerow(scan_results.item(row)["values"])
        else:
            for row in scan_results.get_children():
                data = scan_results.item(row)["values"]
                f.write("\t".join(map(str, data)) + "\n")

ttk.Button(frame, text="Save as CSV", command=lambda: save_results("csv")).grid(row=5, column=0, pady=5)
ttk.Button(frame, text="Save as TXT", command=lambda: save_results("txt")).grid(row=5, column=1, pady=5)

# GUI event loop
root.mainloop()
