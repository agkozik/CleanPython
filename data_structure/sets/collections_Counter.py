# тип «мультимножество» (или «мешок»)
from collections import Counter

inventory = Counter()

loot = {'knife': 1, 'bread': 3}
inventory.update(loot)

print(inventory) # Counter({'bread': 3, 'knife': 1})

more_loot = {'knife': 1, 'apple': 4}
inventory.update(more_loot)
print(inventory)

print(len(inventory))  # Количество уникальных элементов
print(sum(inventory.values()))  # Общее количество элементов