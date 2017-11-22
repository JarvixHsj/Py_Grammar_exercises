def total(a = 5, *num, **phone):
    print('a', a)

    for single_item in num:
        print('single_item',single_item)

    for first_part, second_part in phone.items():
        print(first_part, second_part)

print(total(10,1,2,jack= 1123, john = 2231, inge = 1560))
