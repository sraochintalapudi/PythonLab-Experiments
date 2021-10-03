# String creation 
s1='string in single quote'
s2="string in double quote"
s3="""string in triple quote"""
s4='.'
s5='Newsletter'

# Printing string print(s1)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

#string concatenation
s6=s1+s2+s3
print("Concatenated string = ",s6)
print("Fruits are Apple,Orange,Grape,etc",s4*3)
#substring or slicing
print("Substring of ",s5," = ",s5[4:7])
print("Substring of ",s5," = ",s5[:4])
print("Substring of ",s5," = ",s5[4:])
print("Substring of ",s5," = ",s5[::2])
print("Substring of ",s5," = ",s5[-6:-1])
print("Substring of ",s5," = ",s5[-6:])
print("Substring of ",s5," = ",s5[-10:-6])
print("Reverse of ",s5," = ",s5[::-1])
