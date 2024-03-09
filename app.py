# my_app.py
import streamlit as st
from streamlit_elements import elements, mui


# Streamlit 애플리케이션의 메인 페이지를 정의합니다.
def main():
    with elements("new_element"):  # elements 프레임 생성
        mui.Typography(
            "Hello world"
        )  # "Hello world" 텍스트를 표시하는 Typography 컴포넌트


# 스크립트가 직접 실행될 때만 main 함수를 호출합니다.
main()
