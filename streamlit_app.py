
import streamlit as st
import requests
from googletrans import Translator
from datetime import datetime

st.set_page_config(page_title="世界ニュース翻訳ビューア", layout="wide")
st.title("🌍 世界5カ国の代表メディア トップ10（翻訳つき）")
st.caption(f"🔄 ビルド: version 0.3 / {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} JST")

translator = Translator()

def fetch_and_display_news(name, media, domain, country_code, flag):
    st.subheader(f"{flag} {name}のトップニュース（{media}）")
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": "8091deb44d58406f4b38ea5b1b23fac4",
        "domain": domain,
        "language": "en",
        "country": country_code
    }
    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        articles = data.get("results") or []
        if not isinstance(articles, list):
            st.warning("記事が取得できませんでした。")
            return
        for idx, article in enumerate(articles[:10], 1):
            title_en = article.get("title", "")
            link = article.get("link", "#")
            try:
                title_ja = translator.translate(title_en, src="en", dest="ja").text
            except:
                title_ja = "(翻訳失敗) " + title_en
            st.markdown(f"**{idx}. {title_ja}**  [原文]({link})")
    except Exception as e:
        st.warning(f"エラーが発生しました: {e}")

media_sources = [
    ("アメリカ", "CNN", "cnn.com", "us", "🇺🇸"),
    ("ドイツ", "Der Spiegel", "spiegel.de", "de", "🇩🇪"),
    ("フランス", "Le Monde", "lemonde.fr", "fr", "🇫🇷"),
    ("中国", "Xinhua", "xinhuanet.com", "cn", "🇨🇳"),
    ("日本", "NHK", "nhk.or.jp", "jp", "🇯🇵"),
]

for name, media, domain, cc, flag in media_sources:
    fetch_and_display_news(name, media, domain, cc, flag)
