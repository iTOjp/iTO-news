import streamlit as st

st.set_page_config(page_title="世界3か国の代表メディアトップ10", layout="wide")
st.title("🌍 世界3か国の代表メディアトップ10（翻訳なし）")
st.caption("version 0.9.3 / build: 2025-04-25 03:00:00 JST")

# 表示用の国とメディア
media_sources = {
    "アメリカ（CNN）": "https://newsdata.io/api/1/news?apikey=pub_828414f2650027ef032005a0dc43452796878&country=us&language=en&page=1",
    "ドイツ（Der Spiegel）": "https://newsdata.io/api/1/news?apikey=pub_828414f2650027ef032005a0dc43452796878&country=de&language=en&page=1",
    "フランス（Le Monde）": "https://newsdata.io/api/1/news?apikey=pub_828414f2650027ef032005a0dc43452796878&country=fr&language=en&page=1",
}

import requests

for media, url in media_sources.items():
    st.subheader(media)
    with st.container():
        with st.spinner("ニュースを取得しています…"):
            try:
                res = requests.get(url)
                data = res.json()
                if res.status_code != 200:
                    raise Exception(f"エラーが発生しました: {res.status_code} {data.get('message', '')}")
                for i, article in enumerate(data["results"][:10], 1):
                    st.markdown(f"{i}. [{article['title']}]({article['link']})")
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
