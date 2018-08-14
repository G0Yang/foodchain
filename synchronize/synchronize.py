# 원장이 해시값으로 잘 연결되어 있는지 확인
# -> 아니라면 잘린 부분 이후를 삭제
# -> 나중에 타 노드에게 요청할 수 있음.

# 타 노드의 원장과 비교하여 다른 점이 있는지 확인 <- gRPC 사용
# -> 최소 3개 이상
# -> 다르다면 


# 올바른 원장이지만 중간에 블록이 없는 경우 ??? <- 없음.
# 풀노드를 지향한다면 새로운 접속마다 새로운 장부를 전부 다운로드 받는 형태
# 기존 장부가 해시로 잘 연결되어 있는지 탐색
# 잘 연결 되어 있다면 외부 노드들에게 부족한 정보를 요청함.
# 연결이 되어있지 않다면 조작된 블록으로 간주 <- 제거



import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flagdb.kvstore import kvstore

class synchronize:
    def __init__(self, *args, **kwargs):
        self.flag = []
        self.Chain = None
        return

    def cutChain(self):
        if len(self.flag) == 0:
            return False
        else:
            try:
                print("World State의 정보가 체인 안에 있는지 탐색")
                print("있다면 그 이후를 제거")
                LastBlockInFlagDB = getFlagDBFromChain(Chain.CHID)

                print("없다면 체인을 모두 제거하고 타 노드 중 올바른 체인을 가져온다.")
            except:
                print("Cut chain Fasle")
            else:
                return True
            return False
        return False

    def isCurrectHashInChain(self,Chain):
        if type(Chain) != "<class 'ledger.chain.chain'>":
            return False
        self.Chain = Chain
        for i in renge(0,len(Chain.chains)-1):
            if Chain.Chians[i].BH.currentBlockHash is not Chain.Chians[i+1].BH.previousBlockHash:
                self.flag.append(i+1)
        return self.flag

    def compareToFlagDB(self):
        if self.Chain is None:
            return False
        try :
            local_LastBlock = Chain.chains[-1]
            FalgDB_lastBlock = get_FlagDB(CHID = self.Chain.CHID)

            # 비교 연산...


        except:
            return False
        else:
            return True
        return False