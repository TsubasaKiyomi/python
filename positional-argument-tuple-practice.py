def say_something(word):
    print(word)

say_something('hi')

# # word以外の引数を増やしたい。

def say_something(word,word2,word3):
    print(word)
    print(word2)
    print(word3)
say_something('hi','mike','nance')

# 実行できるが、これだと長いし分かりにくい。

# "まとめられる引数がある。"「*args」アーグス
# (word,word2,word3)　= *args　　
# "" *args タプルの型になる ""
# 実行結果は全てタプルに入れてくれる。
def say_something(*args):
    print(args)
say_something('hi','mike','nance')

# forループで実行すると。
def say_something(*args):
    for arg in args:
        print(arg)

    say_something('Hi','Midske','Nance')



def say_something(word, *args):
    print('wodr =', word)
    for arg in args:
        print(arg)
# タプルを展開して、mike/nanceに、さらにタプルをアンパッキングして、 *argsに渡してタプル化タプル化して入れる。
t = ('mike', 'nance')
say_something('Hi', *t)

# def say_something(word, *args):
#     print('wodr =', word)
#     for arg in args:
#         print(arg)
#     say_something('Hi','Mike','Nance')

# #「 引数を何個入れても　*argsでまとめて、タプル化してくれる」