
import streamlit as st
import feedparser
from datetime import datetime
import requests
import time

DEEPL_API_KEY = "5471786a-d12e-4f9d-978f-a7ed048b9452:fx"
DEEPL_USAGE_URL = "https://api-free.deepl.com/v2/usage"

def check_deepl_quota():
    try:
        response = requests.get(DEEPL_USAGE_URL, headers={"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"})
        data = response.json()
        return data.get("character_count", 0), data.get("character_limit", 500000)
    except:
        return 500000, 500000

def translate(text):
    char_used, char_limit = check_deepl_quota()
    if char_used < char_limit - 10000:
        try:
            deepl_result = requests.post(
                "https://api-free.deepl.com/v2/translate",
                data={"auth_key": DEEPL_API_KEY, "text": text, "target_lang": "JA"}
            )
            return deepl_result.json()["translations"][0]["text"]
        except:
            pass
    try:
        result = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={"client": "gtx", "sl": "en", "tl": "ja", "dt": "t", "q": text}
        )
        return result.json()[0][0][0] + "＊"
    except:
        return "[翻訳失敗]"

st.set_page_config(page_title="愛輝！世界の最新ニュース", layout="wide")
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

st.title("💖 愛輝！世界の最新ニュース")
st.caption(f"version 1.8.1 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

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

for name, url in MEDIA_FEEDS.items():
    st.markdown(f"<div class='media-block'><h3>{name}</h3></div>", unsafe_allow_html=True)
    with st.spinner("ニュースを取得中..."):
        feed = feedparser.parse(url)
        if feed.entries:
            for i, entry in enumerate(feed.entries[:3], 1):
                translated = translate(entry.title)
                card_html = f'''
<div class="card">
<b>{i}. {translated}</b><br>
<code>{entry.title}</code><br>
<a href="{entry.link}" target="_blank">&#128279; 原文を読む</a>
</div>
'''
                st.markdown(card_html, unsafe_allow_html=True)
                time.sleep(0.1)
        else:
            st.warning("記事が取得できませんでした。")
