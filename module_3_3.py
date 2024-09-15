def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3, 'hello')
print_params(4, 'bye', False)

print_params(b=25)
print_params(c=[1,2,3])

values_list = ["hello, world", 999, (True, False)]
values_dict = {
    'a': 'Blabla',
    'b': 1234,
    'c': [4, 4, 3, 'eeee']
}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ["qwerty", 998]
print_params(*values_list2, 42)










