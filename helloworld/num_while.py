total = 72
running = True
res = 0

while running:
    if total > 0:
        res += total
        total = total - 3
    else:
        running = False

else:
    print(res)
    print('Done')

