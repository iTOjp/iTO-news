
import streamlit as st
import requests
from datetime import datetime
from googletrans import Translator

API_KEY = "pub_828414f2650027ef032005a0dc43452796878"
DOMAINS = {
    "us": {"media": "CNN", "domain": "cnn.com"},
    "de": {"media": "Der Spiegel", "domain": "spiegel.de"},
    "fr": {"media": "Le Monde", "domain": "lemonde.fr"},
}

def get_news(domain):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&domain={domain}&language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("results", [])
    except Exception as e:
        return f"エラー: {e}"

def translate_text(text, translator):
    try:
        return translator.translate(text, dest='ja').text
    except:
        return text

st.set_page_config(page_title="世界ニュース比較アプリ", layout="wide")
st.title("🌍 世界3か国の代表メディア トップ10（翻訳つき）")

st.caption(f"🧾 version 0.7 / build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

translator = Translator()

for country, info in DOMAINS.items():
    st.subheader(f"{country.upper()} {info['media']}（{country.upper()}）のトップニュース")
    news_data = get_news(info["domain"])
    if isinstance(news_data, str):
        st.warning(news_data)
    elif not news_data:
        st.info("記事が取得できませんでした。")
    else:
        for i, article in enumerate(news_data[:10], 1):
            title = article.get("title", "No title")
            url = article.get("link", "#")
            translated = translate_text(title, translator)
            st.markdown(f"{i}. {translated} [原文]({url})")
