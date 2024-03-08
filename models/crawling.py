import aiohttp
from dateutil.relativedelta import relativedelta
import json
import pandas as pd
from datetime import datetime
import asyncio
import sys
import time
import os


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def fetch_data(session, url, headers, body):
    async with session.post(url, headers=headers, data=body) as response:
        try:
            response.raise_for_status()
            return await response.json()
        except aiohttp.ClientResponseError as e:
            # 예외 발생 시 URL 정보와 함께 커스텀 예외 메시지를 생성
            raise aiohttp.ClientResponseError(
                response.request_info,
                response.history,
                status=e.status,
                message=f"{e.message}, URL='{response.url}'",
            ) from e


def set_time_range(std_time, days_before=1, years_before=4):
    """
    기준 시간을 바탕으로 지정된 일수 전과 년수 전의 날짜를 계산하여 반환합니다.

        매개변수:
    - std_time: 기준이 되는 datetime 객체
    - days_before: 계산할 이전 일수 (기본값: 1일 전)
    - years_before: 계산할 이전 년수 (기본값: 4년 전)
    """
    end_time = (std_time - relativedelta(days=days_before)).strftime("%Y-%m-%d")
    start_time = (
        std_time - relativedelta(years=years_before, days=days_before)
    ).strftime("%Y-%m-%d")
    return start_time, end_time


async def trend_load_async(std_time, search_keyword, client_id, client_secret, url):
    start_time, end_time = set_time_range(std_time)
    data = {
        "startDate": start_time,
        "endDate": end_time,
        "timeUnit": "date",
        "keywordGroups": [{"groupName": search_keyword, "keywords": [search_keyword]}],
    }
    body = json.dumps(data)
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "Content-Type": "application/json",
    }

    async with aiohttp.ClientSession() as session:
        result = await fetch_data(session, url, headers, body)
        date = [item["period"] for item in result["results"][0]["data"]]
        ratio_data = [item["ratio"] for item in result["results"][0]["data"]]
        df_search_trend = pd.DataFrame(
            {"date": date, search_keyword: ratio_data}
        ).set_index("date")
        return df_search_trend


async def trend_maincode(params, api_url):
    standard_time = datetime.now()
    search_keywords = params.get("search_keywords", [])
    client_id = params.get("id")
    client_secret = params.get("pw")

    results = []
    for keyword in search_keywords:
        try:
            df_search_trend = await trend_load_async(
                standard_time, keyword, client_id, client_secret, api_url
            )
            results.append(df_search_trend)
            # 성공적으로 데이터를 받아왔으므로, 다음 키워드로 넘어갑니다.
        except aiohttp.ClientResponseError as e:
            if e.status == 429:
                print(f"클라이언트 오류 발생: {e.status}, 메시지='{e.message}'")
                break  # 더 이상 다른 클라이언트로 넘어가지 않고 처리를 중단합니다.
            else:
                raise  # 다른 HTTP 오류는 그대로 예외를 발생시킵니다.
        except Exception as e:
            print(f"예상치 못한 오류 발생: {e}")
            break  # 중대한 오류로 인한 처리 중단

    return results


async def main(params):
    # 메인 코드 블록
    api_url = "https://openapi.naver.com/v1/datalab/search"
    # 이벤트 루프 실행 대신 await 사용
    results = await trend_maincode(params, api_url)
    # 상위 디렉토리 (rse112.github.io/) 에 data.json 파일의 경로를 구성
    return results

    # 파라미터


# 데이터 처리 및 파일 저장 로직...

import asyncio
import json
import os

import sys

# 현재 스크립트의 디렉토리 경로를 얻음
current_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 디렉토리 경로를 계산
parent_dir = os.path.dirname(current_dir)
# sys.path에 상위 디렉토리 경로를 추가
sys.path.append(parent_dir)
from utils.config import NAVER_API_ID, NAVER_API_SECRET

# 기존의 비동기 함수 및 main 함수 정의...

if __name__ == "__main__":
    params = {
        "search_keywords": [
            "디도스",
            "클라우드 보안",
            "사이버 공격",
            "주식",
            "비트코인",
            "테슬라",
            "삼성전자",
            "네이버",
            "퇴직연금",
        ],
        "id": NAVER_API_ID,
        "pw": NAVER_API_SECRET,
        "api_url": "https://openapi.naver.com/v1/datalab/search",
        "name": "name",
    }
    results = asyncio.run(main(params))

    if results:  # results 리스트가 비어있지 않은지 확인
        reset_a = results[0].reset_index()  # 첫 번째 결과 사용
        # 데이터를 리스트와 딕셔너리 형태로 변환
        b = {
            "date": reset_a["date"].tolist(),
            "value": reset_a[reset_a.columns[1]].tolist(),
        }

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        data_file_path = os.path.join(parent_dir, "data.json")

        print(data_file_path)
        # 데이터를 JSON 파일에 저장
        try:
            with open(data_file_path, "w") as json_file:
                json.dump(b, json_file)
            print(f"Data saved to {data_file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

    else:
        print("No data to save.")
