tup1 = ('jan','feb','mar','apr','may','june','july','august','september','october','november','december')
tup2 = (1, 2, 3, 4, 5)
tup3=(1, "Hello", (11, 22, 33))
tup4=('India',[10,20,30],'USA')
#print the tuple
print(tup1)

#iterating in tuple 
for mon in tup1:
    print(mon)

#accessing the tuple element
print("The element in the 5th position : ",tup1[5])
print(tup1[-6])
print("Tuple before addition")
print(tup2)
tup2 = tup2 + (7,) 
print("Tuple after addition")
print(tup2)
tup2=tup2+('apple','orange','banana')
print(tup2)

#accessing nested tuple element 
print(tup3[2][1])

#tuple element is mutable, element change is possible 
print("Tuple before change")
print(tup4)
tup4[1][2]=40
print("Tuple after change")
print(tup4)

#Slicing operation in tuples
print(tup1[2:5])
print(tup1[4:])
print(tup1[:4])

#finding position of the element
print("The position of 'october' in the tuple: ",tup1.index('october'))
