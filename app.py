import streamlit as st
import feedparser

st.set_page_config(page_title="CNNニュース翻訳ビューア", layout="wide")
st.title("📰 CNN トップニュース（翻訳なし）")
st.caption("version 1.0 / CNN RSSフィードより取得")

# CNN RSSフィードURL
rss_url = "https://rss.cnn.com/rss/cnn_topstories.rss"

# RSSパース
feed = feedparser.parse(rss_url)

if not feed.entries:
    st.error("RSSフィードを取得できませんでした。")
else:
    for i, entry in enumerate(feed.entries[:10], 1):
        title = entry.title
        link = entry.link
        st.markdown(f"**{i}. {title}**  
[原文はこちら]({link})")