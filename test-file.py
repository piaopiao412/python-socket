#!/user/bin/python
# -*- coding: utf-8 -*-
'''
python3 socket 文件传输--服务端（Windows版本）：
v1.5:
1、接收客户端传递过来的文件

'''
import socket, os,logging
from datetime import datetime

socket = socket.socket()
socket.bind(("192.168.203.83", 6000))
socket.listen(20)
SIZE = 1024*1024*2000
savepath = "/home/hq/图片/11"

def Service():
    while True:
        conn, addr = socket.accept()
        print('Accept new connection from %s:%s...' % addr)
        conn.sendall(bytes("Welcome from server!", encoding="ISO-8859-1"))
        print(conn)
        try:
            while True:
                fpath = str(conn.recv(8192), encoding="ISO-8859-1")
                f_dir = os.path.split(fpath)[0]
                fname = os.path.split(fpath)[1]
                fnameSave = os.path.join(savepath,fname)
                if not os.path.isdir(savepath):
                    os.makedirs(savepath)
                ff = open(fnameSave, 'wb') # 按照配置的路径进行存储
                starttime = datetime.now()
                print("start...")
                recvdata = conn.recv(SIZE)
                if not recvdata:
                    print("reach the end of file")
                    break
                else:
                    ff.write(recvdata)
                ff.close()
                endtime = datetime.now()
                print("end...花费时间(s)",(endtime-starttime).seconds)
        except Exception as e:
            logging.error("服务器异常...")
            logging.exception(e)
        finally:
            conn.close()

    print("receive finished")
    print("connection from %s:%s closed." % addr)

if __name__ == '__main__':
    Service()


