from ledger.transaction import transaction
from ledger.blockheader import blockheader
from ledger.block import block
from ledger.chain import chain

from chaincode.transactionToJson import transactionToJson
from chaincode.blockToJson import blockToJson
from chaincode.chainToJson import chainToJson
from chaincode.client_Json import *
from chaincode.server_Json import *
from chaincode.randFileName import *

from Stakeholder.Stakeholder import *
from flagdb.kvstore import *

from msp.msp import msp
from synchronize.synchronize import synchronize

from hash256.hash256 import hash256


from socket import *

import tempfile, time, os, json, pathlib

# 1 트랜잭션 만들기
def makeTransaction():
    print("make transaction")
    생산자 = input('생산자 이름 : ')
    전화번호 = input('전화번호 : ')

    타입 = input('배송 상태 : ')

    이름 = input('이름 : ')
    산지 = input('산지 : ')
    등급 = input('등급 : ')
    무게 = input('무게 : ')

    try : tx = transaction(생산자 = 생산자, 전화번호 = 전화번호, 이름 = 이름, 산지 = 산지, 등급 = 등급, 무게 = 무게, 타입 = 타입)
    except : print("error!")
    else : print("done!!")

    print(tx.toDict())
    return tx

# 2 트랜잭션 저장(o) + 보내기(x)
def sendTransaction(tx):
    if type(tx) != type(transaction()):
        return False
    print("send transaction")
    ttj = transactionToJson(filename = "tx_" + randFileName(), data = tx)
    return ttj

# 3 블록 만들기
def makeBlock(tx):
    if type(tx) != type(transaction()):
        return False
    print("make block")
    Block = block(tx)

    print(Block.toDict())
    return Block

# 4 블록 저장(o) + 보내기(x)
def sendBlock(Block):
    if type(Block) != type(block()):
        return False
    print("send block")
    btj = blockToJson(filename = "block_" + randFileName(), data = Block)
    return btj

# 5 체인 만들기
def makeChain(Block):
    if type(Block) != type(block()):
        return False
    print("make chain")
    Chain = chain(CHID = input('CHID : '), block = Block)

    print(Chain.toDict())
    return Chain

# 6 체인 저장(o) + 보내기(x)
def sendChain(Chain):
    if type(Chain) != type(chain()):
        return False
    print("send chain")
    ctj = chainToJson(filename = "ch_" + randFileName(), data = Block)
    ctj.appendBlock(Chain.toDict())
    ctj.saveJson()
    return ctj

# 7 파일 리스트 보여주기
def showFileList():
    path = os.path.dirname(__file__) + "\\" + str(input('dir : ')) + "\\"
    file_list = os.listdir(path)
    file_list.sort()

    print()
    print("--------- \data_server ---------")

    for i in file_list:
        print(i)

    print()

# 9 기존 체인에 블록 추가
def appendBlockInChain(Block, Chain, ctj):
    if type(Chain) != type(chain()) or type(Block) != type(block()):
        return False
    print("append Block In Chain")
    try: ctj.appendBlock(Block.toDict())
    except: print("append error!!!")

    try: ctj.saveJson()
    except: print("save error!!!")
    return True

# 12 worldstate 다루기 - 아파치 couchDB (보류)
def worldstate(Chain):
    W = kvstore()
    while True:
        print("1. login")
        print("2. show databasas")
        print("3. show data in database")
        print("4. insert data in database")
        print("5. make database")
        print("6. select database")
        print("0. exit")

        num = int(input('num : '))

        if num == 1:
            W.login(user = 'admin', password = 'food1234', IP = '202.31.147.216')

        elif num == 2:
            W.showDatabases()

        elif num == 3:
            W.showData()

        elif num == 4:
            data = ""
            try: data = Chain.chains[-1].toDict()
            except: print("error")

            W.insertDB(data = data)

        elif num == 5:
            W.makeDB(DBname = input('DBname : '))

        elif num == 6:
            W.connectDB(DBname = input('DBname : '))

        elif num == 0:
            break

    return False

# 14 socket-client 다루기
def socket_client():
    HOST = str(input('HOST : '))
    PORT = int(input('PORT : '))
    filename = str(input('다운로드 받은 파일이름을 입력하세요:'))
    getFileFromServer(Host = HOST, Port  = PORT, filename = filename)
    
    flag = input('T = 트랜잭션, B = 블록, C = 체인 : ')
    
    if flag == "c" or flag == "C":
        try : 
            ctj = chainToJson(filename = filename)
            ctj.data = ctj.loadJson()
            Chain = chain()
            Chain.fromDict(Dict = ctj.data)
            print(Chain.toDict())
        except:
            print("file is not exist")

    elif flag == "b" or flag == "B":
        try : 
            btj = blockToJson(filename = filename)
            btj.data = btj.loadJson()
            Block = block()
            Block.fromDict(Dict = btj.data)
            print(Block.toDict())
        except:
            print("file is not exist")

    elif flag == "t" or flag == "T":
        try : 
            ttj = transactionToJson(filename = filename)
            ttj.data = ttj.loadJson()
            Transaction = transaction()
            Transaction.fromDict(Dict = ttj.data)
            print(Transaction.toDict())
        except:
            print("file is not exist")

    return False

# 15 socket-server 다루기
def socket_server():
    try :
        HOST = str(input('HOST : '))
        PORT =  int(input('PORT : '))
        runServer(Host = HOST, Port  = PORT)
    except:
        print()
    return False

# 20 json 파일을 브로드케스팅으로 보내기(x)
def sendJsonBroadcasting():
    cs = socket(AF_INET, SOCK_DGRAM)
    cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    path = os.path.dirname(__file__) + "\data_server\\"

    file = pathlib.Path(path + 'tx.json')
    file_text = file.read_text(encoding='utf-8')

    #cs.sendto(file_text.encode(), ('255.255.255.255', 9009))

    return False

# 21 json 파일을 브로드케스팅으로 받기(x)
def takeJsonBroadcasting():
    s1 = server_Json()
    s1.runServer()
    return False

if __name__ == "__main__":
    tx = ""
    Block = ""
    Chain = ""

    ttj = ""
    btj = ""
    ctj = ""

    while True:
        print("")
        print("-------------- 종합 예제 --------------")
        print("1. make transaction")
        print("2. send transaction")

        print("3. make block")
        print("4. send block")

        print("5. make chain")
        print("6. send chain")

        print("7. show filesystem (dir input)")

        print("8. chain hash check")

        print("9. append block in chain")

        print("10. reset transaction, block, chain, ttj, btj, ctj")

        print("11. get ledger")
        print("12. worldstate")
        print("13. show transaction, block, chain")

        print("14. client-server")
        print("15. socket-server")

        
        print("20. send json to Broacast-socket")
        print("21. take json from Broacast-socket")

        print("0. exit")

        try : num = int(input('input : '))
        except : num = None

        if num == 1:
            tx = makeTransaction()

        elif num == 2:
            ttj = sendTransaction(tx)

        elif num == 3:
            Block = makeBlock(tx)

        elif num == 4:
            btj = sendBlock(Block)

        elif num == 5:
            Chain = makeChain(Block)

        elif num == 6:
            ctj = sendChain(Chain)
            print(ctj.loadJson())

        elif num ==7:
            showFileList()

        elif num == 8:
            # 8 채인 안에 블록들 해시 연결 확인
            sync = synchronize()
            try : sync.isPriviousHash(ctj)
            except : print("sync, ctj is not define!!")

        elif num == 9:
            appendBlockInChain(Block, Chain, ctj)

        elif num == 10:
            tx = ""
            Block = ""
            Chain = ""
            ttj = ""
            btj = ""
            ctj = ""

        elif num == 11:
            # 11 기존 원장 불러오기
            try :
                ctj = chainToJson(filename = str("ch_" + input('filename : ')))
                ctj.data = ctj.loadJson()
            except : print("file is not exist")
            try : 
                Chain = chain()
                Chain.fromDict(Dict = ctj.data)
            except:
                print("set fromFict() error")

        elif num == 12:
            worldstate(Chain)

        elif num == 13:
            try: print(tx.toDict())
            except:print("tx error")

            try: print(ttj.data)
            except:print("ttj error")

            try: print(Block.toDict())
            except:print("Block error")

            try: print(btj.data)
            except:print("btj error")

            try: print(Chain.toDict())
            except:print("Chain error")

            try: print(ctj.data)
            except:print("ctj error")
            
        elif num == 14:
            socket_client()

        elif num == 15:
            socket_server()

        elif num == 20:
            sendJsonBroadcasting()

        elif num == 21:
            takeJsonBroadcasting()

        elif num == 0:
            break

        else:
            print("try again...")