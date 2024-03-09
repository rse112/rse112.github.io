import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
import matplotlib.font_manager as fm
import sys

# 한글 폰트 및 마이너스 기호 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 현재 스크립트 위치 및 상위 디렉토리 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.get_data import DataLoader

# 데이터 로더 인스턴스 생성 및 데이터 로드
data_loader = DataLoader.get_instance()
keyword = "비트코인"
stock_data = data_loader.get_data(keyword)

# 데이터 프레임 변환 및 'date' 열 datetime 변환
df = pd.DataFrame(stock_data)
df["date"] = pd.to_datetime(df["date"])

# 그래프 저장 경로 설정
today_str = datetime.now().strftime("%y%m%d")
graph_dir = os.path.join("graph", today_str)
os.makedirs(graph_dir, exist_ok=True)
graph_file_path = os.path.join(graph_dir, f"{keyword}_graph.png")

# 시계열 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["value"], marker="o", linestyle="-", markersize=1)
plt.title(f"{keyword} Graph")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 저장 및 출력
plt.savefig(graph_file_path)
plt.show()

print(f"Graph saved to {graph_file_path}")
