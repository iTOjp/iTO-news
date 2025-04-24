
import streamlit as st
import requests
from datetime import datetime

# --- 設定 ---
API_KEY = "8091deb44d58406f4b38ea5b1b23fac4"
COUNTRIES = {
    "US": {"name": "アメリカ", "media": "CNN", "lang": "en"},
    "DE": {"name": "ドイツ", "media": "Der Spiegel", "lang": "de"},
    "FR": {"name": "フランス", "media": "Le Monde", "lang": "fr"},
}

# --- ヘッダー ---
st.set_page_config(page_title="世界ニュース比較ビューア", layout="wide")
st.title("🌍 世界3か国の代表メディア トップ10（翻訳つき）")

# --- バージョン表示 ---
version = "0.4-mini"
build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.caption(f"📄 ビルド: version {version} / {build_time} JST")

# --- ニュース取得関数 ---
def fetch_news(country_code):
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "lang": "en",
        "country": country_code.lower(),
        "max": 10,
        "token": API_KEY,
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("articles", [])
    except Exception as e:
        return f"エラー: {e}"

# --- 表示処理 ---
for code, info in COUNTRIES.items():
    st.subheader(f"{code} {info['name']}のトップニュース（{info['media']}）")
    with st.spinner("取得中..."):
        articles = fetch_news(code)
        if isinstance(articles, str):
            st.warning(f"{articles}")
        elif articles:
            for i, article in enumerate(articles):
                st.markdown(f"{i+1}. [{article['title']}]({article['url']})")
        else:
            st.info("記事が取得できませんでした。")
