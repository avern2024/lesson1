my_dict = {'Andrei': 1969, 'Sveta': 1970, 'Artem': 1991}
print(my_dict)
print(my_dict['Sveta'])
print(my_dict.get('Dasha'))
my_dict.update({'Sahsa': 2000, 'Alisa': 2002})
print(my_dict.pop('Sahsa'))
print(my_dict)
print()
my_set = {22, 'Python', False, (1, 2), (1, 2), False, 22}
print(my_set)
my_set.update([77, '22'])
my_set.discard(22)
print(my_set)