my_dict = {'Dima': 1989, 'Melana': 1990, 'Andrey': 1991, 'Samanta': 1992}
print(my_dict)
print(my_dict['Dima'])
my_dict['Oksana'] = 1985
print(my_dict['Oksana'])
my_dict.update({'Ira': 1999, 'Sergey': 2000})
a = my_dict.pop('Andrey')
print(a)
print(my_dict)
my_set = {"Dom", 33, 20, False, "Dom"}
print(my_set)
my_set.update(["Room", 256])
my_set.remove("Dom")
print(my_set)
