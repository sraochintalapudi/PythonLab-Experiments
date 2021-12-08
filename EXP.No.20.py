class py_solution:
    def reverse_words(self, s):
        lst = s.split(" ")
        lst = lst[::-1]
        st=""
        for w in lst:
            st = st + " " + w
        return st

s=input("Enter a string: ")
rs=py_solution()
r = rs.reverse_words(s) 
print("The reversed sentence: ",r)

