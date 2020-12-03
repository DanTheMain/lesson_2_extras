# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

names = [student['first_name'] for student in students]
for name in set(names):
    print(f'{name}: {names.count(name)}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

names = [student['first_name'] for student in students]
max_repeated_name, max_count = names[0], names.count(names[0])
for i in range(1, len(names)):
  if names.count(names[i]) > max_count:
    max_repeated_name = names[i]
print(f'Самое частое имя среди учеников: {max_repeated_name}') 


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
school_classes = {i + 1: school_students[i] for i in range(0, len(school_students))}
for class_id, students in school_classes.items():
    names = [student['first_name'] for student in students]
    print(f'Самое частое имя в классе {class_id}: {max(set(names), key = names.count)}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
for a_class in school:
  student_genders = [is_male[student['first_name']] for student in a_class['students']]
  print(f"В классе {a_class['class']} {student_genders.count(False)} девочки и {student_genders.count(True)} мальчика.")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

max_males, max_females = {'class': None, 'count': 0}, {'class': None, 'count': 0}
for a_class in school:
  student_genders = [is_male[student['first_name']] for student in a_class['students']]
  male_count = student_genders.count(True)
  female_count = student_genders.count(False)
  if female_count > max_females['count']:
    max_females.update({'class': a_class['class'], 'count': female_count})
  if male_count > max_males['count']:
    max_males.update({'class': a_class['class'], 'count': male_count})
print(f"Больше всего мальчиков в классе {max_males['class']}") 
print(f"Больше всего девочек в классе {max_females['class']}") 
