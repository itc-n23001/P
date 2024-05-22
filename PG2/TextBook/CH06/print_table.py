def print_table(table_data):
    # 最大の文字列長を計算
    max_length = 0
    for table in table_data:
        for item in table:
            max_length = max(max_length, len(item))

    # テーブルを右揃えして出力
    for table in table_data:
        for item in table:
            print(item.rjust(max_length), end=' ')
        print()  # 改行


# テーブルデータ
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# テーブルを右揃えして出力
print_table(table_data)
