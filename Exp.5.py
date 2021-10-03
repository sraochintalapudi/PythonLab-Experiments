lst = []
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=int(input("Enter number to append: "))
        lst.append(n)
        print("List: ",lst)
    elif choice==2:
        if len(lst)==0:
           print("List is empty, no item to remove:")
           print()
           continue
        n=int(input("Enter number to remove: "))
        if n not in lst:
            print("The item to be removed not in list:")
            print()
            continue
        lst.remove(n)
        print("List: ",lst)
    elif choice==3:
        print("List: ",lst)
    elif choice==0: 
        print("Exiting!")
    else:
        print("Invalid choice!!") 
        print()
