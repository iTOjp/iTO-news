
import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="世界ニュース翻訳ビューア", layout="wide")
st.title("🌍 世界3か国の代表メディア トップ10（翻訳つき）")
st.caption("📄 version 0.6 / build: 2025-04-25 02:38:02 JST")

translator = Translator()

news_sources = [
    {"country": "us", "media": "CNN", "domain": "cnn.com", "flag": "🇺🇸"},
    {"country": "de", "media": "Der Spiegel", "domain": "spiegel.de", "flag": "🇩🇪"},
    {"country": "fr", "media": "Le Monde", "domain": "lemonde.fr", "flag": "🇫🇷"},
]

API_KEY = "8091deb44d58406f4b38ea5b1b23fac4"

def fetch_news(domain):
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": API_KEY,
        "domain": domain,
        "language": "en",
    }
    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json().get("results", [])
    except Exception as e:
        return f"エラー: {str(e)}"

for source in news_sources:
    st.subheader(f"{source['flag']} {source['media']}（{source['country'].upper()}）のトップニュース")
    with st.spinner("取得中..."):
        result = fetch_news(source["domain"])
        if isinstance(result, str):
            st.warning(result)
            continue
        if not result:
            st.info("記事が取得できませんでした。")
            continue
        for idx, article in enumerate(result[:10], 1):
            title = article.get("title", "")
            link = article.get("link", "#")
            try:
                title_ja = translator.translate(title, src="en", dest="ja").text
            except:
                title_ja = "(翻訳失敗) " + title
            st.markdown(f"**{idx}. {title_ja}** [原文]({link})")
    st.markdown("---")
