# This Python file uses the following encoding: utf-8

from msp_Member.msp_CreateMember import createMember
from encryption.msp_createAsyKey import createAsymmetricKey
import sys



class mspManage:

    #def updateMember():
                              


    def getMemberElement(self, element):        
        return member[element]    #member['_id']



    def run(self):

        while True:
            print("")
            print("=====================")
            print("1. 멤버 추가")
            print("2. 멤버 보기")
            print("3. 멤버 삭제")
            print("4. 키 관리")
            print("5. 메뉴 다시보기")
            print("0. 종료")
            print("=====================\n")
            num = input(" 입력 > ")
            
            memberCreate = createMember()
            keyCreate = createAsymmetricKey()
            if (num == '1'):
                memberCreate.createMember()

            elif num == '2':
                while 1:
                    print("  1. 전체보기 :")
                    print("  2. 이름검색 :")
                    print("  0. 나가기 :")
                    mNum = input(" 입력 > ")
                    if mNum == '1':
                        memberCreate.viewMembers()
                    elif mNum == '2':
                        mName = input("검색할 이름 입력 : ")
                        memberCreate.viewMember('userName', mName)
                    elif mNum == '0':
                        break

            elif num == '3':
                mPhone = input("검색할 핸드폰번호 입력(exit:x) : ")
                if kName == 'x':
                    break
                else:
                    memberCreate.deleteMember('userPhone',mPhone)

            elif num == '4':
                kName = input("생성할 키 이름 입력(exit:x) : ")
                if kName == 'x':
                    break
                else:
                    keyCreate.run(kName)
            

            elif num == '5':
                print("=====================")
                print("1. 멤버 추가")
                print("2. 멤버 보기")
                print("3. 멤버 삭제")
                print("4. 키 생성")
                print("5. 메뉴 보기")
                print("0. 종료")
                print("=====================")
            elif num == '0':
                sys.exit()

            else:
                print("  ")
                print("   다시 입력하시오")
                print("  ")
        #createMember()
        #viewMembers()
        #viewMember()
        #getMemberElement(collection, '_id')
        #msp.setAttribute(ID="id2")

        #validCheckID("a1") #id중복체

    
if __name__ == "__main__":
    r = mspManage()
    while True:
        r.run()
    #t = createMember()
    #t.findDocument("userIPv4",ID="a6")
