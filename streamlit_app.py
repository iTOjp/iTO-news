
import streamlit as st
import feedparser
from datetime import datetime

# 表示設定
st.set_page_config(page_title="代表メディアニュース比較", layout="wide")
st.title("📰 世界の代表メディア 最新ニュース（翻訳なし）")
st.caption(f"version 0.9.4 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

# メディア一覧とRSS
RSS_FEEDS = {
    "CNN（アメリカ）": "https://rss.cnn.com/rss/cnn_topstories.rss",
    "ワシントン・ポスト（アメリカ）": "https://feeds.washingtonpost.com/rss/world"
}

# 表示処理
for media_name, feed_url in RSS_FEEDS.items():
    st.subheader(media_name)
    with st.spinner("ニュースを取得しています..."):
        try:
            feed = feedparser.parse(feed_url)
            for i, entry in enumerate(feed.entries[:10], 1):
                st.markdown(f"**{i}. {entry.title}**")
                st.markdown(f"[原文を読む]({entry.link})")
        except Exception as e:
            st.error(f"⚠ ニュースの取得に失敗しました: {e}")
