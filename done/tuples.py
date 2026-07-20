# t1 = (1,2,3,4,5)
# print("Int Tuples ", t1)
# t2 = (1.2,3.4,5.2,9.2)
# print("Float Tuples ", t2)
# t3 = ('a', 'b', 'c', 'd')
# print("String Tuples ", t3)
# t4 = (True, False, True, False)
# print("Boolean Tuples ", t4)
# t5 = ()
# print("Empty Tuple", t5)
# t6 = (26,) #agr single element hai to , lga dena otherwise string le ga
# print(type(t6))
# t7 = (1,2,3,4, (8,'a', 1.2)) #nested tuple
# print(t7)
# t8 = (1,2,3,4, [8,'a', 1.2], (1,2,3), ['a','c']) #tuples also have list
# print(t8)
# t9 = (10,20,30) #imutable hai to error aye  ga values assign nhi kr skte
# t9[0] = 100
# print(t9)
#a list within a tuple is still mutable
# t10 = (1,2,3,4, [8,'a', 1.2], (1,2,3), ['a','c']) #tuple allow duplcate elements
# t10[4][0] = "Hi"
# print(t10)
#access to index in tuple
# t11 = (1,2,3,4, [8,'a', 1.2], (1,2,3), ['a','c'])
# print(t11[0], t11[4][1])
# #negative indexing
# print(t11[-1][0], t11[-2][1])
# print("mytuple.index(2)", t11.index(1)) #will tell index of element in tuple
# #slicing in tuples
# t12 = (1,2,3,4,5,6,7)
# print(t12[0:1])
# food_item1 = ("banana", "mango", "apple")
# food_item2 = ("grapes", "juice", "shake")
# result = food_item1 + food_item2
# print(result * 2)

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 

print(len(genres_tuple))
print(genres_tuple[2])
print(genres_tuple[3:6])
print(genres_tuple[0:2])
print(genres_tuple.index('disco'))
C_tuple = (-5, 1, -3)
print(sorted(C_tuple))

st3 = " ".join(genres_tuple)
print(st3, type(st3))
