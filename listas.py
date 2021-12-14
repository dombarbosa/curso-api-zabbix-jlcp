lista_one = [1, 21, 3, 7, 23, 1, 10, 15, 2, 2, 2, 3, 4, 8, 2, 1, 3, 1, 3]

#Muito importante
i = 1
while True:
    if i < 4:
        print('Quantos números {} tem nessa lista: {}'.format(i, lista_one.count(i)))
        i = i + 1
    else:
        break
