# def say_something():
#     print('hi')
# say_something()
# print(type(say_something))
# f「function」
# f = say_something
# f()

# 返り値 return 返り値

# def say_something():
#     s = 'hi'
#     return s

# result = say_something()
# print(result)


# 「引数」
# (color)の部分が”引数”
# def what_is_this (color):
#     print(color)
# what_is_this('red')


def what_is_this (color):
    if color =='red':
        return 'tomato'
    elif color =='green':
        return 'green pepper'
    else:
        return "i don't know"
result = what_is_this('green')
print(result)

