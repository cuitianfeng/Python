import socket
import struct
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('server start...')
while True: #链接循环
    conn,client_addr=phone.accept()
    print(conn,client_addr)

    while True: #通讯循环
        try:
            cmd=conn.recv(1024)
            if not cmd:break

            #执行命令，拿到结果
            res=subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

            stdout=res.stdout.read()
            stderr=res.stderr.read()

            #制作报头
            header=struct.pack('i',len(stdout)+len(stderr))

            #先发报头(固定长度)
            conn.send(header)
            #再发真实的数据
            conn.send(stdout)
            conn.send(stderr)

        except Exception: #针对windwos
            break
    conn.close()

phone.close()