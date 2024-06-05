from pathlib import Path

# 最小ファイルサイズ（1MB = 1024 * 1024バイト）
min_file_size = 1024 * 1024


def find_large_files(start_dir):
    start_path = Path(start_dir)

    for file_path in start_path.rglob('*'):
        if file_path.is_file() and file_path.stat().st_size > min_file_size:
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f'大きなファイルを発見🗽: {file_path} (サイズ: {size_mb:.2f} MB)')


if __name__ == '__main__':
    path_to_search = 'folder_path'
    find_large_files(path_to_search)