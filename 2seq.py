inp_str=input('Введите цифры через запятую (, или ;  или / ) : ')
if ',' in inp_str: str_sep = ','
if ';' in inp_str: str_sep = ';'
if '/' in inp_str: str_sep = '/'
inp_val=inp_str.split(str_sep)
inp_val=[int(i) for i in inp_val]
print(set(inp_val))