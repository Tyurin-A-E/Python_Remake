#       -----------------------------------------
#   Базовая конструкция для работы с url адресами:
# import webbrowser

# def open_url(url):
#     webbrowser.open(url)

# open_url('http://gooogle.com')
#       -----------------------------------------

#       -----------------------------------------
#   Простой декоратор:
# import webbrowser

# def validator(func):
#     def wrapper(url):
#         print('Текст до')
#         func(url)
#         print('Текст после')
#     return wrapper

# @validator
# def open_url(url):
#     webbrowser.open(url)

# open_url('http://gooogle.com')
#       -----------------------------------------

#       -----------------------------------------
# Выполнение проверки:
import webbrowser

def validator(func):
    def wrapper(url):
        if '.' and 'http' in url:
            func(url)
        else:
            print('You write incorrect url')
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

user_url = input('Write your url: ')
open_url(user_url)
#       -----------------------------------------