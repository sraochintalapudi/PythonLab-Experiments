class py_solution: 
   def pow(self, x, n):
      if x==0 or x==1 or n==1:
         return x
      if x==-1:
         if n%2 ==0:
            return 1
         else:
            return -1
      if n==0:
         return 1
      if n<0:
         return 1/self.pow(x,-n)
      val = self.pow(x,n//2)
      if n%2 ==0:
          return val*val
      return val*val*x

while True:
    print("Enter q or Q to quit ")
    x=input("Enter x value: ")
    if (x=='q' or x=='Q'):
        break
    else:
      n=input("Enter n value: ")
      n=int(n)
      x=int(x)
      p=py_solution()
      q=p.pow(x,n)
    print(x," to the power ",n," is = ",q)
    print()
    continue
