from _thread import *
import socket
import json

HOST = "127.0.0.1"
PORT = 6000
FILE_PATH = 'C:/temp/received/data'

def received_thread(client_socket, addr):
    try:
        # 파일 크기 수신
        # size = client_socket.recv(1024)
        # size = int(size.decode())
        # print(f"수신할 파일 크기: {size}")
        # json 문자열을 수신
        finfo = client_socket.recv(1024).decode()
        finfo = json.loads(finfo)
        print(f'파일명: {finfo.get("file_name")}, 파일크기: {finfo.get("file_size")}')
        size = finfo.get("file_size")
        fpath = "C:/temp/received/" + finfo.get("file_name")

        # 준비 상태 전송
        client_socket.send("ready".encode())

        # 파일 수신
        total_size = 0
        with open(fpath, "wb") as f:
            while True:
                data = client_socket.recv(512)
                f.write(data)
                total_size += len(data)
                if total_size >= size: break
            
            print(f"수신 완료: {total_size} bytes")
    
    except Exception as e:
        print(e)
    finally:
        client_socket.close()

with socket.socket() as s:
    try:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            client_socket, addr = s.accept()    # 접속대기
            # 스레드 기동
            start_new_thread(received_thread, (client_socket, addr))

    except Exception as e:
        print(e)