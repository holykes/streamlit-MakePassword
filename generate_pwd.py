import streamlit as st
import random
import string


def generate_password():
    # 8자리의 무작위 암호 생성
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return password


# Streamlit 애플리케이션 시작
st.title("암호 생성 프로그램")

# "암호 생성" 버튼
if st.button("암호 생성"):
    # 암호 생성 함수 호출
    password = generate_password()

    # 생성된 암호 출력
    st.success(f"생성된 암호: {password}")
