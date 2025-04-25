
import streamlit as st
import requests

# ✅ ページ設定（必ず最初に）
st.set_page_config(page_title="愛輝！世界の代表メディア 最新ニュース", layout="wide")

# 🌟 アプリ本体
st.title("🌏 愛輝！世界の代表メディア 最新ニュース")
st.markdown("翻訳付きで各国メディアのトップ記事をチェックできます。")

# 翻訳関数（DeepL → Googleに自動切替）
DEEPL_API_KEY = "5471786a-d12e-4f9d-978f-a7ed048b9452:fx"
DEEPL_USAGE_URL = "https://api-free.deepl.com/v2/usage"

def check_deepl_quota():
    try:
        response = requests.get(DEEPL_USAGE_URL, headers={"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"})
        data = response.json()
        return data.get("character_count", 0), data.get("character_limit", 500000)
    except:
        return 500000, 500000  # エラー時は上限扱いでGoogle使用

def translate_text(text, target_lang="JA"):
    char_used, char_limit = check_deepl_quota()
    if char_used < char_limit - 10000:
        # DeepL使用
        try:
            result = requests.post(
                "https://api-free.deepl.com/v2/translate",
                data={"auth_key": DEEPL_API_KEY, "text": text, "target_lang": target_lang}
            )
            return result.json()["translations"][0]["text"]
        except:
            pass  # DeepL失敗時にGoogleへ
    # Google翻訳へフォールバック
    try:
        result = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={"client": "gtx", "sl": "en", "tl": "ja", "dt": "t", "q": text}
        )
        return result.json()[0][0][0] + "＊"
    except:
        return "(翻訳失敗)"

# ニュースデータ（元の英語）
news_data = {
    "🇺🇸 CNN（米）": [
        "President Biden strengthens environmental policy",
        "U.S. economy grows faster than expected",
        "New immigration policy under discussion",
    ],
    "🇯🇵 NHKニュース（日本）": [
        "New school year begins, entrance ceremonies held",
        "Government continues investigation on earthquake damage",
        "Food prices rise due to yen depreciation",
    ],
    "🇬🇧 BBC News（英）": [
        "UK parliament debates election reform",
        "New tourism campaign launched in London",
        "New budget proposed for climate action",
    ],
}

# 表示部分（翻訳＋カード形式）
for media, articles in news_data.items():
    st.subheader(media)
    for original in articles:
        translated = translate_text(original)
        with st.container():
            st.markdown(
                f'''
<div style="border-radius: 16px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); padding: 1rem; margin-bottom: 1rem; background-color: #f9f9f9;">
    <strong>{translated}</strong><br>
    <span style="font-size: 0.85rem; color: #555;">{original}</span>
</div>
''',
                unsafe_allow_html=True
            )
