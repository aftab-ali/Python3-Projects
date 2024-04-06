import sys
import socket
from datetime import datetime


# Define your target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Arguments.")
    print("Syntax: python3 portscanner.py <ip>")

# Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        results = s.connect_ex((target,port))
        if results == 0:
            print(f"Port {port} is Open.")
        s.close()
    print("\nTime Stopped. " + str(datetime.now()))
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could not be Resolved.")
    sys.exit()
except socket.error:
    print("\nCould not Connect to the Server.")
    sys.exit()


