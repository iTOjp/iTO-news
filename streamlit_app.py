import streamlit as st
import feedparser
from datetime import datetime
import deepl

translator = deepl.Translator("5471786a-d12e-4f9d-978f-a7ed048b9452:fx")

def translate(text):
    try:
        return translator.translate_text(text, target_lang="JA").text
    except Exception as e:
        return f"[翻訳エラー: {e}]"

st.set_page_config(page_title="愛輝！世界の代表メディア 最新ニュース", layout="wide")
st.title("愛輝！世界の代表メディア 最新ニュース")
st.caption(f"version 1.3.0 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

MEDIA_FEEDS = {
    "BBC News（イギリス）": "http://feeds.bbci.co.uk/news/rss.xml",
    "Reuters（Google経由・国際）": "https://news.google.com/rss/search?q=site:reuters.com&hl=en-US&gl=US&ceid=US:en",
    "The New York Times（アメリカ）": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "The Washington Post（アメリカ）": "http://feeds.washingtonpost.com/rss/national",
    "Le Monde（フランス）": "https://www.lemonde.fr/rss/une.xml",
    "Der Spiegel（ドイツ）": "https://www.spiegel.de/international/index.rss",
    "中国網（中国）": "http://www.china.org.cn/rss/china_rss.xml",
    "Folha de S.Paulo（ブラジル）": "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
    "NHKニュース（日本）": "https://www3.nhk.or.jp/rss/news/cat0.xml"
}

for name, url in MEDIA_FEEDS.items():
    st.subheader(name)
    with st.spinner("ニュースを取得中..."):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:5], 1):
                translated = translate(entry.title)
                st.markdown(f"**{i}. {translated}**")
                st.markdown(f"`{entry.title}`")
                st.markdown(f"[🔗 原文を読む]({entry.link})")
                st.markdown("---")
        else:
            st.warning("記事が取得できませんでした。")
