song = input().split()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
list_1 = list()
for item in song:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    list_1.append(k)
if len(set(list_1)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
