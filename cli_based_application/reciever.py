import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP - user datagram protocol
# ip_address = "192.168.1.64"
ip_address = "127.0.0.1"
port_no = 2525 

complete_address = (ip_address,port_no)

s.bind(complete_address)

print("HEY i AM LISTENING ...")
while True:
    message = s.recvfrom(100)
    print(message)