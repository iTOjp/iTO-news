
import streamlit as st
import requests

st.set_page_config(page_title="iTO-news Newsdata動作確認版", layout="wide")
st.title("🇺🇸 CNNのトップニュース（翻訳なし・英語表示）")

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
        title = article.get("title", "")
        desc = article.get("description", "")
        link = article.get("link", "#")

        st.markdown("### {}. {}".format(idx, title))
        st.write(desc)
        st.markdown("[Original article]({})".format(link))
        st.markdown("---")
else:
    st.warning("ニュースデータが取得できませんでした。APIキーまたは通信環境をご確認ください。")
