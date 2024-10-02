def efc(a,b):
   d=1
   for i in range(1,max(a,b)+1):
        if a%i==0 and b%i==0:
            d=i
        s = y
        y = x - (a / b) * y
        x = s
      
a=int(input())
b=int(input())
print(efc(a,b))