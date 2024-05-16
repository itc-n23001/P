from inventory import display_inventory


def add_to_inventory(inventory_dict, items_list):
    for item in items_list:
        inventory_dict.setdefault(item, 0)
        inventory_dict[item] += 1


if __name__ == '__main__':
    inv = {'金貨': 42, 'ロープ': 1}
    dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
