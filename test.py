import redis

# Redis 클라이언트 생성
r = redis.Redis(host='localhost', port=6379, db=0)

# 데이터 저장
r.set('test', 'success')

# 데이터 불러오기
value = r.get('test')
print(value)
