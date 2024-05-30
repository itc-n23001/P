import re
from pathlib import Path

import pyinputplus as pyip


def search_files_for_pattern(directory_path, pattern):
    for filename in Path(directory_path).iterdir():
        file_path = str(filename)

        with open(file_path, encoding='utf-8') as file:
            for line in file:
                if re.search(pattern, line):
                    print(f'{filename.name}: - {line}')


def main():
    dir_path = 'folder_path'
    re_str = pyip.inputStr('正規表現を入力してください: ')
    search_files_for_pattern(dir_path, re_str)


if __name__ == '__main__':
    main()
