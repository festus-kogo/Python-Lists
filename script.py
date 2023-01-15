inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
# print(inventory_len)
# Output
# 19
first = inventory[0]
# print(first)
# Output
# twin bed

last = inventory[inventory_len - 1]
# print(last)
# Output
# pillow

# Slice
inventory_2_6 = inventory[2:6]
# print(inventory_2_6)
# Output
# ['headboard', 'queen bed', 'king bed', 'dresser']

first_3 = inventory[0:3]
# print(first_3)
# Output
# ['twin bed', 'twin bed', 'headboard']

twin_beds = inventory.count("twin bed")
# print(twin_beds)
# Output
# 4

removed_item = inventory.pop(4)
# print(removed_item)
# Output
# king bed

inventory.insert(10, "19th Century Bed Frame")
# print(inventory)
# Output
# ['twin bed', 'twin bed', 'headboard', 'queen bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', '19th Century Bed Frame', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory.sort()
print(inventory)
# Output
# ['19th Century Bed Frame', 'dresser', 'dresser', 'headboard', 'king bed', 'king bed', 'nightstand', 'nightstand', 'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table', 'twin bed', 'twin bed', 'twin bed', 'twin bed']
