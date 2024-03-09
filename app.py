import streamlit as st

st.title("Welcome to My Streamlit Homepage!")

st.write(
    "This is a simple Streamlit Webpage. You can add more interactive elements here.zzzzz"
)


# 사용자 입력 받기
user_input = st.text_input("Enter your name:")

# 버튼 추가
if st.button("Say Hello"):
    st.write(f"Hello, {user_input}!")
