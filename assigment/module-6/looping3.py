List1 = ['apple', 'banana', 'mango']
search_item = 'banana'

for fruit in List1:
    if fruit == search_item:
        print(search_item, "is found in the list")
        break
else:
    print(search_item, "is not found in the list")
