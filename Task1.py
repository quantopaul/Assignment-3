def factorial(n):
                if n<2:
                        return 1
                else:
                        return n*factorial(n-1)
n=int(input("Enter a number for its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")

n=int(input("Enter a number for its factorial: "))
fact=1
if(n<2):
                print(f"The factorial of {n} is: {fact}")
else:
                for i in range(2,n+1):
                                fact*=i
                print(f"The factorial of {n} is: {fact}")