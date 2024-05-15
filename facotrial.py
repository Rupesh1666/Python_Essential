fact = int(input("Enter a number to check factorial:"))
factorial =1
for i in range (1, fact+1):
    factorial *=i
print("the factorial of", fact, "=", factorial)