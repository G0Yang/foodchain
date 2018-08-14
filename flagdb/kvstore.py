import couchdb

class kvstore:
    def __init__(self, *args, **kwargs):
        self.server = ""
        self.db = ""
        try :
            user = kwargs['user'] # admin
            password = kwargs['password'] # food1234
            self.server = couchdb.Server("http://%s:%s@"+ kwargs['IP'] +":5984/" % (user, password))
        except:
            print("init false!!")
        return

    def login(self, *args, **kwargs):
        try :
            user = kwargs['user'] # admin
            password = kwargs['password'] # food1234
            self.server = couchdb.Server("http://%s:%s@" % (user, password) + kwargs['IP'] +":5984/")
        except:
            print("login false!!")
            return False
        else:
            print("login succeces!!")
            return True
        return False

    def makeDB(self, DBname):
        if DBname in self.server:
            print(DBname + " is exist!!")
            return False
        else:
            db = self.server.create(DBname)
            return db
        return False
        
    def connectDB(self, DBname):
        if DBname in self.server: # DBname is foodchain
            self.db = self.server[DBname]
            return self.db
        else:
            print("DBname is not exist in databasa")
            return False
        return False

    def insertDB(self, data): # data is Dictionary
        try :
            self.db.save(data)
        except:
            print("DB is not initialized")
        else:
            return True
        return False

    def showDatabases(self):
        try:
            for i in self.server:
                print(i)
        except:
            print("server is not initialized")
        return False

    def showData(self):
        try :
            for i in self.db:
                print(self.db.get(i))
        except:
            return False
        else:
            return True
        return False


'''
k = kvstore()
k.login(user = 'admin', password = 'food1234', IP = '202.31.146.57')
#k.showDatabases()
k.db = k.connectDB(DBname="foodchain")
print(k.db)
print("show :", k.showData())
print("insert : ", k.insertDB(data = {'name' : 'kim'}))
print("show :", k.showData())
'''


''' # 테스트 예제
import couchdb


# 데이터베이스 로그인
user = "admin"
password = "food1234"
couchserver = couchdb.Server("http://%s:%s@202.31.146.57:5984/" % (user, password))


# 데이터베이스 전체 탐색 쿼리
for dbname in couchserver:
    print(dbname)


# 특정 데이터 베이스 탐색 OR 생성
dbname = "foodchain"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)


# 값 삽입 쿼리
#doc_id, doc_rev = db.save({'hash': '123JKH123KJ12H3KJH12KKLAJHSD'})
#print(doc_id, doc_rev)


# 값 탐색 쿼리
for i in db:
    try: # 키에 hash 가 없을 수 있기 때문에 꼭 예외처리 해줘야 함
        print(db.get(i)['hash'])
        print(type(db.get(i)['hash']))
    except:
        print("id not in hash")


# 데이터베이스 삭제 쿼리
#del couchserver [dbname]


# 여러 값 삽입 쿼리
#docs = [{'key': 'value1'}, {'key': 'value2'}]
#for (success, doc_id, revision_or_exception) in db.update(docs):
#    print(success, doc_id, revision_or_exception)

'''