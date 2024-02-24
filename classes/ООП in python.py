#       -----------------------------------------
#   Создание класса в python: 
#   Пример: создание класса с целью описания котов
# class Cat:
#     name = None
#     age = None
#     isHappy = None

#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy

#     def get_data(self):
#         print(self.name, 'age:', self.age, '. Happy:', self.isHappy)

# cat1 = Cat()
# cat1.set_data('Барсик', 3, True)

# cat2 = Cat()
# cat2.set_data('Васька', 2, False)

# cat1.get_data()
# cat2.get_data()
#       -----------------------------------------

#       -----------------------------------------
#   Создание конструкторов
# class Cat:
#     name = None
#     age = None
#     isHappy = None

#     def __init__(self, name = 'Неизвестно', age = 'Неизвестен', isHappy = 'Неизвестно'):
#         self.set_data(name, age, isHappy)
#         self.get_data()

#     def set_data(self, name = 'Неизвестно', age = 'Неизвестен', isHappy = 'Неизвестно'):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy

#     def get_data(self):
#         print(self.name, 'age:', self.age, '. Happy:', self.isHappy)

# cat1 = Cat('Барсик', True)
# cat1.set_data('Джон', 2)

# cat2 = Cat('Васька', 2, False)
#       -----------------------------------------
