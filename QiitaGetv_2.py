# ライブラリのインポート
import json
import requests
import pandas as pd
import time
import datetime

def makeResult():
    # ファイル名のフォーマット準備 GetLog_年月日.csv
    now = datetime.datetime.now()
    path = 'getlog_' + now.strftime('%Y%m%d%H%M') + '.csv'

    # CSVからURLを読み込み
    data = pd.read_csv('url.csv',encoding="utf-8")
    urls = data['url']

    # リクエストヘッダ
    params = {'page': '1', 'per_page': '10', 'query':'tag:Python'}

    # ユーザーエージェントの設定
    # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    # headers = {'User-Agent': ua}

# CSVに書かれたURL分、ゲット
    for url in urls:
        time.sleep(180)
        # 一旦、JSONとして取得
        new_articles = requests.get(url, params=params,).json()
        # 辞書リストをデータフレーム型に変換。
        df = pd.io.json.json_normalize(new_articles)
        # 列の抽出＋並び替え、リネーム
        df = df[['user.id', 'created_at', 'title', 'url']]
        df.columns = ["ユーザーID", "作成日時", "タイトル", "リンク"]
        #CSVに書き込み、任意のファイル名で保存
        df.to_csv(path)

if __name__ == '__main__':
    makeResult()
