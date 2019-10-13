col_string=int(input('Сколько элементов пожелаете?: '))
str_values=[]
for string in range(col_string):
  str_values.append(int(input(f'Введите {string+1} элемент: ')))
str_values.sort()
print('Отсортировали, взгляните : {}'.format(str_values), "все ли так?")