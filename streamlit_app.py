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
.card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 1em;
    margin-bottom: 1em;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
.media-block {
    background-color: #ffe6f0;
    border-left: 6px solid #ff69b4;
    border-radius: 10px;
    padding: 0.5em 1em;
    margin-top: 2em;
    margin-bottom: 1em;
}
</style>
""", unsafe_allow_html=True)
st.title("💖 愛輝！世界の代表メディア 最新ニュース")
st.caption(f"version 1.8.0 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

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
    "🇶🇦 Al Jazeera（カタール）": "https://www.aljazeera.com/xml/rss/all.xml",
    "🇦🇺 ABC News（豪）": "https://www.abc.net.au/news/feed/51120/rss.xml"
}

card_template = """
<div class="card">
<b>{i}. {translated}</b><br>
<code>{original}</code><br>
<a href="{link}" target="_blank">&#128279; 原文を読む</a>
</div>
"""

for name, url in MEDIA_FEEDS.items():
    st.markdown(f"<div class='media-block'><h3>{name}</h3></div>", unsafe_allow_html=True)
    with st.spinner("ニュースを取得中..."):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:3], 1):
                translated = translate(entry.title)
                card_html = card_template.format(i=i, translated=translated, original=entry.title, link=entry.link)
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            st.warning("記事が取得できませんでした。")
