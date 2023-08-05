"""
Various utilities
"""

import socket
import sys
import time

def is_port_open(host, port, timeout = 0.5):
    'Checks if a connection to the specified host and port can be established'
    'True if the host/port is open, False if the timeout is reached'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))

    return result == 0

def wait_for_port_to_open(host, port, timeout):
    'Wait for port to open and return True if successful; time out after the specified duration'
    time0 = time.time()
    while not is_port_open(host=host, port=port, timeout = 0.5):
        # Stop, if timeout is reached
        if time.time() - time0 >= timeout:
            return False
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

    return True
