s1=int(input("Side 1 of the triangle ")) 
s2=int(input("Side 2 of the triangle "))
s3=int(input("Side 3 of the triangle "))
big = max(s1,s2,s3)
if(big==s1): 
    if(s1**2 == (s2**2 + s3**2)):
        print("The triangle sides given is a right angled triangle", s1**2, (s2**2+s3**2))
    else:
        print("The triangle sides given is not right angled triangle",s1**2, (s2**2+s3**2))
elif(big==s2):
      if(s2**2==(s1**2+s3**2)):
          print("The triangle sides given is a right angled triangle",s2**2,(s1**2+s3**2))
      else:
        print("The triangle sides given is not right angled triangle", s2**2,(s1**2+s3**2))
elif(big==s3):
      if(s3**2==(s1**2+s2**2)):
        print("The triangle sides given is a right angled triangle",s3**2,(s1**2+s2**2))
      else:
        print("The triangle sides given is not right angled triangle", s3**2, (s1**2+s2**2))
