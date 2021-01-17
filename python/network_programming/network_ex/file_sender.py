import os
import socket

HOST = "127.0.0.1"
PORT = 6000
FILE_PATH = 'C:/temp/CNN_0.ckpt.meta'

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            yield data

def file_info(fpath):
    # file_name = fpath.split('/')[-1]

    # os.path.split(fpath) --> (directory path, file name)
    file_name = os.path.split(fpath)[1]
    file_size = os.path.getsize(fpath)
    return {
        "file_name":file_name,
        "file_size":file_size
    }

import json
with socket.socket() as s:
    try:
        s.connect((HOST, PORT))

        finfo = file_info(FILE_PATH)
        # 파일 크기 전송
        print("전송 파일명", finfo["file_name"])
        print("전송 파일 크기", finfo["file_size"])
        msg = json.dumps(finfo)
        s.sendall(msg.encode())

        # 준비 상태 수신
        isready = s.recv(1024).decode()
        if isready == "ready":
            # 파일 전송
            for data in file_read(FILE_PATH):
                s.sendall(data)
            print("전송완료")

    except Exception as e:
        print(e)