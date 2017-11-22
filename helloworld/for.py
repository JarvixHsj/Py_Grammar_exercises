for i in range(1,5):
    if i == 2:
        continue
    if i == 3 :
        print('提前 over')
        break
        print('break 后的print')
    print(i)

else:
    print('The for loop is over')
