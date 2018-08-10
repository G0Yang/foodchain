# 원장이 해시값으로 잘 연결되어 있는지 확인
# -> 아니라면 잘린 부분 이후를 삭제
# -> 나중에 타 노드에게 요청할 수 있음.

# 타 노드의 원장과 비교하여 다른 점이 있는지 확인
# -> 최소 3개 이상
# -> 다르다면 

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flagdb.kvstore import kvstore

class synchronize:
    def __init__(self, *args, **kwargs):
        self.flag = True
        self.Chain = None
        return

    def get_FlagDB(self, CHID):

        return False

    def isCurrectHashInChain(self,Chain):
        if type(Chain) != "<class 'ledger.chain.chain'>":
            return False
        self.Chain = Chain
        for i in renge(0,len(Chain.chains)-1):
            if Chain.Chians[i].BH.currentBlockHash is not Chain.Chians[i+1].BH.previousBlockHash:
                self.flag = False
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