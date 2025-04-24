
import streamlit as st
import requests

VERSION = "0.4"
BUILD_TIME = "2025-04-24 17:25:12 JST"

def translate_to_japanese(text):
    return text

news_sources = [
    {"country": "us", "lang": "en", "name": "アメリカ", "media": "代表メディア"},
    {"country": "de", "lang": "de", "name": "ドイツ", "media": "代表メディア"},
    {"country": "fr", "lang": "fr", "name": "フランス", "media": "代表メディア"},
    {"country": "cn", "lang": "zh", "name": "中国", "media": "代表メディア"},
    {"country": "jp", "lang": "ja", "name": "日本", "media": "代表メディア"},
]

API_KEY = "8091deb44d58406f4b38ea5b1b23fac4"
API_URL = "https://gnews.io/api/v4/top-headlines"

st.set_page_config(page_title="世界ニュース比較ビューア", layout="wide")
st.title("🌍 世界5カ国の代表メディア トップ10（翻訳つき）")
st.caption(f"📄 ビルド: version {VERSION} / {BUILD_TIME}")

for info in news_sources:
    st.subheader(f"{info['country'].upper()} {info['name']}のトップニュース（{info['media']}）")
    params = {
        "apikey": API_KEY,
        "country": info["country"],
        "lang": info["lang"],
        "max": 10,
    }
    try:
        res = requests.get(API_URL, params=params, timeout=10)
        data = res.json()
        articles = data.get("articles", [])
        if not isinstance(articles, list) or not articles:
            st.warning("記事が取得できませんでした。")
            continue
        for i, article in enumerate(articles[:10], 1):
            title = article.get("title", "No Title")
            url = article.get("url", "#")
            st.markdown(f"{i}. [{translate_to_japanese(title)}]({url})")
    except Exception as e:
        st.error(f"⚠️ ニュース取得時にエラーが発生しました: {e}")
