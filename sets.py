# #Sets are unindexed and unordered index se access nhi kr skte
# sets = {1.9,0,3,1.5,2}
# s1 = set([1,2,3,4,5])
# print(sets, type(sets))
# print(s1, type(s1))
# emptySet = {} #dont use this otherwise it  will take as empty dictionary
# print(emptySet, type(emptySet))
# #use set()
# emptySet2 = set()
# print(emptySet2, type(emptySet2))
# #hetrogenous set also set are not in order and is unordered, jab bhi print krwaye ge to order change hota rhe ga
# s2 = {1.2,3, "a", True}
# print(s2, type(s2))
# #sets does not allow duplicate
# s3 = set(["usama", "mobeen", "zia", "usama"])
# print(s3)

# a = {1,2,3}
# b = {2,1,3}
# print(id(a), id(b), a == b, a is b) #is operator means k same object in memory ko point kr rhe

# #cannot assign alues using indexing

# #cannot add list, set in set, (mutable data types nhi rkh skte in set)
# #Nested sets
# # nestedSets = {1,2,3, {1,2,3}}
# # print(nestedSets)

# #Adding elements into set
# s3.add("Ahyan")
# print(s3)
# #adding list into set
# # s3.add(["ahyan", "mobeen"])
# # print(s3)
# #single element add kre ga
# s3.add(("ahyan", "mobeen", "ab"))
# print(s3)
# #mutiple items add krne k liyey update() use krna, list ko bhi add kr de ga update convert kre ga list ko set me 
# #mutable ko add kr de ga set me using update
# s3.update([119,2,3], [4,5,6])
# print(s3)
# #removing random element from set
# s3.pop()
# print(s3)
# #remove specific element from set and does not return anything
# s3.remove("ab") #single element tuple me gaye ho tb remove kr de ga otherwise it will throw error
# print(s3) 
#discard() used to remove element from set if not found than it will not throw error

# s3 = set(["usama", "mobeen", "zia", "usama"])
# s3.discard('Adu')
# print(s3)

# deletes entire set from memory as well
# del s3
# print(s3)
# s3.clear()
# print(s3)
# s5 = {1,2,3,4,5}
# print(max(s5))
# print(min(s5))
# print(sum(s5))
a = {"usama", "mobeen", "zia"}
b = {"haris", "mateen", "zia"}
#used for union
c = a|b 
print("Union ", c) 
#used for intersection
d = a & b
# d = a.intersection(b) same chez
print("Intersection", d)
# difference jo first set ka second set me nhi aye ga wh de ga
e = a - b
print("Difference ",e)
#symmetric difference me jo chez common wh nhi deta aur jo cheze ik dfa pri hai wh de ga
f = a ^ b
print(f)
#subset
lk = {1,2}
mk = {1,2}
g = lk <= mk
print("Subset ", g)
#superset
h = lk >= mk
print("SuperSet ", h)
#isthisjoint used when kisi bi set me kuch common na mile to tb true otherwise false
ja = {1,2,3}
aj = {4,5,6}
i = ja.isdisjoint(aj)
print(i)