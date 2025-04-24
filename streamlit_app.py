
import streamlit as st
import requests

st.set_page_config(page_title="世界3か国の代表メディア トップ10", layout="wide")

st.title("🌍 世界3か国の代表メディア トップ10（翻訳つき）")
st.caption("🔖 version 0.9 / build: 2025-04-25 03:00:00 JST")

API_KEY = "pub_828414f2650027ef032005a0dc43452796878"
BASE_URL = "https://newsdata.io/api/1/news"

news_sources = {
    "US CNN（US）": {"country": "us", "language": "en"},
    "DE Der Spiegel（DE）": {"country": "de", "language": "de"},
    "FR Le Monde（FR）": {"country": "fr", "language": "fr"},
}

for name, params in news_sources.items():
    st.subheader(name)
    with st.status("ニュースを取得しています...", expanded=False):
        try:
            url = f"{BASE_URL}?apikey={API_KEY}&country={params['country']}&language={params['language']}&page=1"
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()

            if "results" in data and data["results"]:
                for idx, article in enumerate(data["results"][:10], 1):
                    title = article.get("title", "No title")
                    link = article.get("link", "#")
                    st.markdown(f"{idx}. {title} [原文]({link})")
            else:
                st.warning("記事が取得できませんでした。")

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
