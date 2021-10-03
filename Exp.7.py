mon={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'june'}
stud={'kiran':23,'kumar':20,'dinesh':19,'rakesh':21}

print("mon Dictionary is ",mon)
print("The element in the key position 3 is :",mon[3])
print("The mon dictionary values are: ",mon.values())
print("The mon dictionary keys are: ",mon.keys())

#adding an item in the dictionary 
print("Before addition")
for item in mon.values():
    print(item,end=' ')

mon[7]='july' 
print()
print("After addition")
for item in mon.values():
    print(item,end=' ')
    print()
print("Before deletion")
for item in stud.values():
    print(item,end=' ')
    print()
    
del stud['kumar']

print("After deletion")
for item in stud.values():
    print(item,end=' ')
    print()

print("Before change")
print("stud Dictionary is ",stud)
stud['dinesh']=55
print("After change")
print("stud Dictionary is ",stud)

print("Key value pair of dictionary")
print(stud.items())
