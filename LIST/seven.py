def neg(n):
    while n <= 0:
        print(n, end=" ")
        n += 1
    print()

def pos(n):
    n -= 1
    while n >= 0:
        print(n, end=" ")
        n -= 1
    print()

def process_number(n):
    if n == 0:
        print("already Zero")
    elif n < 0:
        neg(n)
    else:
        pos(n)

# Example usage:
n = int(input("Enter a number: "))
process_number(n)
