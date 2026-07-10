#Sets are unindexed and unordered index se access nhi kr skte
sets = {1.9,0,3,1.5,2}
s1 = set([1,2,3,4,5])
print(sets, type(sets))
print(s1, type(s1))
emptySet = {} #dont use this otherwise it  will take as empty dictionary
print(emptySet, type(emptySet))
#use set()
emptySet2 = set()
print(emptySet2, type(emptySet2))
#hetrogenous set also set are not in order and is unordered, jab bhi print krwaye ge to order change hota rhe ga
s2 = {1.2,3, "a", True}
print(s2, type(s2))
#sets does not allow duplicate
s3 = set(["usama", "mobeen", "zia", "usama"])
print(s3)

a = {1,2,3}
b = {2,1,3}
print(id(a), id(b), a == b, a is b) #is operator means k same object in memory ko point kr rhe

#cannot assign alues using indexing

#cannot add list, set in set, (mutable data types nhi rkh skte in set)
#Nested sets
# nestedSets = {1,2,3, {1,2,3}}
# print(nestedSets)

#Adding elements into set
s3.add("Ahyan")
print(s3)
#adding list into set
# s3.add(["ahyan", "mobeen"])
# print(s3)
#single element add kre ga
s3.add(("ahyan", "mobeen"))
print(s3)
#mutiple items add krne k liyey update() use krna, list ko bhi add kr de ga update convert kre ga list ko set me 
#mutable ko add kr de ga set me using update
s3.update([1,2,3], [4,5,6])
print(s3)