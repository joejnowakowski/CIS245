

x = 5
n = 0
while x > 0:
    print(f"loop {n + 1}")
    x -= 1
    n += 1
    if x == 4:
        break
else:
    print("full while")

for n in range(5):
    print(f"n is {n}")
    # if n == 4:
    #     break
else:
    print("else statement")

print("statement\n"*5)