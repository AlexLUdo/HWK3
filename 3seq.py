pervyj_nabor=set(input('Введите элементы первого множества через запятую: ').split(','))
vtoroj_nabor=set(input('Введите элементы второго множества через запятую: ').split(','))
print('Первое множество за вычетом второго: ', pervyj_nabor.difference(vtoroj_nabor))