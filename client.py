'''
    win10 client-socket
'''

import socket
import os
import sys
import struct

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client():

    def SetPortIp(self, port, ip):
        self.port = port           # 设置端口
        self.ip = ip  # 设置需要连接的服务器IP


        s.settimeout(10)
        try:
            s.connect((port, ip))
            print('Connect success !')
        except Exception:
            print('Connect failed !')

    def SendData(self, path):
        self.path = path

        fhead = struct.pack(b'128sq', bytes(os.path.basename(path), encoding='utf-8'),
                            os.stat(path).st_size)  # 将xxx.jpg以128sq的格式打包
        s.send(fhead)

        fp = open(path, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read(1024)  # 读入图片数据
            if not data:
                print('{0} send over...'.format(path))
                break
            s.send(data)  # 以二进制格式发送图片数据

        server_reply = s.recv(1024).decode()
        print(server_reply)

        s.close()
        sys.exit()  # 循环发送


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
object =Client()
object.SetPortIp(2000, '192.168.203.20')
object.SendData('D:/test-picture/oasis_1080.jpg')


