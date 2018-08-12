# foodchain

이 프로잭트는 군산대학교 컴퓨터 정보 공학과와 순천대학교와 협업 프로잭트로써 국가 사업에 기반한다.
농수산 식품의 이력 관리 및 추적 시스템을 블록체인으로써 구현하는 것을 목표로 한다.
필자는 군산대학교 컴퓨터 정보 공학과 소속 학생이고 DAD 연구실에 소속되어있다.

현재 A팀, B팀으로 나누어져 개발, 연구가 진행중이다

A팀은 P2P, 맴버쉽, 암호화
B팀은 분산원장, 분산합의, 트랜잭션

필자는 B팀에 속해있고 분산원장을 다루고 있다.

기본적으로 트랜잭션과 분산원장이 기본 블록체인의 폼을 따르기 때문에
이 프로그램은 자체 제작으로 순수한 이론적 개념을 어떤 참조없이 창작한 것을 명시한다.

추가적으로 gRPC, couchDB등 참조가 생기면 분명히 명시를 할 것이다.

현재 버젼은 아주 기본적인 부분조차 구현이 안되어있기 때문에 파이썬의 기본 모듈로써 작업이 가능했다.

***
## 파일 구조
* foodchain
  * chaincode
    - blockToJson.py            # 합의를 위한 블록 생성
    - chainToJson.py            # 새로운 장부 만들기, 장부에 내역 추가
    - client_Json.py
    - randFileName.py           # 각 인터페이스 이름 생성
    - server_Json.py
    - transactionToJson.py      # 트랜잭션 재안서(.json) 저장
  * client
    - client.py
  * data_server
    
  * flagdb
    - kvstore.py                # 하이퍼랫저 패브릭의 Worldstate 기능
  * hash256
    - hash256.py                # hash256 구현 <- hashlib 참조
  * ledger
    - block.py                  # 블록 인터페이스
    - blockheader.py            # 블록헤더 인터페이스
    - chain.py                  # 체인 인터페이스
    - transaction.py            # 트랜잭션 인터페이스
  * msp
    - msp.py
  * Stakeholder
    - Stakeholder.py            # 합의 알고리즘
  * synchronize
    - synchronize.py            # 기존 원장 무결성 채크
  - Foodchain.py                # 종합 예제
  - metadata.py                 # 이 프로그램의 metadata
  - readme.txt                  # 패치노트
  
