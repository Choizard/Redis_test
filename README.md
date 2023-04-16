# Redis_test
레디스 설치 및 서버 실행, 코드 테스트

## WSL (Ubuntu) 내에 설치 및 서버 실행

1. 윈도우 업데이트 최신화 및 재시작 (에러발생 방지)

2. 재시작 후 설치 (경로 : /usr/bin/redis-server)

$ sudo apt-add-repository ppa:redislabs/redis
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install redis-server

3. 서버 실행

$ sudo service redis-server start

4. 실행 확인 및 명령어 입력 ( WSL 하나 더 실행 )

$ redis-cli
127.0.0.1:6379> ping
PONG




