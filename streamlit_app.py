import streamlit as st
import requests
from datetime import datetime

API_KEY = "pub_828414f2650027ef032005a0dc43452796878"
DOMAINS = {
    "アメリカ（CNN）": "cnn.com",
    "ドイツ（Der Spiegel）": "spiegel.de",
    "フランス（Le Monde）": "lemonde.fr",
}

st.set_page_config(page_title="ニュース比較ビューア", layout="wide")
st.title("🌍 世界3か国の代表メディア トップ10（翻訳なし）")
st.caption(f"version 0.9.2 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

def fetch_news(domain):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&domain={domain}&language=en"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json().get("results", [])
    except Exception as e:
        return f"エラー: {e}"

for name, domain in DOMAINS.items():
    st.subheader(name)
    with st.spinner("ニュースを取得しています..."):
        news = fetch_news(domain)
        if isinstance(news, str):
            st.warning(news)
        elif not news:
            st.info("記事が取得できませんでした。")
        else:
            for i, article in enumerate(news[:10], 1):
                title = article.get("title", "No title")
                url = article.get("link", "#")
                st.markdown(f"{i}. {title} [原文]({url})")
    st.markdown("---")