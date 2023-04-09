n = int(input("Enter a number to find factor : "))
print("The factors of ",n," is")
for x in range(1,n+1):
      if n%x==0:
      	print(x)
