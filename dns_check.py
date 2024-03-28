import socket

# Define a function to check if port 53 is open for inbound access for a given IP address
def check_inbound_access(ip_address, port=53):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # Set a timeout of 10 seconds

    try:
        # Try to connect to the IP address on port 53
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed
    except socket.error as e:
        return False  # Connection failed
    finally:
        sock.close()


# Replace 'your_ip_address' with the actual IP address you want to check
ip_to_check = '192.168.1.110'

# Check if port 53 is open for inbound access and print the result
if check_inbound_access(ip_to_check):
    print(f"Port 53 is open for inbound access on IP address {ip_to_check}.")
else:
    print(f"Port 53 is not open for inbound access on IP address {ip_to_check}.")