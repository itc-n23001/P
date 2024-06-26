import ezsheets

# Googleスプレッドシートにアクセス
spreadsheet = ezsheets.Spreadsheet('pg2_program')

# シート1を選択 (必要に応じてシート名やインデックスを変更)
sheet = spreadsheet[0]

# 名前とメールアドレスのリストを作成
names_and_emails = []

# データを取得 (1行目はヘッダー行としてスキップ)
for row in sheet.getRows()[1:]:
    name = row[0]  # 名前の列 (必要に応じてインデックスを変更)
    email = row[1]  # メールアドレスの列 (必要に応じてインデックスを変更)
    names_and_emails.append((name, email))

# 結果を表示
for name, email in names_and_emails:
    print(f"Name: {name}, Email: {email}")
