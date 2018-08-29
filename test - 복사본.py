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
global ip 
import socketserver, os, pathlib, sys, socket
from os.path import exists

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.block import block
from ledger.transaction import transaction
from ledger.transaction_Producer import *
from ledger.transaction_Vehicle_wearing import *
from ledger.transaction_Vehicle_shipment import *
from ledger.transaction_Inventory_Management import *
from ledger.transaction_Auction import *
from ledger.transaction_Seller import *

from chaincode.transactionToJson import *
from chaincode.server_Json import *
from chaincode.blockToJson import blockToJson
from chaincode.randFileName import *
from chaincode.leader_rand import *
from chaincode.chainToJson import *

from msp.msp_Client.request_client import mspRequest, ipv4Request
from encryption.tr_sk_encrypt import *

#from uuid import getnode


# 1. run server
def socket_server():
    try :
        HOST = "202.31.146.57"
        PORT =  9009
        runServer(Host = HOST, Port  = PORT)
    except:
        print()
    return False

# 2. make tx
def makeTransaction(tmp):
    print("make transaction")

    tx = None
    
    if tmp == 'Producer':
        print('----------생산 트랜잭션----------')
        생산자이름 = input('생산자이름 : ')
        생산자전화번호 = input('생산자전화번호 : ')
        생산자주소 = input('생산자주소 : ')
        브랜드 = input('브랜드 : ')
        상품이름 = input('상품이름 : ')
        재배품종 = input('재배품종 : ')
        재배지주소 = input('재배지주소 : ')
        재배작형 = input('재배작형 : ')
        수확날짜 = input('수확날짜 : ')
        출하날짜 = input('출하날짜 : ')
        무게 = input('무게 : ')
        등급 = input('등급 : ')
        당도 = input('당도 : ')
        이력추적관리번호 = input('이력추적관리번호 : ')
        사업자등록번호 = input('사업자등록번호 : ')
        농약제품명 = input('농약제품명 : ')
        농약용도 = input('농약용도 : ')
        농약형태 = input('농약형태 : ')
        try :
           tx = transaction_Producer(생산자이름 = 생산자이름, 생산자전화번호 = 생산자전화번호, 생산자주소 = 생산자주소, 브랜드 = 브랜드, 상품이름 = 상품이름, 재배품종 = 재배품종, 재배지주소 = 재배지주소, 재배작형 = 재배작형, 수확날짜 = 수확날짜, 출하날짜 = 출하날짜, 무게 = 무게, 등급 = 등급, 당도 = 당도, 이력추적관리번호 = 이력추적관리번호, 사업자등록번호 = 사업자등록번호, 농약제품명 = 농약제품명, 농약용도 = 농약용도, 농약형태 = 농약형태)
           return tx

        except Exception as E:
           print(E)

    elif tmp == 'Distributor':
        print("1. 입고")
        print("2. 출고")
        num = input("select : ")
        if num == '1':
            print('----------입고 트랜잭션----------')
            단체이름 = input('단체이름 : ')
            사업자등록번호 = input('사업자등록번호 : ')
            담당자이름 = input('담당자이름 : ')
            담당자전화번호 = input('담당자전화번호 : ')
            입고날짜 = input('입고날짜 : ')
            입고단체이름 = input('입고단체이름 : ')
            입고단체주소 = input('입고단체주소 : ')
            상품이름 = input('상품이름 : ')
            수량 = input('수량 : ')
            무게 = input('무게 : ')
            온도 = input('온도 : ')
            입고차량번호 = input('입고차량번호 : ')
            입고차량운전자 = input('입고차량운전자 : ')
            입고차량운전자전화번호 = input('입고차량운전자전화번호 : ')
            try : tx = transaction_Vehicle_wearing(단체이름 = 단체이름, 사업자등록번호 = 사업자등록번호, 담당자이름 = 담당자이름, 담당자전화번호 = 담당자전화번호, 입고날짜 = 입고날짜, 입고단체이름 = 입고단체이름, 입고단체주소 = 입고단체주소, 상품이름 = 상품이름, 수량 = 수량, 무게 = 무게, 온도 = 온도, 입고차량번호 = 입고차량번호, 입고차량운전자 = 입고차량운전자, 입고차량운전자전화번호 = 입고차량운전자전화번호)
            except Exception as E : print(E)
            else : return tx

        elif num == '2':
            print('----------출고 트랜잭션----------')
            단체이름 = input('단체이름 : ')
            사업자등록번호 = input('사업자등록번호 : ')
            담당자이름 = input('담당자이름 : ')
            담당자전화번호 = input('담당자전화번호 : ')
            출고날짜 = input('출고날짜 : ')
            출고단체이름 = input('출고단체이름 : ')
            출고단체주소 = input('출고단체주소 : ')
            상품이름 = input('상품이름 : ')
            수량 = input('수량 : ')
            무게 = input('무게 : ')
            온도 = input('온도 : ')
            출고차량번호 = input('출고차량번호 : ')
            출고차량운전자 = input('출고차량운전자 : ')
            출고차량운전자전화번호 = input('출고차량운전자전화번호 : ')
            try : tx = transaction_Vehicle_shipment(단체이름 = 단체이름, 사업자등록번호 = 사업자등록번호, 담당자이름 = 담당자이름, 담당자전화번호 = 담당자전화번호, 출고날짜 = 출고날짜, 출고단체이름 = 출고단체이름, 출고단체주소 = 출고단체주소, 상품이름 = 상품이름, 수량 = 수량, 무게 = 무게, 온도 = 온도, 출고차량번호 = 출고차량번호, 출고차량운전자 = 출고차량운전자, 출고차량운전자전화번호 = 출고차량운전자전화번호)
            except Exception as E : print(E)
            else : return tx

    elif tmp == 'WManager':
        print('----------재고관리 트랜잭션----------')
        단체이름 = input('단체이름 : ')
        사업자등록번호 = input('사업자등록번호 : ')
        담당자이름 = input('담당자이름 : ')
        담당자전화번호 = input('담당자전화번호 : ')
        창고번호 = input('창고번호 : ')
        구역번호 = input('구역번호 : ')
        재고확인날짜 = input('재고확인날짜 : ')
        재고확인시간 = input('재고확인시간 : ')
        상품이름 = input('상품이름 : ')
        수량 = input('수량 : ')
        무게 = input('무게 : ')
        try :
           tx = transaction_Inventory_Management(단체이름 = 단체이름, 사업자등록번호 = 사업자등록번호, 담당자이름 = 담당자이름, 담당자전화번호 = 담당자전화번호, 창고번호 = 창고번호, 구역번호 = 구역번호, 재고확인날짜 = 재고확인날짜 ,재고확인시간 = 재고확인시간, 상품이름 = 상품이름, 수량 = 수량, 무게 = 무게)
           return tx

        except Exception as E:
           print(E)

    elif tmp == 'Auctioneer':
        print('----------경매 트랜잭션----------')
        상품이름 = input('상품이름 : ')
        상품등급 = input('상품등급 : ')
        단체이름 = input('단체이름 : ')
        사업자등록번호 = input('사업자등록번호 : ')
        담당자이름 = input('담당자이름 : ')
        담장자전화 = input('담장자전화 : ')
        경매날짜 = input('경매날짜 : ')
        낙찰금액 = input('낙찰금액 : ')
        try :
           tx = transaction_Auction(상품이름 = 상품이름, 상품등급 = 상품등급, 단체이름 = 단체이름, 사업자등록번호 = 사업자등록번호, 담당자이름 = 담당자이름, 담장자전화 = 담장자전화, 경매날짜 = 경매날짜, 낙찰금액 = 낙찰금액)
           return tx

        except Exception as E:
           print(E)

    elif tmp == 'Seller':
        print('----------판매 트랜잭션----------')
        단체이름 = input('단체이름 : ')
        사업자등록번호 = input('사업자등록번호 : ')
        담당자이름 = input('담당자이름 : ')
        담당자전화번호 = input('담당자전화번호 : ')
        이력추적관리번호 = input('이력추적 관리번호 : ')
        상품무게 = input('상품무게 : ')
        판매날짜 = input('판매날짜 : ')
        판매가격 = input('판매가격 : ')
        구매자이름 = input('구매자이름 : ')
        구매자전화번호 = input('구매자전화번호 : ')
        try :
           tx = transaction_Seller(단체이름 = 단체이름, 사업자등록번호 = 사업자등록번호, 담당자이름 = 담당자이름, 담당자전화번호 = 담당자전화번호, 이력추적관리번호 = 이력추적관리번호, 상품무게 = 상품무게, 판매날짜 = 판매날짜, 판매가격 = 판매가격, 구매자이름 = 구매자이름, 구매자전화번호 = 구매자전화번호)
           return tx

        except Exception as E:
           print(E)


    elif number == '0':
        print('종료')
        return 

    else : print("done!!")

    print(tx.toDict())
    return tx


# 3. take_atfter_tx
def take_after_tx(filename):
    ttj = transactionToJson(filename = filename)
    ttj.data = ttj.loadJson()
    Transaction = transaction()
    Transaction.fromDict(Dict = ttj.data)
    print(Transaction.toDict())
    return Transaction
    

# 7. make_block
def make_block(tx):
    Block = block(tx)
    print(Block.toDict())
    btj = blockToJson(filename = "block_" + Block.blockID+".json", data = Block)
    return Block

# 9. block dispersion
def block_dispersion(Host,Port,filename):
    path = os.path.dirname(__file__) + "\data_server\\"
    filename = path + filename

    with socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
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
                
# 10. chain append
def chain_append():
    path = os.path.dirname(__file__) + "\data_server\\"
    filename = str(input('체인에 연결시킬 블록 : '))
    btj = blockToJson(filename = filename)
    btj.data = btj.loadJson()
    Block = block()
    Block.fromDict(Dict = btj.data)
    chid = input('CHID : ')
    filename = "ch_" + chid + ".json"
    if not exists(path + filename):
        Chain = chain(CHID = chid, block = Block)
        Chain.append(Block)
        ctj = chainToJson(filename = filename, data = Chain)
        ctj.saveJson()
    else:
        ctj = chainToJson(filename = filename)
        ctj.data = ctj.loadJson()
        Chain = chain()
        Chain.fromDict(Dict = ctj.data)
        Chain.append(Block)
        ctj = chainToJson(filename = filename, data = Chain)
        ctj.saveJson()
    print(Chain.toDict())

# 11. 암호화
def encrypt(Block):
    block_encrypt = en()
    sk_key = block_encrypt.create_key()
    block_encrypt.tr_ec(sk_key, "block_" + Block.blockID + ".json")
    return False


if __name__ == "__main__":
    filename = ""
    result = 0
    tx = None
    Block = None
    en_data = None
    tmp = None
    while True:
        print("login")
        
        ID = input("ID : ")
        PW = input("PW : ")
    
        msp = mspRequest()
        tmp = msp.verificationRequest(ID, PW)
    
        print(tmp, type(tmp))
    
        if tmp == "Auctioneer" or tmp == "Distributor" or tmp == "Producer" or tmp == "Seller" or tmp == "WManager" :
            break

    while True:
        
        print("---------------- socket - blockchain test ----------------")
        print("1. run server")
        print("2. make tx")
        print("3. make block")
        print("4. block encryption")
        print("5. Block dispersion")
        print("0. 종료")
    
        num = int(input('select : '))
        if num == 1:
            print("1. run server")
            socket_server()
    
        elif num == 2:
            print("2. make tx")
            tx = makeTransaction(tmp)
        
        elif num == 3:
            print("3. make BLock")
            Block = make_block(tx)

        elif num == 4:
            en_data = encrypt(Block)
            
        elif num == 5:
            print("4. Block dispersion")
            filename = "block_" + Block.blockID + "_skec.pem"
            #block_dispersion(Host = "202.31.146.57", Port= 9011, filename=filename)
            #ip = ["202.31.146.57"]
            ip = ipv4Request()
            num, ip = ip.ipv4Request("02")
            for i in ip:
                try:
                    block_dispersion(Host = i,Port= 9009, filename=filename)
                except Exception as e:
                    print(e)
            filename="ch_1.json"
            ctj = chainToJson(filename=filename)
            if not exists(path + filename):
                Chain = chain(CHID = chid, block = Block)
                Chain.append(Block)
                ctj = chainToJson(filename = filename, data = Chain)
                ctj.saveJson()
            else:
                ctj = chainToJson(filename = filename)
                ctj.data = ctj.loadJson()
                Chain = chain()
                Chain.fromDict(Dict = ctj.data)
                Chain.append(Block)
                ctj = chainToJson(filename = filename, data = Chain)
                ctj.saveJson()
            print(Chain.toDict())
            
            
        elif num==0:
            break

        print()
        print()
        print()
        print()
