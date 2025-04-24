
import streamlit as st
import feedparser
from googletrans import Translator

st.set_page_config(page_title="iTO-news (米国ニュース調査版)", layout="wide")

st.title("🇺🇸 アメリカのトップニュース（CNN）")

rss_url = "https://rss.cnn.com/rss/cnn_topstories.rss"
feed = feedparser.parse(rss_url)

# DEBUG: RSSの中身を表示
st.subheader("🔍 DEBUG: RSS取得結果（feed.entries）")
st.write(feed.entries)

translator = Translator()

with st.spinner("ニュースを取得して翻訳中です..."):
    news = []
    for entry in feed.entries[:10]:
        title_en = entry.title
        summary_en = entry.summary if 'summary' in entry else ""
        link = entry.link

        try:
            title_ja = translator.translate(title_en, src='en', dest='ja').text
            summary_ja = translator.translate(summary_en, src='en', dest='ja').text
        except Exception as e:
            title_ja = "(翻訳エラー) " + title_en
            summary_ja = "(翻訳エラー) " + summary_en
            st.error(f"翻訳エラー: {e}")

        news.append({
            "title_ja": title_ja,
            "summary_ja": summary_ja,
            "link": link
        })

for idx, item in enumerate(news, 1):
    st.markdown(f"### {idx}. {item['title_ja']}")
    st.write(item['summary_ja'])
    st.markdown(f"[原文リンクはこちら]({item['link']})")
    st.markdown("---")
