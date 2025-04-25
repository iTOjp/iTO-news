
import streamlit as st
import requests
from datetime import datetime
import feedparser

MEDIA_FEEDS = {
    "BBC News（イギリス）": "http://feeds.bbci.co.uk/news/rss.xml",
    "Reuters（イギリス）": "http://feeds.reuters.com/reuters/topNews",
    "The New York Times（アメリカ）": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "The Washington Post（アメリカ）": "http://feeds.washingtonpost.com/rss/national"
}

st.set_page_config(page_title="世界の代表メディア 最新ニュース（翻訳なし）", layout="wide")
st.title("🗞️ 世界の代表メディア 最新ニュース（翻訳なし）")
st.caption(f"version 1.0.0 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

for name, url in MEDIA_FEEDS.items():
    st.subheader(name)
    with st.spinner("ニュースを取得しています…"):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:10], 1):
                st.markdown(f"**{i}. {entry.title}**")
                st.markdown(f"[原文を読む]({entry.link})")
        else:
            st.error("ニュース記事を取得できませんでした。")
