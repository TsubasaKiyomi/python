# 関数　=　function  定義 = definition
# def menu(entree='beef',drink='wine'):
#     print(entree, drink)
# menu(entree='beef',drink='coffee')
# 実行結果は beef coffee

# 引数を（dessert等）追加して行きたい  **kwargs　（keyword　argsの略)(args = argument)

# def menu(**kwargs):
#     print(kwargs)
# menu(entree='beef',drink='coffee')
# 実行結果   {'entree': 'beef', 'drink': 'coffee'}　となる。
# 　""**args 辞書の型になる"""    "" *args タプルの型になる ""

# def menu(**kwargs):
#     # print(kwargs)
#     for k, v in kwargs.items():
#         print(k,v)
# menu(entree='beef', drink='coffee')
# 実行結果は entree beff  dorink coffeeとなり キーワードとバリューが扱える


#  (**d)(dictionary)
# 一度(**d)で展開されて、渡される。（キーワード引数のように）
# 渡されたら(**kwargs)でまた、辞書化されて   for k, v in kwargs.items():　　print(k,v)　のfunction内で辞書として使える。
# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k,v)

# d = {
#     'entree':'beef',
#     'dorink':'ice cofee',
#     'dessdrt':'ice'}
# menu(**d)


# 　位置引数とタプル化(*args)と辞書化(**args)を一度に表示
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana','apple','orange',entree='beef',drink='coffee')

# 実行結果　位置引数の　food　に　banana 
# *args まとめた物として('apple', 'orange')
# **kwargs キーワードで出したので{'entree': 'beef', 'drink': 'coffee'}