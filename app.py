import streamlit as st
import pandas as pd
import os

# --- 設定 ---
# 投票対象の10個の案
CANDIDATES = [
    "アプリ案1:【アニメ聖地巡礼】",
    "案2:【爆買いアプリ】",
    "案3: 「最強ポートフォリオ」プロデュース",
    "案4: 「超絶プレミアム文化体験」",
    "案5: 【JLPT対策アプリ】",
    "案6: 「Yuka」",
    "案7: Niche Dating Apps（ニッチデートアプリ）",
    "案8: 旅先の移動の無駄な調査、苦労を下げるMaaS",
    "案9: タンプラリー型旅行サクサクアプリ",
    "案10: その他"
]

# データ保存用ファイル
DATA_FILE = "votes.csv"
# 管理者用パスワード（結果を見るための鍵）
ADMIN_PASSWORD = "secret_open"

# --- 関数: データの読み書き ---
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["candidate", "voter_ip"])

def save_vote(candidate):
    df = load_data()
    # 簡易的な重複防止（必要なければ削除可）
    # 今回はシンプルに「追記」のみ行います
    new_data = pd.DataFrame({"candidate": [candidate]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# --- UI構築 ---
st.title("🗳️ アイデア投票アプリ")
st.markdown("以下の10個の案から、最も良いと思うものに投票してください。")

# 1. 投票セクション
st.header("投票する")
selected_option = st.radio("どの案に投票しますか？", CANDIDATES)

if st.button("投票を送信"):
    save_vote(selected_option)
    st.success(f"「{selected_option}」に投票しました！ありがとうございます。")

st.markdown("---")

# 2. 結果開示セクション（パスワード保護）
st.header("集計結果（管理者のみ）")
st.markdown("結果は開示されるまで伏せられています。")

input_pass = st.text_input("開示パスワードを入力してください", type="password")

if input_pass == ADMIN_PASSWORD:
    st.success("認証成功：結果を表示します")
    
    df = load_data()
    if not df.empty:
        # 集計
        vote_counts = df["candidate"].value_counts()
        
        # グラフ表示
        st.bar_chart(vote_counts)
        
        # 表で詳細表示
        st.write("詳細データ:")
        st.dataframe(vote_counts)
        st.metric("総投票数", len(df))
    else:
        st.info("まだ投票はありません。")
elif input_pass:
    st.error("パスワードが違います。")
else:
    st.info("🔒 結果は非表示です")