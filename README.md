# DustScan
Dust Scan is a port scanning tool. 

## There are two options in this tool
You can scan using sever IP or host name.

## Installation on Termux
```
pkg install git
pkg install python
git clone 
pip3 install pyfiglet
cd Dustscan
python3 dustscan.py
```

## Installation on Ubuntu Linux
```
sudo apt install python
sudo apt install git
sudo apt install python3 -pip
sudo pip3 install pyfiglet
git clone 
cd DustScan
python3 dustscan.py
```

## Usage
To run this tool, type the following commands
```
python3 dustscan.py
```
This tool has two options

There are..
1. Scanning using host name
2. Scanning using IP address

If you don't know ip address of host, you should choice option 1.

```
Created by Zin Yaw.
[-1-] Scan using host name
[-2-] Scan using IP address
Select an option > 1
```
I tested with my localhost
```
Enter host name > localhost
Scanning IP 127.0.0.1. Please wait....
Port 631 is open.
Port 33144 is open.
Port 50740 is open.
```
