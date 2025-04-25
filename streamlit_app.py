import streamlit as st
import feedparser
from datetime import datetime
import urllib.parse

# ✅ アプリの設定
st.set_page_config(page_title="ワシントンポストの最新ニュース", layout="wide")
st.title("📰 ワシントンポストの最新ニュース（翻訳なし）")
st.caption(f"version 0.9.3 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

# ✅ RSS URL（Washington Post の RSS フィード）
RSS_URL = "https://feeds.washingtonpost.com/rss/national"

# ✅ ニュースを取得する関数
def fetch_rss(url):
    try:
        feed = feedparser.parse(url)
        return feed.entries[:10]
    except Exception as e:
        st.error(f"ニュース取得エラー: {e}")
        return []

# ✅ 表示処理
with st.spinner("ニュースを取得しています..."):
    articles = fetch_rss(RSS_URL)

if articles:
    for i, entry in enumerate(articles, 1):
        st.markdown(f"**{i}. {entry.title}**")
        st.markdown(f"[原文を見る]({entry.link})")
        st.markdown("---")
else:
    st.warning("記事を取得できませんでした。")
