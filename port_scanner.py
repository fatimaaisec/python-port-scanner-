import socket
from datetime import datetime

# Common ports and services
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


def scan_ports(target):
    print("\n" + "=" * 50)
    print(f"Scanning Target: {target}")
    print(f"Started at: {datetime.now()}")
    print("=" * 50)

    open_ports = []

    try:
        ip = socket.gethostbyname(target)

        for port in range(1, 1025):
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.settimeout(0.3)

            result = scanner.connect_ex((ip, port))

            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown Service")

                print(f"[OPEN] Port {port} - {service}")
                open_ports.append((port, service))

            scanner.close()

    except socket.gaierror:
        print("Invalid target or hostname.")

    except KeyboardInterrupt:
        print("\nScan stopped by user.")

    except Exception as error:
        print("Error:", error)

    save_results(target, open_ports)

    print("\nScan Completed.")


def save_results(target, open_ports):
    filename = f"scan_results_{target}.txt"

    with open(filename, "w") as file:
        file.write(f"Scan Results for {target}\n")
        file.write("=" * 40 + "\n")

        for port, service in open_ports:
            file.write(f"Port {port} - {service}\n")

    print(f"\nResults saved to: {filename}")


target = input("Enter target IP or website: ")

scan_ports(target)
