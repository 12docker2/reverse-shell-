import os
import socket

def main():
    Device = socket.gethostname()
    Ip = socket.gethostbyname(Device)
    print(f"Aqui el nombre de el pc: {Device} y aqui la ip: {Ip}")

if __name__ == '__main__':
    main()
