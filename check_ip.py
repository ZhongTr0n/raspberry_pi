import socket
import datetime


current_IP = "0.0.0.0"
print(current_IP)

while True:
    new_IP = socket.gethostbyname(socket.gethostname())
    now = datetime.datetime.now()
    if new_IP != current_IP:
        print("The new IP is: {}".format(new_IP))
        print("Change took place at: {}".format(now))
        print("")
        current_IP = new_IP

