#Task-1 Create an empty list
emptyList = []
print(emptyList)

#Task-2 Now store the number of items to the shopping_list
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
print(shopping_list)

#Task-3 Add a new item to the shopping_list
shopping_list.append('Football')
print("Appended list ", shopping_list)

#Task-4 Print First item from the shopping_list
print("First item in shopping list is ", shopping_list[0])

#Task-5 Print Last item from the shopping_list
lengthShoppingList = len(shopping_list)
print("Last item in shopping list is ", shopping_list[lengthShoppingList - 1])

#Task-6 Print the entire Shopping List
print("Entire Shopping List ", shopping_list)

#Task-7 Print the item that are important to buy from the Shopping List
print("Important Items from Shopping List are ", shopping_list[1:3])

# Task-8 Change the item from the shopping_list, Instead of <u>"Pen"</u> I want to buy <u>"Notebook"</u>

shopping_list.remove("Pen")
shopping_list.insert(3, "Notebook")
print("Updated List with Notebook ", shopping_list)

# Task-9 Delete the item from the shopping_list that is not required
# Let's delete items that are unimportant, such as; I don't want to buy <u>Clothes</u>, let's delete it.

shopping_list.remove("Clothes")
print("Updated list without item that's not required", shopping_list)

#Task-10

print("Updated Shopping List with all applied methods ", shopping_list)
