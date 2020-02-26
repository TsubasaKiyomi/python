# Capital(頭文字：大文字)頭文字が大小バラバラのlistを統一させる。
# 頭が小文字の部分を大文字に直したい。(tue/fri/sat)
"""
l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
# wordsからwordループした物を引数として渡されたchange_words(words,func)のfuncに渡すと
    for word in words:
# change_words(words,func)のfuncに渡すと print(func(word))のfuncに渡される。
        print(func(word))
# sample_func(wprd)を引数のchange_words(words,func):に渡す。
def sample_func(word):
    # capitalize = 大文字にする。
    return word.capitalize()

change_words(l, sample_func)
"""

# 「lambda」を使い簡単に表示させる。
"""
l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
    for word in words:
         print(func(word))
# lambda で１行にできる。

# def change_words(words,func):
# return word.capitalize()

# lambda word: が　def change_words(words,func):　の引数に渡されて、
# 次の行の　実行するreturn word.capitalize()のreturnを書かずに書ける。なので１行でおさまる。
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)

"""
# さらに lambdaで簡略
l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
    for word in words:
         print(func(word))

# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())

# 小文字にもしたい。。。
l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words,func):
    for word in words:
         print(func(word))
# lamdbaを使わないと、大文字、小文字にしたいコードは４行もかかる
# def sample_func(word):
#     return word.capitalize()

# # lower = 小文字にする
# def sample_func2(word):
#     return word.lower()

# lambdaを使用すればコードは２行で書ける。
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

