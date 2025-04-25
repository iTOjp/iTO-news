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
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #fff0f5;
}
h1, h2, .stMarkdown {
    color: #ff69b4 !important;
}
.stMarkdown {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)
st.title("💖 愛輝！世界の代表メディア 最新ニュース")
st.caption(f"version 1.6.0 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

MEDIA_FEEDS = {
    "🌐 Reuters（世界）": "https://news.google.com/rss/search?q=site:reuters.com&hl=en-US&gl=US&ceid=US:en",
    "🇺🇸 CNN（米）": "https://news.google.com/rss/search?q=site:cnn.com&hl=en-US&gl=US&ceid=US:en",
    "🇯🇵 NHKニュース（日本）": "https://www3.nhk.or.jp/rss/news/cat0.xml",
    "🇬🇧 BBC News（英）": "http://feeds.bbci.co.uk/news/rss.xml",
    "🇫🇷 Le Monde（仏）": "https://www.lemonde.fr/rss/une.xml",
    "🇩🇪 Der Spiegel（独）": "https://www.spiegel.de/international/index.rss",
    "🇷🇺 TASS（露）": "https://tass.com/rss/v2.xml",
    "🇭🇰 SCMP（中国）": "https://www.scmp.com/rss/91/feed",
    "🇧🇷 Folha de S.Paulo（ブラジル）": "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
    "🇶🇦 Al Jazeera（カタール）": "https://www.aljazeera.com/xml/rss/all.xml"
}

for name, url in MEDIA_FEEDS.items():
    st.subheader(name)
    with st.spinner("ニュースを取得中..."):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:3], 1):
                translated = translate(entry.title)
                st.markdown(f"**{i}. {translated}**")
                st.markdown(f"`{entry.title}`")
                st.markdown(f"[🔗 原文を読む]({entry.link})")
                st.markdown("---")
        else:
            st.warning("記事が取得できませんでした。")
