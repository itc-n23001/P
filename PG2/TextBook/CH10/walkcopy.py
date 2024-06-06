import os
import shutil

source_directory = "test"  # 探索する元のディレクトリ
destination_directory = "destination"  # コピー先のディレクトリ

# コピー先のディレクトリが存在しない場合、作成する
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# ファイルを探索してコピーする
for a, b, c in os.walk(source_directory):
    for f in c:
        if f.endswith((".jpg", ".pdf")):
            source_file = os.path.join(a, f)
            destination_file = os.path.join(destination_directory, f)
            shutil.copy2(source_file, destination_file)  # ファイルをコピー
            print(f"Copied {source_file} to {destination_file}")
