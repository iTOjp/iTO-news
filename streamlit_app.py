import streamlit as st
from streamlit.components.v1 import html

# 💫 ラメエフェクト
html("""
<div id="glitter-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999;"></div>

<script>
const container = document.getElementById("glitter-container");

window.addEventListener("scroll", () => {
  for (let i = 0; i < 4; i++) {
    const sparkle = document.createElement("div");
    sparkle.style.position = "absolute";
    sparkle.style.width = "6px";
    sparkle.style.height = "6px";
    sparkle.style.borderRadius = "50%";
    sparkle.style.background = "linear-gradient(45deg, #fff, #ffc0cb, #add8e6)";
    sparkle.style.top = `${window.scrollY + Math.random() * window.innerHeight}px`;
    sparkle.style.left = `${Math.random() * window.innerWidth}px`;
    sparkle.style.opacity = "0.8";
    sparkle.style.boxShadow = "0 0 8px white";
    sparkle.style.animation = "fadeout 2s ease-out forwards";
    container.appendChild(sparkle);
    setTimeout(() => {
      sparkle.remove();
    }, 2000);
  }
});

const style = document.createElement("style");
style.textContent = `
@keyframes fadeout {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(0.5); opacity: 0; }
}`;
document.head.appendChild(style);
</script>
""", height=0)

# 🌟 アプリ本体
st.set_page_config(page_title="愛輝！世界の代表メディア 最新ニュース", layout="wide")

st.title("🌏 愛輝！世界の代表メディア 最新ニュース")
st.markdown("翻訳付きで各国メディアのトップ記事をチェックできます。")

# ニュースダミーデータ（翻訳付き）
news_data = {
    "🇺🇸 CNN（米）": [
        {"title_ja": "バイデン大統領、環境政策を強化", "title_en": "President Biden strengthens environmental policy"},
        {"title_ja": "アメリカ経済、予想を上回る成長", "title_en": "U.S. economy grows faster than expected"},
    ],
    "🇯🇵 NHKニュース（日本）": [
        {"title_ja": "新学期始まる、小中学校で入学式", "title_en": "New school year begins, entrance ceremonies held"},
        {"title_ja": "地震の被害状況、政府が調査継続", "title_en": "Government continues investigation on earthquake damage"},
    ],
    "🇬🇧 BBC News（英）": [
        {"title_ja": "イギリス議会、選挙法改革を審議", "title_en": "UK parliament debates election reform"},
        {"title_ja": "ロンドンで新たな観光キャンペーン", "title_en": "New tourism campaign launched in London"},
    ],
}

# 表示部分
for media, articles in news_data.items():
    st.subheader(media)
    for article in articles:
        with st.container():
            st.markdown(
                f'''
<div style="border-radius: 16px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); padding: 1rem; margin-bottom: 1rem; background-color: #fffafc;">
    <strong>{article["title_ja"]}</strong><br>
    <span style="font-size: 0.85rem; color: #666;">{article["title_en"]}</span>
</div>
''',
                unsafe_allow_html=True
            )
