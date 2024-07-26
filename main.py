from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
import os

load_dotenv()
API_KEY = os.getenv('OPEN_API_KEY')

# Chat 모드
llm = ChatOpenAI(api_key=API_KEY)




# Complete 모드
# llm = OpenAI(api_key=API_KEY)
# result = llm.invoke("코딩에 대한 시를 써줘")
# print(result)



import streamlit as st
st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시 해주세요.")
# st.write(f"시의 주제는? {title}")

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        result = llm.invoke(f"{content}에 대한 시를 써줘")
        st.write(f"{result.content}")
