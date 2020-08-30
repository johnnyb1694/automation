def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def augment_inventory(inventory, items_to_add):
    for item in items_to_add:
        # Following line searches the inventory for a given item; if none is found, 0 is returned for assignment in the next phase
        key_count = inventory.get(item, 0)
        inventory[item] = key_count + 1

    return(inventory)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print('Before...')
display_inventory(inv)
inv = augment_inventory(inv, loot)
print('After...')
display_inventory(inv)
