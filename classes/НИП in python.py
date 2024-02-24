#       -----------------------------------------
#   Наследование:
# class Building:
#     year = None
#     town = None

#     def __init__(self, year, town):
#         self.year = year
#         self.town = town

#     def get_info(self):
#         print('Year: ', self.year, '. Town: ', self.town)

# class School(Building):
#     pupils = 0

#     def __init__(self, pupils, year, town):
#         super(School, self).__init__(year, town)
#         self.pupils = pupils
        
# class Shop(Building):
#     pass

# class House(Building):
#     pass

# school = School(100, 2000, 'Moscow')
# house = Building(2000, 'Moscow')
# shop = Building(2000, 'Moscow')
#       -----------------------------------------

#       -----------------------------------------
#   Полиморфизм:
# class Building:
#     year = None
#     town = None

#     def __init__(self, year, town):
#         self.year = year
#         self.town = town

#     def get_info(self):
#         print('Year: ', self.year, '. Town: ', self.town)

# class School(Building):
#     pupils = 0

#     def __init__(self, pupils, year, town):
#         super(School, self).__init__(year, town)
#         self.pupils = pupils

#     def get_info(self):
#         super().get_info()
#         print('Pupils: ', self.pupils)
        
# class Shop(Building):
#     pass

# class House(Building):
#     pass

# school = School(100, 2000, 'Moscow')
# school.get_info()
# house = Building(2000, 'Moscow')
# shop = Building(2000, 'Moscow')
#       -----------------------------------------

#       -----------------------------------------
#   Инкапсуляция
class Building:
    __year = None
    __town = None

    def __init__(self, year, town):
        self.year = year
        self.town = town

    def get_info(self):
        print('Year: ', self.year, '. Town: ', self.town)

class School(Building):
    pupils = 0

    def __init__(self, pupils, year, town):
        super(School, self).__init__(year, town)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print('Pupils: ', self.pupils)
        
class Shop(Building):
    pass

class House(Building):
    pass

school = School(100, 2000, 'Moscow')
school.get_info()
house = Building(2000, 'Moscow')
house.get_info()
shop = Building(2000, 'Moscow')
shop.get_info()
#       -----------------------------------------