import socket
import sys
from datetime import datetime

# Define authorized targets strictly as per assignment instructions
AUTHORIZED_TARGETS = ['127.0.0.1', 'localhost', 'scanme.nmap.org']

def scan_ports(target, start_port, end_port):
    """
    Scans a range of ports on a target IP.
    """
    # Validate target for ethical compliance
    if target not in AUTHORIZED_TARGETS:
        print(f"[WARNING] scanning {target} is NOT authorized for this assignment.")
        print(f"Allowed targets: {AUTHORIZED_TARGETS}")
        return

    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        # Resolve hostname to IP if necessary
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")
        return

    try:
        for port in range(start_port, end_port + 1):
            # Create a socket for each port check
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout so we don't hang on closed ports
            s.settimeout(0.5) 
            
            # connect_ex returns 0 if connection is successful (Port Open)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[OPEN] Port {port} is OPEN")
            else:
                # Uncomment the line below if you want to see closed ports (can be spammy)
                # print(f"[CLOSED] Port {port} is closed")
                pass
            
            s.close()

    except KeyboardInterrupt:
        print("\n[EXIT] Exiting program...")
        sys.exit()
    except socket.error:
        print("[ERROR] Could not connect to server.")
        sys.exit()

    print("-" * 50)
    print(f"Scan completed at: {datetime.now()}")

if __name__ == "__main__":
    # Test Case 1: Scanning Localhost Common Ports
    print("\n--- TEST CASE 1: Localhost Common Ports ---")
    scan_ports('127.0.0.1', 20, 80)

    # Test Case 2: Scanning scanme.nmap.org (Limited range)
    print("\n--- TEST CASE 2: scanme.nmap.org ---")
    scan_ports('scanme.nmap.org', 20, 80)
    
    # Test Case 3: Error Handling (Unauthorized Host)
    print("\n--- TEST CASE 3: Unauthorized Host Check ---")
    scan_ports('google.com', 80, 80)