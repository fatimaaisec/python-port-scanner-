import socket

target = input("Enter target IP or website: ")

print(f"\nScanning target: {target}")
print("Please wait...\n")

for port in range(1, 1025):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    scanner.close()

print("\nScan completed.")
