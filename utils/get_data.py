import json
from pathlib import Path
from typing import Optional


class DataLoader:
    _instance = None
    _data = None

    @staticmethod
    def get_instance():
        if DataLoader._instance is None:
            DataLoader._instance = DataLoader()
        return DataLoader._instance

    def __init__(self):
        if DataLoader._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DataLoader._instance = self
            self.load_data()

    def load_data(self):
        json_path = Path(__file__).resolve().parent.parent / "data.json"
        with open(json_path) as f:
            DataLoader._data = json.load(f)

    @staticmethod
    def get_data(keyword: str) -> Optional[dict]:
        data = DataLoader._data.get(keyword)
        if data is not None:
            return data
        else:
            raise EnvironmentError(
                f"Set the {keyword} environment variable or include it in data.json"
            )


keyword = [
    "주식",
    "비트코인",
    "금값",
    "주식",
    "알트코인",
    "테슬라",
    "삼성전자",
    "네이버",
    "퇴직연금",
]
# 반드시 이중에서 사용해야함

# DataLoader 인스턴스 생성 및 데이터 로드
data_loader = DataLoader.get_instance()

# 첫 번째 키워드에 해당하는 데이터를 가져옵니다.
keyword = "주식"
stock_data = data_loader.get_data(keyword)
print(stock_data)
