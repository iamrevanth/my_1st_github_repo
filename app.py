# Example of an looped if condition
print("PROG 1: This is Looped IF statement")
x = 5

if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("x is greater than 10")
    else:
        print("x is not greater than 10")
elif x < 5:
    print("x is less than 5")
    if x > 2:
        print("x is greater than 2")
    else:
        print("x is not greater than 2")
elif x == 5:
    print("x is equal to 5")

# print options
print("PROG 2: This is PRINT statement")
print("X is : " f"{ x }" " and is of type : " f"{ type(x) }")
print("X is :", x, "and is of type : " f"{ type(x) }")
# Example of a looped if condition with a message

print("PROG 3: This is MESSAGE statement")

message = "X is greater than 5 and less than 20" if x > 5 and x < 20 else "X bigger than 20" if x > 20 else "X is less than or equal to 5"
print(message)


print("PROG : FOR Loop")
for i in range(1,5,2):
    print("Attempt ", i, " of 10", i*".")
    