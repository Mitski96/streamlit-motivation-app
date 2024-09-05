import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai

# OpenAI APIキーを設定
openai.api_key = os.getenv('OPENAI_API_KEY')

# StreamlitのUI
st.title("志望動機生成アプリ")

# 入力フォーム
url = st.text_input("企業のURLを入力してください:")
keywords = st.text_input("関連キーワードを入力してください（カンマで区切ってください）:")
details = st.text_area("詳細を入力してください:")

# サイトを探索し、リンクとテキストを取得する関数
def explore_site(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # ページ内のテキスト収集
        text_content = soup.get_text(separator="\n")
        
        return text_content
    except Exception as e:
        return f"エラーが発生しました: {e}"

# ボタン
if st.button("志望動機を生成"):
    if url and keywords:
        # サイトのテキストを取得
        site_text = explore_site(url)
        
        # キーワードをリストに変換
        keywords_list = [k.strip() for k in keywords.split(',')]
        
        # キーワードとサイトの情報を組み合わせてプロンプト作成
        prompt = (
            f"以下のキーワードを考慮して、次の企業に合った志望動機を生成してください。\n"
            f"キーワード: {', '.join(keywords_list)}\n\n"
            f"企業サイトのテキスト:\n{site_text[:1000]}...\n\n"  # テキストが長い場合はカット
            f"追加の詳細:\n{details}"
        )
        
        # OpenAI APIリクエストの送信
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=400
        )
        
        # 志望動機の出力
        motivation = response.choices[0].text.strip()
        st.success("志望動機が生成されました！")
        st.write(motivation)
    else:
        st.error("URLとキーワードは必須です。")

