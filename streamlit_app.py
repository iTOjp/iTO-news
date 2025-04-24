
import streamlit as st
import requests
from googletrans import Translator
from datetime import datetime

API_KEY = "8091deb44d58406f4b38ea5b1b23fac4"
API_URL = "https://gnews.io/api/v4/top-headlines"

st.set_page_config(page_title="米国ニュース翻訳ビューア", layout="wide")
st.title("🇺🇸 アメリカのトップニュース（翻訳つき）")
st.caption("📄 version 0.3-us / build: 2025-04-24 17:31:35 JST")

translator = Translator()

params = {
    "token": API_KEY,
    "country": "us",
    "lang": "en",
    "max": 10,
}

try:
    st.info("ニュースを取得しています...")
    res = requests.get(API_URL, params=params, timeout=10)
    res.raise_for_status()
    data = res.json()
    articles = data.get("articles", [])

    if not isinstance(articles, list) or not articles:
        st.warning("記事が取得できませんでした。")
    else:
        for idx, article in enumerate(articles, 1):
            title_en = article.get("title", "")
            url = article.get("url", "#")
            try:
                title_ja = translator.translate(title_en, src="en", dest="ja").text
            except:
                title_ja = "(翻訳失敗) " + title_en
            st.markdown(f"**{idx}. {title_ja}**  [原文]({url})")
except Exception as e:
    st.error(f"⚠️ エラーが発生しました: {e}")
