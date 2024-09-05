import os
import streamlit as st
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Streamlit SecretsからAPIキーを取得
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    st.error("APIキーが設定されていません。")

openai.api_key = api_key

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

# ボタン
if st.button("自己紹介文を生成"):
    if university and age and skills and why_hire:
        # プロンプト作成
        prompt = (
            f"以下の情報を基に、企業向けの自己紹介文を生成してください。\n\n"
            f"出身大学（学部）: {university}\n"
            f"年齢: {age}\n"
            f"スキル: {skills}\n"
            f"企業に貢献できるポイント: {why_hire}\n"
            f"追加情報: {additional_info}\n\n"
            "自己紹介文:"
        )
        
        # OpenAI APIリクエストの送信
        completion = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=400,
            temperature=0.7,
        )
        
        # 自己紹介文の出力
        introduction = completion.choices[0].text.strip()
        st.success("自己紹介文が生成されました！")
        st.write(introduction)
    else:
        st.error("すべての必須フィールド（出身大学、年齢、スキル、貢献ポイント）を入力してください。")
