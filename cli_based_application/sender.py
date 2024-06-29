import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP - user datagram protocol

# target_ip = '192.168.1.64'  # my_ip 
target_ip = '127.0.0.1'
target_port = 2525   # my_port 

while True:
    message = input('Plz enter message : ')
    message = message.encode('ascii')
    s.sendto(message,(target_ip,target_port))
    print("Your message has been Successfully sent!")
