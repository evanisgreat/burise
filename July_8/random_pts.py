import random

def get_points():
    x = random.randrange(-1,1)
    y = random.randrange(-1, 1)
    return x, y


total = 10000

success = 0

for _ in range(total):
    x, y = get_points()

    if x ** 2 + y **2 <= 1:
        success += 1

print(4 * success / total)