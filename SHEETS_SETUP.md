# Google Sheets連携の設定方法

## 1. Google Cloud Platformでサービスアカウント作成

1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 新しいプロジェクトを作成
3. 「APIとサービス」→「認証情報」
4. 「認証情報を作成」→「サービスアカウント」
5. サービスアカウント名を入力して作成
6. 作成したサービスアカウントをクリック
7. 「キー」タブ→「鍵を追加」→「新しい鍵を作成」→「JSON」
8. JSONファイルがダウンロードされます

## 2. Google Sheets APIを有効化

1. 「APIとサービス」→「ライブラリ」
2. "Google Sheets API"を検索して有効化
3. "Google Drive API"も検索して有効化

## 3. Streamlit Secretsに設定

1. Streamlit Community Cloudのアプリ設定画面を開く
2. 「Settings」→「Secrets」
3. 以下の形式で追加:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

(ダウンロードしたJSONファイルの内容をコピー)

## 4. アプリで有効化

`app.py`の以下の行を変更:
```python
ENABLE_GOOGLE_SHEETS = True  # FalseからTrueに変更
```

## 5. スプレッドシートの共有

作成されたスプレッドシートは自動的に読み取り専用で共有されます。
サービスアカウントのメールアドレスに編集権限が必要です。
