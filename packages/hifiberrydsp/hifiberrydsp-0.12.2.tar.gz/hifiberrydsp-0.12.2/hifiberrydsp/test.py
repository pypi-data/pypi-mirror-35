'''
Created on 7 Aug 2018

@author: matuschd
'''

import socket


def main():
    packet = bytearray([9, 0, 0, 0, 0, 0, 18, 0, 0,
                        0, 0, 4, 2, 119, 0, 0, 0, 0])
    IP = '192.168.4.156'
    PORT = 8086
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(packet)
    data = s.recv(BUFFER_SIZE)
    print(data)
    s.close()


if __name__ == '__main__':
    main()
