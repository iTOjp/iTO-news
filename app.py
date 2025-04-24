
import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="iTO News Viewer", layout="wide")

st.title("🌍 世界のニュース比較ビューア")
st.markdown("トップニュースを世界各国のメディアで比較。日本語で要約し、原文にもアクセスできます。")

# 表示対象のニュース（仮で手動定義）
articles = [
    {
        "title": "米大統領、ウクライナへの追加支援を表明",
        "sources": {
            "BBC": "https://www.bbc.com/news/world-123456",
            "CNN": "https://edition.cnn.com/2024/04/20/world/ukraine-aid-us/index.html",
            "NHK": "https://www3.nhk.or.jp/news/html/20240420/k100123456789.html"
        }
    },
    {
        "title": "インドで大規模な選挙が開始",
        "sources": {
            "BBC": "https://www.bbc.com/news/world-asia-india-123456",
            "The Hindu": "https://www.thehindu.com/news/national/india-election-2024/article123456.ece",
            "NHK": "https://www3.nhk.or.jp/news/html/20240419/k100123456788.html"
        }
    }
]

for article in articles:
    st.subheader(article["title"])
    for source, url in article["sources"].items():
        st.markdown(f"- [{source}]({url})")

st.info("※ 本アプリはニュース構造のモック版です。リアルタイム取得や翻訳は次フェーズで拡張可能です。")
