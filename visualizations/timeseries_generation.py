from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import os

import sys

# 현재 스크립트의 디렉토리 경로를 얻음
current_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 디렉토리 경로를 계산
parent_dir = os.path.dirname(current_dir)
# sys.path에 상위 디렉토리 경로를 추가
sys.path.append(parent_dir)
from utils.config import MONGO_DB_URL, MONGO_DB_NAME

# MongoDB 클라이언트 생성
client = MongoClient(MONGO_DB_URL)

# 데이터베이스와 컬렉션 선택
db = client[MONGO_DB_NAME]
collection = db["data_json"]

# MongoDB에서 데이터 로드
data = (
    collection.find_one()
)  # 데이터를 하나만 가져옵니다. 여러 데이터를 다루려면 find() 사용

# Pandas DataFrame으로 변환
df = pd.DataFrame(data)

# 'date' 열을 datetime 객체로 변환
df["date"] = pd.to_datetime(df["date"])

# 시계열 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["value"], marker="o", linestyle="-")
plt.title("Time Series Graph")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.xticks(rotation=45)  # 날짜 레이블을 45도 회전
plt.tight_layout()  # 그래프 레이아웃을 조정

plt.savefig("timeseries_graph.png")  # 그래프를 이미지 파일로 저장
plt.show()  # 그래프 보여주기
