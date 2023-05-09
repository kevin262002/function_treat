def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select Opretoer")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

choice = input("Enter choice (1,2,3,4) : ")

if choice == '1':
    print(add(num1,num2))
    
elif choice =='2':
    print(subtract(num1,num2))

elif choice =='3':
    print(multiply(num1,num2))

elif choice =='4':
    print(divide(num1,num2))

else:
    print("Inpute Not Valide")










    
    
