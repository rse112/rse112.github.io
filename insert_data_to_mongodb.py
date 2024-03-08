from pymongo import MongoClient
import json
from utils.config import MONGO_DB_NAME, MONGO_DB_URL

# MongoDB 클라이언트 생성
client = MongoClient(MONGO_DB_URL)

# 데이터베이스와 컬렉션 선택
db = client[MONGO_DB_NAME]
collection = db["data_json"]  # 컬렉션 이름을 지정

# data.json 파일에서 데이터 로드
with open("data.json") as f:
    data = json.load(f)

# 데이터 삽입
collection.insert_many(
    [data]
)  # data가 리스트 형태라면 insert_many, 딕셔너리라면 insert_one 사용

print("Data inserted into MongoDB.")
