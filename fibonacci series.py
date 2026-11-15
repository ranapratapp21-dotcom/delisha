
# Fibonacci Sequence Using Recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Get the number of terms
n = int(input("Enter the number of terms: "))

# Print Fibonacci sequence
print("Fibonacci Sequence:")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nProgram completed successfully!")
