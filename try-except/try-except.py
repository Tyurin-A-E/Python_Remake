#       -----------------------------------------
#   Базовая строка для работы с исключениями:
# try: 
#     x = int(input('Write number: '))
#     x += 5
#     print(x)
# except ValueError:
#     print("Please write number! Don't write the text")
#       -----------------------------------------

#       -----------------------------------------
#   Практическое применение конструкции:
# x = 0
# while x == 0:
#     try: 
#         x = int(input('Write number: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Please write number! Don't write the text")
#         x = 0
#       -----------------------------------------

#       -----------------------------------------
#   Различные виды ошибок: (Нераскомментировать)
# except ZeroDivisionError # Ошибка вызванная при делении на ноль
# except ValueError # Ошибка вызванная при неправильном введённом типе данных
#       -----------------------------------------

#       -----------------------------------------
#   Блок finnaly:
# try: 
#     x = int(input('Write number: '))
#     x += 5
#     print(x)
# except ValueError:
#     print("Please write number! Don't write the text")
# finally:
#     print('Finally')
#       -----------------------------------------

#       -----------------------------------------
#   Блок else:
# try: 
#     x = int(input('Write number: '))
#     x += 5
#     print(x)
# except ValueError:
#     print("Please write number! Don't write the text")
# else:
#     print('else')
#       -----------------------------------------
