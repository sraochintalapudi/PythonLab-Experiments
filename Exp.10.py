# This is the example of print simple pyramid pattern  
n = int(input("Enter the number of rows"))  
# outer loop to handle number of rows  
for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       

            # ending line after each row  
        print()
for i in range(n, 1, -1):
    for j in range(1,i):
        print("* ",end="")
    print()
