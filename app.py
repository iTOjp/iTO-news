import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(page_title="Washington Post ニュース", layout="wide")

st.title("📰 Washington Post ニュースビューア（RSS）")
st.caption("version 1.0 / built: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

RSS_URL = "https://www.washingtonpost.com/rss/homepage"

with st.status("RSSからニュースを取得中...", expanded=False):
    feed = feedparser.parse(RSS_URL)

if feed.bozo:
    st.error("RSSの取得に失敗しました。通信環境をご確認ください。")
else:
    entries = feed.entries[:10]
    for i, entry in enumerate(entries, 1):
        st.markdown(f"**{i}. {entry.title}**")
        st.markdown(f"[🔗 記事を読む]({entry.link})")
