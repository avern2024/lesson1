grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print('Оценки:', grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Ученики:', students)
# В цикле определяем среднее арифметическое каждого элемента списка
grades = [sum(x) / len(x) for x in grades]
print('Средние баллы:', grades)
# Упорядочиваем коллекцию students, переводя множество в список
students = list(students)
# Сортируем список по алфавиту
students.sort()
print(students)
# Конвертируем два списка в словарь
students_grades = dict(zip(students, grades))
print(students_grades)