
import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="iTO-news GNews仮版", layout="wide")

st.title("🇺🇸 CNNの最新ニュース（GNews仮API）")

translator = Translator()

url = "https://gnews.io/api/v4/search"
params = {
    "q": "site:cnn.com",
    "lang": "en",
    "max": 10,
    "token": "demo"
}

response = requests.get(url, params=params)
data = response.json()

if "articles" in data:
    for idx, article in enumerate(data["articles"], 1):
        title_en = article.get("title", "")
        desc_en = article.get("description", "")
        link = article.get("url", "#")

        try:
            title_ja = translator.translate(title_en, src='en', dest='ja').text
        except:
            title_ja = "(翻訳エラー) " + title_en

        try:
            desc_ja = translator.translate(desc_en, src='en', dest='ja').text
        except:
            desc_ja = "(翻訳エラー) " + desc_en

        st.markdown("### {}. {}".format(idx, title_ja))
        st.write(desc_ja)
        st.markdown("[原文リンクはこちら]({})".format(link))
        st.markdown("---")
else:
    st.warning("ニュースデータが取得できませんでした。APIキーまたは通信環境をご確認ください。")
