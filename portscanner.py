import socket

from colorama import *

yellow = Fore.YELLOW

def check_open_port(host,port):
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    

    try:
        connection.connect((host,port))
        print(f"[+]{yellow} {port} Port Is Open ")

    except:
        pass

host = input("Enter The Ip Address To Scan ")

for port in range(0,1021):
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    check_open_port(host,port)








