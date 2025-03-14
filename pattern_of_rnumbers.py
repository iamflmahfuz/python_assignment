n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%3==0 and j%5==0:
            print("FizzBuzz",end=" ")
        elif j%3==0:
            print("Fizz",end=" ")
        elif j%5==0:
            print("Buzz",end=" ")
        else:
            print(j,end=" ")
    print()                    