fact = int(input("Enter your integer factorial number :  "))
factorial = 1
for x in range(1,fact+1,1) :
    print(x)
    factorial = factorial * x

print("Total factorial is : ",factorial)