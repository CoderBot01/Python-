#Triangle pattern
num=int(input("Enter the number" of rows))
for i in range(1,num+1):
	print("  " *(num-i) +" ∆ "* i  )


#right Triangle
num=int(input("Enter the number of rows"))
for i in range(1,num+1):
	print("  " *(num-i) +"∆ "* i  )

#left Triangle
num=int(input("Enter the number of rows"))
for i in range(1,num+1):
	print( "∆ "* i  )


#square
num=int(input("Enter the number of rows"))
for i in range(num):
	for j in range(num):
	    print( "∆ ",end="")
	print()


