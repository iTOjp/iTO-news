
import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="世界ニュース翻訳ビューア", layout="wide")
st.title("🌍 世界5カ国の代表メディア トップ10（翻訳つき）")

translator = Translator()

def fetch_and_display_news(name, media, domain, country_code, flag):
    st.subheader(f"{flag} {name}のトップニュース（{media}）")
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": "pub_1234567890abcdef",
        "domain": domain,
        "language": "en",
        "country": country_code
    }
    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        articles = data.get("results", [])
        if not articles:
            st.info("記事が取得できませんでした。")
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

fetch_and_display_news("アメリカ", "CNN", "cnn.com", "us", "🇺🇸")
fetch_and_display_news("ドイツ", "Der Spiegel", "spiegel.de", "de", "🇩🇪")
fetch_and_display_news("フランス", "Le Monde", "lemonde.fr", "fr", "🇫🇷")
fetch_and_display_news("中国", "Xinhua", "xinhuanet.com", "cn", "🇨🇳")
fetch_and_display_news("日本", "NHK", "nhk.or.jp", "jp", "🇯🇵")
