# foodchain
## 개요
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

## 1차 정식 수정
팀 구조 변경

A 팀 : P2P
B 팀 : 분산원장, 분산합의, 트랜잭션, 맴버쉽, 암호화

기본적으로 이런 구조이긴 하지만 앞으로 진행하면서 또 다르게 바뀔 가능성이 매우 충분하다.
아래 개발 환경은 팀 전부의 개발환경이 아닌 필자 혼자만의 개발 환경임.

이번 팀 조정으로 인해서 암호화와 기존 foodchain과 합치는 중 pycrypto를 불러오는 과정에서 오류가 발생함.
아나콘다3 5.1.0 (3.6 - 32bit) 버전으로 통합할 가능성이 충분함.
테스트 빌드 환경이 파이썬 3.6.5 32bit 환경이여서 필요한 모듈을 전부 pip를 이용하여 설치했으나 추후 조정을 하여 아나콘다와 순정 파이썬과의 조율이 있을 예정.

처음부터 그래왔지만 이 소스들은 B팀에 속해있는 필자가 주도적으로 만들었기 때문에 A팀에 관련된 소스는 거의 없고 통신에 관련된 내용은 전부 B팀 자체적으로 추가한 부분임을 밝힘.


***
## 개발 환경
* H/W 1
	- CPU
		Ryzen 1600 (3.7 O.C)
	- ram
		samsung ddr4 8gb x 2 (3200 O.C)
	- VGA
		GTX 970 4gb
	- M2
		1tb (2280)

* S/W 1
	- 윈도우 10 RS5 insight preview (64 bit)
	- 비주얼 스튜디오 2017 커뮤니티
	- 파이썬 3.6.5 (32, 64 bit)
	- 아나콘다3 (32, 64 bit)


	
* H/W 2
	- CPU
		i7 3770
	- ram
		samsung ddr3 8gb x 2
	- VGA
		GTX 750ti 1gb
	- M2
		SSD 240gb

* S/W 2
	- 윈도우 10 RS4 (64 bit)
	- 비주얼 스튜디오 2017 커뮤니티
	- 파이썬 3.6.5 (32, 64 bit)
	- 아나콘다3 (32, 64 bit)


***
## 파일 구조
* foodchain
  * chaincode
    - blockToJson.py            # 합의를 위한 블록 생성
    - chainToJson.py            # 새로운 장부 만들기, 장부에 내역 추가
    - client_Json.py
    - randFileName.py           # 각 인터페이스 이름 생성
    - leader_rand.py            # 트랜잭션 종합을 위해 리더가 생성하는 랜덤 값
    - socket_Json.py			# Foodchain.py 에 쓰이는 소켓 통신
    - server_Json.py			# test.py 에 쓰이는 소켓 통신
    - transactionToJson.py      # 트랜잭션 재안서(.json) 저장

  * client
    - client.py					# 역활별 기능 제한을 구현할 예정
	
  * data_client

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

  * test_result					# 테스트를 하면서 생기는 로그나 캡쳐등 증빙자료

  - Foodchain.py                # 종합 예제
  - metadata.py                 # 이 프로쟉트의 metadata
  - readme.txt                  # 패치노트
  - test.py						# 9.4일 순천대 발표를 위한 소스
  
