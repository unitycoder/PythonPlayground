import socket

# get IP address of this host (without extra plugins)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("google.com",80))
IP = s.getsockname()[0]
print IP
s.close()

