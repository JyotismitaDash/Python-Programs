n = int(input("enter n values"))

for i in range(1, n + 1):
    for row in range(n - i):
        print("  ", end="")
    for col in range(i):
        print("* ", end="")
    print()