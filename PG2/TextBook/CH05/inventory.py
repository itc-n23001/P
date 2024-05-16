def display_inventory(inventory_dict):
    count = 0
    print('持ち物リスト')
    for k, v in inventory_dict.items():
        count += v
        print(v, k)
    print('アイテム総数：', count)


if __name__ == '__main__':
    inventory = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
    display_inventory(inventory)