import socket
import threading
from datetime import datetime

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Proxy"
}

open_ports = []
lock = threading.Lock()


def scan_port(ip, port):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        result = scanner.connect_ex((ip, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")

            with lock:
                print(f"[OPEN] Port {port} - {service}")
                open_ports.append((port, service))

        scanner.close()

    except:
        pass


def scan_target(target):
    print("\n" + "=" * 50)
    print(f"Scanning Target: {target}")
    print(f"Started at: {datetime.now()}")
    print("=" * 50)

    try:
        ip = socket.gethostbyname(target)

        threads = []

        for port in range(1, 1025):
            t = threading.Thread(target=scan_port, args=(ip, port))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    except socket.gaierror:
        print("Invalid target hostname.")

    print("\nScan completed.")
    save_results(target)


def save_results(target):
    filename = f"scan_results_{target}.txt"

    with open(filename, "w") as file:
        file.write("Open Ports:\n")
        file.write("=" * 30 + "\n")

        for port, service in open_ports:
            file.write(f"{port} - {service}\n")

    print(f"Results saved to {filename}")


target = input("Enter target IP or website: ")
scan_target(target)
