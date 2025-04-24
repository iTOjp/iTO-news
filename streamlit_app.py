
import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="iTO-news Newsdata仮版", layout="wide")
st.title("🇺🇸 CNNのトップニュース（Newsdata仮API）")

translator = Translator()

url = "https://newsdata.io/api/1/news"
params = {
    "apikey": "pub_1234567890abcdef",
    "domain": "cnn.com",
    "language": "en",
    "country": "us"
}

response = requests.get(url, params=params)
data = response.json()

if "results" in data:
    for idx, article in enumerate(data["results"][:10], 1):
        title_en = article.get("title", "")
        desc_en = article.get("description", "")
        link = article.get("link", "#")

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
