import streamlit as st
import feedparser
from datetime import datetime
import requests

def translate(text, target_lang="JA"):
    try:
        res = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={
                "client": "gtx",
                "sl": "auto",
                "tl": target_lang,
                "dt": "t",
                "q": text,
            },
            timeout=5,
        )
        return res.json()[0][0][0]
    except Exception as e:
        return f"[翻訳エラー: {e}]"

st.set_page_config(page_title="愛輝！世界の代表メディア 最新ニュース（翻訳あり）", layout="wide")
st.title("🗞️ 世界の代表メディア 最新ニュース（日本語翻訳付き）")
st.caption(f"version 1.1.0 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

MEDIA_FEEDS = {
    "BBC News（イギリス）": "http://feeds.bbci.co.uk/news/rss.xml",
    "Reuters（Googleニュース経由）": "https://news.google.com/rss/search?q=site:reuters.com&hl=en-US&gl=US&ceid=US:en",
    "The New York Times（アメリカ）": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "The Washington Post（アメリカ）": "http://feeds.washingtonpost.com/rss/national"
}

for name, url in MEDIA_FEEDS.items():
    st.subheader(name)
    with st.spinner("ニュースを取得しています..."):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:10], 1):
                jp_title = translate(entry.title)
                st.markdown(f"**{i}. {jp_title}**")
                st.markdown(f"[🔗 原文を読む]({entry.link})")
                st.markdown("---")
        else:
            st.warning("記事が取得できませんでした。")
