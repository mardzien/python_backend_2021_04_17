
print("    ", end="")
for i in range(10):
    print(f"{i:5}", end="")
print()
print()

for x in range(10):
    print(x, end="   ")
    for y in range(10):
        print(f"{x * y:>5}", end="")
    print()
