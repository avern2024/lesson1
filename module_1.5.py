immutable_var = (1, False, 'Python', [6,4])
print(immutable_var)
# Невозможно напрямую изменить элементы кортежа, например  - immutable_var[0]  = 23 выдаст ошибку "'tuple' object does not support item assignment" потому, что кортеж является неизменяемым типом данных.
# Можно изменить элемент кортежа обходным путем, преобразовав кортеж в список и обратно
immutable_var = list(immutable_var)
immutable_var[0]  = 23
immutable_var = tuple(immutable_var)
print(immutable_var)
print()
mutable_list = [123, 'Pyton', True, (4, 5)]
print(mutable_list)
mutable_list[3] = 23
print(mutable_list)