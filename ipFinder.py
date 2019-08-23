import socket
sd = input("Enter the URL to Find the IP Address")
k = socket.gethostbyname(sd)
print(k)
