for x in range(2,10):
    for y in range(2,x):
        if x % y ==0:
            print(x,' equals ',y,' * ',x//y,' ,so this is not a prime number')
            break
        else:
            print(x," ,this is a prime number")
