import socket
import os



def postData():
    # 实例化
    sk = socket.socket()
    # 定义连接的ip和port
    ip_port = ('192.168.203.83', 6000)
    # 服务器连接
    sk.connect(ip_port)
    # 文件上传，获取传送文件目录
    filenames = os.listdir(r"D:\test-picture")
    print(filenames)
    newfilename = "/".join(filenames)
    print(newfilename)
    print(type(newfilename))
    #将目录上传
    sk.send(newfilename.encode())
    for name in filenames:
        print(type(name))
        print(type(filenames))
    #打开文件
        with open('D:\\test-picture\\'+name,'rb') as f:
            #按每一段分割文件上传
            for i in f:
                # print(type(f))
                sk.send(i)
                #等待接收完成标志
                data=sk.recv(1024)
                #判断是否真正接收完成
                if data != b'success':
                    break
        #给服务端发送结束信号
        sk.send('quit'.encode())
    sk.close()
if __name__ == "__main__":
      postData()

