# employeeData = {
#     "id": ["1", "2", "3"],
#     "name": ["usama", "mobeen", "zia"],
#     "age": ["29", "39", "49"]
# }
# print("Total Employee Data ", employeeData)

# sameEmployeeData = {
#     "id": ["1", "1", "1"],
#     "name": ["usama", "mobeen", "zia"],
#     "age": ["29", "39", "49"]
# }
# print("Value same Employee Data ", sameEmployeeData)

# # same key results in last wle ko pick kre  ga
# sameEmployeeData2 = {
#     "id": ["1", "1", "1"],
#     "id": ["usama", "mobeen", "zia"]
# }
# print("Key same Employee Data ", sameEmployeeData2)

#access items in dictinary
# employeeData = {
#     "name" : ["Usama", "mobeen"],
#     "age" : "21"
# }
# print(employeeData.get("name"))
# print(employeeData["age"])
# print(employeeData.keys())
# print(employeeData.values())
# print(employeeData.items()) #return tupples in list

#change items in dictionary

# employeeData = {
#     "name" : ["Usama", "mobeen"],
#     "age" : "21"
# }
# employeeData["Color"] = "Red"
# print(employeeData.keys())

# employeeData["name"][0] = "Mateen"
# print(employeeData)

#update in dictionary
# employeeData = {
#     "name" : ["Usama", "mobeen"],
#     "age" : "21"
# }
# employeeData.update({"age": "25"})
# print(employeeData)

#remove items in employeeList

# employeeData = {
#     "name": ["usama", "mobeen", "zia"],
#     "age": [21, 25, 27]
# }
# employeeData.pop("age") #removes item with specific key
# print(employeeData)
# employeeData.popitem() #removes item from last 
# print(employeeData)
# del employeeData["name"] #or del employeeData to remove entire dictionary from memory
# print(employeeData)
# employeeData.clear()

#accessing and creating nested dictionaries 
# myFamily = {
#     "child1" : {
#         "name":"usama",
#         "age": 21
#     } ,
#     "child2": {
#         "name": "mobeen",
#         "age": 25
#     },
#      "child3": {
#         "name": "ahyan",
#         "age": 30
#     },
# }
# print(myFamily["child1"]["name"])

# child1 = {
#         "name":"usama",
#         "age": 21
#     }
# child2 = {
#         "name": "mobeen",
#         "age": 25
#     }
# child3 = {
#         "name": "ahyan",
#         "age": 30
#     },

# myFamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }
# print(myFamily)

#TAskss


# soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# #task1
# a = soundtrack_dic.keys()
# print(a)

# #task2
# b = soundtrack_dic.values()
# print(b)

# #task3 
# # a) Create a dictionary <code>album_sales_dict</code> where the keys are the album name and the sales in millions are the values.

# album_sales_dict = {
#     "album_name": ["Sunday Magzine", "monday magzine", "tuesday magzine"],
#     "sales": ["1,000,230,000", "2,000,230,000", "3,800,270,000"]
# }
# print(album_sales_dict.keys(), album_sales_dict.values(), album_sales_dict["sales"][0])


inventory = {}

product1 = {
"ProductNo1" : "Mobile Phone",
"ProductNo1_quantity" : 5,
"ProductNo1_price" : 20000,
"ProductNo1_releaseYear": 2020
}

product2 = {
"ProductNo2" : "Laptop",
"ProductNo2_quantity" : 10,
"ProductNo2_price" : 50000,
"ProductNo2_releaseYear" : 2023
}
inventory = {
    "Product1" : product1,
    "Product2" : product2
}

print(inventory)
print("ProductNo2_releaseYear" in inventory) #false de ga kiu k in operator dictionary me sirf top keys ko chk kra ha
#top keys filhal product 1 and product 2 hai inventory me
print("ProductNo2_releaseYear" in inventory["Product2"]) #true de ga kiu k product 2 k keys check kre ga sirf

del inventory['Product1']["ProductNo1_releaseYear"]
del inventory["Product2"]["ProductNo2_releaseYear"]

print(inventory)
