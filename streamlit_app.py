import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを環境変数から取得
openai_api_key = os.getenv('OPENAI_API_KEY')

# OpenAIクライアントを作成
client = OpenAI(api_key=openai_api_key)

# StreamlitのUI
st.title("自己紹介文生成アプリ")

# 入力フォーム
university = st.text_input("出身大学（学部）を入力してください:")
age = st.text_input("年齢を入力してください:")
skills = st.text_area("あなたのスキルを入力してください (例: Python, データ分析, マネジメント):")
why_hire = st.text_area("企業に貢献できるポイントを入力してください (例: 強みや経験):")
additional_info = st.text_area("追加情報を入力してください (例: 性格、情熱、目標など):")
