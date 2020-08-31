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
print("<1> Scan All port")
print("<2> Scan System port")
print("<3> Scan registred port")
print("<4> Scan Dynamic port")
choose = input("Select an option > ")
if choose == "2":
    start = 0
    end = 1023
elif choose == "3":
    start = 1024
    end = 49151
elif choose == "4":
    start = 49151
    end = 65535
elif choose == "1":
    start = 0
    end = 65535
try:
    i = 0
    for port in range(start,end):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print("Port {} is open.".format(port))
            i = 1
        sock.close()
    if i == 0:
       print("<+> No port is open.") 
except:
    print("[+]An error occupied.")
