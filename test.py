# This Python file uses the following encoding: utf-8

# 기영 202.31.146.57
# 기도 202.31.147.203
# 신재 202.31.146.48
# 상훈 202.31.146.58
# PORT 9009

# 가정
# 1. 기존 장부는 있다. (Chain은 이미 있다.)
# 2. 기존 장부에 트랜잭션을 발생시켜 블록화를 하고 채인에 추가함
# 3. 채인에 추가할 때 FlagDB까지 갱신을 시켜야 한다.
# 4. 트랜잭션은 이미 만들어진 data_server\tx_52qp2i55919387.json 을 기본으로 한다.
# 5. 기존 장부는 data_server\ch_8srkziel366214.json 을 기본으로 한다.
# 6. 마지막 10. chain append는 모든 노드가 최대한 비슷한 시간에 동시에 수행되어야 한다.
# 7. 결론적으로 tx_52qp2i55919387.json 의 내용이 합의를 통해서 ch_8srkziel366214.json 에 추가되어야 한다.

import socketserver, os, pathlib, sys, socket
from os.path import exists




from chaincode.server_Json import *




# 1. run server
def socket_server():
    try :
        HOST = "202.31.146.57"
        PORT =  9009
        runServer(Host = HOST, Port  = PORT)
    except:
        print()
    return False

# 2. send tx

def send_tx(Host, Port, filename):
    path = os.path.dirname(__file__) + "\data_client\\"
    filename = path + filename

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((Host,Port))

        if not exists(filename): # 파일이 해당 디렉터리에 존재하지 않으면
            print("not exists(filename)")
            return # handle()함수를 빠져 나온다.

        with open(filename, 'rb') as f:
            try:
                data = f.read()
                sock.sendall(data)
                print(data)
            except Exception as e:
                print(e)



if __name__ == "__main__":
    print("---------------- socket - blockchain test ----------------")
    print("1. run server")
    print("2. send tx")
    print("3. take after tx")
    print("4. agree")
    print("5. send leader")
    print("6. leader Synthesis")
    print("7. make block")
    print("8. renewal FlagDB")
    print("9. Block dispersion")
    print("10. chain append")
    print("")

    num = int(input('select : '))

    if num == 1:
        print("1. run server")
        socket_server()

    elif num == 2:
        print("2. send tx")
        send_tx("202.31.146.57", 9009, "tx_52qp2i55919387.json")

    elif num == 3:
        print("3. take after tx")

    elif num == 4:
        print("4. agree")

    elif num == 5:
        print("5. send leader")

    elif num == 6:
        print("6. leader Synthesis")

    elif num == 7:
        print("7. make block")

    elif num == 8:
        print("8. renewal FlagDB")

    elif num == 9:
        print("9. Block dispersion")

    elif num == 10:
        print("10. chain append")