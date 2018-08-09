import time, sys, os, json, pathlib, socket, threading
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from chaincode.chainToJson import *
from worldstate.kvstore import kvstore

# 기존 체인안에 있는 블록들이 헤시값으로 잘 연결되어 있는지 확인함.
# 각 체인의 마지막 블록과 W에 저장되어 있는 블록값이 일치하는 지 확인.
# 같지 않다면 기존 블록을 처리하는 알고리즘을 구현.

class synchronize:
    def __init__(self, *args, **kwargs):
        return

    def isPriviousHash(self, ctj):
        print(type(ctj.data))
        print(ctj.data.toDict())



        # 블록이 이어디는 것을 Hash를 이용하여 탐색
        # 재귀함수 형식으로 재작하여 최종 마지막 블록의 Hash값을 반환하게 제작

    #def callWorldState(self, block):
        #중간에 잘린 블록을 얻기위해서 W에 최신 정보와 잘려진 마지막 블록을 대조하여 잘린 블록인지, 이어진 블록인지 판별


    def checkLastBlock(self):
        return




if __name__ == "__main__":
    cj1 = chainToJson(filename = "8srkziel366214.json")
    print(cj1)

    sync = synchronize()
    sync.isPriviousHash(cj1)
    '''
    for i in range(1, len(ctj.data)):
        if ctj.data[str(i)]['BH_currentBlockHash'] == ctj.data[str(i+1)]['BH_previousBlockHash']:
            print(i, "matched!!")
            continue
        else:
            print("not match!!")
    '''