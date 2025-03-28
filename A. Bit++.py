n = int(input())  # number of statements
x = 0

for _ in range(n):
    s = input().strip()
    if s == "++X" or s == "X++":
        x += 1
    else:
        x -= 1

print(x)
