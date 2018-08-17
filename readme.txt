2018.07.25 패치노트
1. chaincode/chainToJson , ledger/block , ledger/transaction , ledger/blockheader , ledger/chain 작업.
2. chain, block, transaction, blockheader에 toDict 함수 추가.
-> 나중에 Json 파일로 변환하기 위한 함수
3. 데이터 통신은 Json 파일을 중심으로 송수신함.
4. 제안서 생성 -> transactionToJson 사용
5. 블록 생성 -> blockToJson 사용
6. 기존 원장 추가 -> chainToJson 사용

2018.07.26 패치노트
1. 모든 소스에 예외처리 삽입.
2. 1개의 원장은 1개의 파일로 저장.
-> 파일 이름을 랜덤으로 생성하는 tempfile 모듈 사용.
-> 파일들을 관리하는 무언가의 프로그램 필요??????
3. 소켓 기반 json파일을 주고 받음. data_server 에서 data_client로 이동 확인
4. import 중복 최소화 root 폴더에 Foodchain.py 으로 테스트 진행

2018.07.27 패치노트
1. 분산원장 endorser 소스 추가 <- 박신재 작업
2. transaction에 검증, 서명 등 변수 추가 <- 박신재 작업
3. Foodchain.py 폴더 임시 기능 분리 구현 완료
4. 각 파일 모듈화, 예외처리 완료

2018.07.28 패치노트
1. leader 폴더 안에 kvstore.py 추가
-> 아파치 제공 couchDB 기반의 key-value store를 202.31.146.57에 설치하고 테스트확인 완료
-> 기본적인 쿼리를 파이썬 함수로써 예외처리를 포함하여 제작.
-> 입력되는 정보의 종류를 선별해야 함.
-> 추후에 W로써의 노드는 윈도우로 설치하여 couchDB를 설치하여 작업할 예정.
-> mac, centOS 설치 시 오류가 많음. (윈도우 10 최신 빌드 버전 권장 64bit)
-> 테스트 couchDB 주소 = 202.31.146.57:5984/_utils/index.html

2018.08.01 패치노트
1. couchDB와 공인IP와 바인딩을 했지만 외부에서 접근이 안되는 상황 해결.
-> 윈도우 제어판 -> 시스템 및 보안 -> Windows Defender 방화벽 -> 고급 설정 
-> 인바운드 규칙 생성 -> 포트 5984(default) -> 접근 허용 (TCP, UDP 두가지 설정)
2. 외부에서 couchDB로 값 insert 테스트 진행 중

2018.08.05 패치노트
1. randFileName.py 생성.
-> json파일을 생성하면서 파일 이름이 겹치지 않게 하기 위해서 임의로 지정.
-> 임의 랜덤 문자열과 생성 시간을 조합하여 파일이름을 결정함.
-> chainToJson.py에 테스트 결과 정상적으로 생성되는 것을 확인함.

2018.08.06 패치노트
1. Worldstate에 올라가는 데이터 형식 정의
-> {
	CHID,					# 파일이름과 CHID를 같게 하여 DB안에서 CHID도 중복이 안일어나게 끔 구성.
	Chain_hash,				# 머클트리 해시를 구하는 방식을 채택하여 해시값 계산.
	lastblock = Chains[-1]	# 해당 체인의 마지막 1개 블록을 전부 입력 <- 값을 비교할 때에는 전부 비교 OR 일부 비교
							# 블록의 toDict() 함수를 사용하여 딕셔너리 형태로 값을 저장
}
2. 블록 속성 중 "blocksize": 136 으로 값이 고정되는 현상 발견. -> 수정 필요
3. 블록이 체인안에 들어갈 때, "blockNumber": 0 으로 값이 고정되는 현상 발견. -> 수정 필요
4. 블록 안에 트랜잭션이 딕셔너리 안에서 "3" 의 값으로 들어가는 현상 발견 -> tx001, tx002 등 counting 작업 필요
5. Worldstate에 couchDB를 사용하는 이유 -> https://blog.panoply.io/couchdb-vs-mongodb  ,  http://ryufree.tistory.com/215?category=252658
6. 체인이 저장되는 json 파일에 정확하게 체인의 속성값들이 들어가지 않음. <- 수정 필요
7. 프로그램 전반적으로 사용되는 각 클래스의 toDict()의 참조 값들을 정의할 필요가 있음.

2018.08.08 패치노트
1. ledger/transaction.py , ledger/block.py , ledger/chain.py , chaincode/transactionToJson.py , chaincode/blockToJson.py , chaincode/chainToJson.py 수정
-> 각 소스에서 프로그램 상에는 변수로서 존재하고 파일을 저장하고 toDict()함수로 표기할 때에만 딕셔너리 형태로 변환하도록 변형
-> 소스에서 각 항목을 다룰 때 변수로써 혹은 딕셔너리로써 일관성없이 처리되고 있는 부분 수정
-> 특별히 chainToJson.py 에서 json 파일을 딕셔너리로, 딕셔너리를 chain 형 클래스 변수로 변환하는 과정 중 시간 소비 발생.
-> 각 클래스별로 파일로 저장되는 부분까지는 수정 완료.
2. 2018.08.06 패치노트 2,3,4,6,7 번 항목 패치 완료.
-> 2번 항목 : toDict() 함수의 문자열 총 길이로 파일 크기 계산
-> 3번 항목 : blockNumber는 체인에 추가될 경우 의미가 있기 때문에 chain.py 중 append() 함수에서 참조됨.
-> 4번 항목 : 각 클래스별로 자기 자신의 번호를 추가하여 해당 번호를 참조하여 이름을 선정함. <- 상위 개념으로 갈 경우 그냥 리스트 형식으로 넘어감.
-> 6,7번 항목 : 1번 참조
3. 파일 이름을 랜덤으로 생성하여 파일간 중복이 없도록 작업
-> 각 파일이름을 randFileName() 함수를 사용하여 클래스별로 ch_, tx_, block_ 접두어를 사용하여 파일을 구분함.

2018.08.09 패치노트
1. github private 계정 연동 완료
-> 로컬 공유 배포 중지
2. transaction, block, blockheader, chain에 fromDict() 함수 추가
-> 파일 안의 Dict를 각 클래스 변수로 변환하는 작업 완료.
3. 각 파일 조정 및 용어 재정의
4. 이 프로그램에서의 에러를 정의할 필요가 있음.
5. centOS7에 mongoDB v3.0 설치 완료 <- 박신재 작업
-> 참고 링크 : https://blog.naver.com/pray26/221198835501 (신재 블로그)

2018.08.13 패치노트
1. 종합예제 14번, 15번 추가 socket 기반 json 파일 주고 받기 완료
-> 파일을 받은 후 처리를 해야 함.
-> 14번 client, 15번 server 역활 배정

2018.08.16 패치노트
1. 9월 4일 발표를 위한 test.py 파일 생성
-> 기존 Foodchain.py에서는 server_Json.py 를 사용하고
-> test.py에서는 server_Json(1).py 를 사용함.
-> 파일명은 능동적으로 변할 수 있음.
2. 파일을 클라이언트가 서버로 전송하기 위해 test.py에 서버로 Json파일을 데이터화 해서 보내는 작업까지 완료.

2018.08.17 패치노트
1. 실제 서버안의 노드에 소스를 올려서 테스트 진행
-> 인코딩 문제 발생 <- # This Python file uses the following encoding: utf-8  구문 삽입하여 해결
-> 인코딩 https://www.python.org/dev/peps/pep-0263/ 참고
-> pip install couchdb 필요
-> 기본 centos7 에는 2.7버전이 기본 내장. <- http://victorydntmd.tistory.com/256 을 참고하여 3.6으로 변환하여 작업 진행
-> wget --ftp-user=dnp --ftp-password=1234 ftp://dnpcloud.ipdisk.co.kr/HDD1/Torrent/foodchain.zip 사용하여 다운로드 가능.
-> 압축을 출기 위해서 yum install -y unzip 수행
-> 노드 안에서 자잘한 문제들 발생... <- 변수가 많아서 생략
-> 테스트를 진행한 Node_Test_History.txt 별도 저장
2. 데이터화하여 전송을 완료했지만 데이터를 파일로 변환하는 과정이 없었던 부분 추가 완료.
-> test.py의 2번 항목 작업 완료
-> Foodchain.py 의 15번 항목 서버열기 와 test.py의 2번 항목 tx 보내기 를 테스트 함. <- 정상작동 확인
-> 2018.08.17_test1.png, 2018.08.17_test2.png 항목으로 확인 가능