import streamlit as st
import requests
from datetime import datetime

API_KEY = "pub_828414f2650027ef032005a0dc43452796878"  # これは検証後、有効性が必要

# 今回は1メディアに限定
DOMAINS = {
    "ワシントン・ポスト（The Washington Post）": "washingtonpost.com"
}

st.set_page_config(page_title="ワシントンポスト ニュース", layout="wide")
st.title("📰 ワシントンポストの最新ニュース（翻訳なし）")
st.caption(f"version 0.9.3 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

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
        st.error(news)
    elif not news:
        st.warning("記事が取得できませんでした。")
    else:
        for idx, article in enumerate(news[:10], 1):
            st.markdown(f"{idx}. [{article.get('title')}]({article.get('link')})")
