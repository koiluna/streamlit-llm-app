# APIKEYの設定
from dotenv import load_dotenv
load_dotenv()

# Webアプリの作成
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("LLMを使って専門家に質問するアプリ")

st.write("##### 専門家A: 医療分野の専門家")
st.write("医療分野に関する質問を入力すると、LLMが回答します。")
st.write("##### 専門家B: 農業分野の専門化")
st.write("農業分野に関する質問を入力すると、LLMが回答します。")

selected_item = st.radio(
    "質問したい専門家を選択してください。",
    ["医療分野の専門家", "農業分野の専門家"]
)

input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "医療分野の専門家":
        messages = [
            SystemMessage(content="あなたは医療分野の専門家です。"),
            HumanMessage(content=input_message),
            ]
        result = llm(messages)
        st.write({result})
    else:
        messages = [
            SystemMessage(content="あなたは農業分野の専門家です。"),
            HumanMessage(content=input_message),
            ]
        result = llm(messages)
        st.write({result})