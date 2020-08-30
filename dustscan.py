import socket
import pyfiglet
import os
os.system("clear")
print(pyfiglet.figlet_format("DUST SCAN"))
print("Created by Zin Yaw.")
print("[-1-] Scan using host name: ")
print("[-2-] Scan using IP address: ")
userchoice = input("Select an option > ")
if userchoice == "1":
    host = input("Enter host name > ")
    ip = socket.gethostbyname(host)
if userchoice == "2":
    ip = input("Enter IP address > ")
print("Scanning IP {}. Please wait.......".format(ip))
try:
    for port in range(1,65534):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print("Port {} is open.".format(port))
        sock.close()
except:
    print("[+]An error occupied.")
