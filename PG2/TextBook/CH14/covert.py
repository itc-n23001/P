import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 認証とAPIクライアントの設定
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

def authenticate():
    creds = None
    # トークンの読み込み
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # 認証が必要な場合
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # トークンの保存
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def upload_sheet(file_path, sheet_name):
    creds = authenticate()
    drive_service = build('drive', 'v3', credentials=creds)

    # ファイルメタデータの設定
    file_metadata = {'name': sheet_name, 'mimeType': 'application/vnd.google-apps.spreadsheet'}
    media = MediaFileUpload(file_path, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Google Driveにファイルをアップロード
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = file.get('id')
    
    # Google Sheets APIを使用してシート名を変更
    sheets_service = build('sheets', 'v4', credentials=creds)
    request_body = {
        "requests": [
            {
                "updateSpreadsheetProperties": {
                    "properties": {
                        "title": sheet_name
                    },
                    "fields": "title"
                }
            }
        ]
    }
    sheets_service.spreadsheets().batchUpdate(spreadsheetId=file_id, body=request_body).execute()
    return file_id

def main():
    # アップロードするファイルのパス
    file_path = 'path_to_your_spreadsheet.xlsx'
    
    # Google Sheetsのシート名
    sheet_name = 'pg2_program'
    
    # ファイルをGoogle Sheetsにアップロード
    file_id = upload_sheet(file_path, sheet_name)
    print(f'File uploaded with ID: {file_id}')

if __name__ == '__main__':
    main()

