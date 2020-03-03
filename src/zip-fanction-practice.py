# 「zip関数」　= 複数のリストを同時に取得したい場合に使用する。
# zip関数はfor文と一緒に使われる。

# days = ['Mon','Tue','Wed']
# fruits = ['apple','banana','orange']
# drinks = ['coffee','tea','beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])


# [i]と言うインデックスを指定しなくてもzip関数で簡略化できる。
# days = ['Mon','Tue','Wed']
# fruits = ['apple','banana','orange']
# drinks = ['coffee','tea','beer']

# zip関数は1番始めのものをピックアップして入れるので　
# zip(days, fruits, drinks): 
# for day, fruit, drinkそれぞれの変数に入る
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)


# 「zip関数」　= 複数のリストを同時に取得したい場合に使用する。
#　引数にインデックスを取得したいリストを指定する。
# 
# zip 
# (リスト１,リスト２,.....) 

# names = ['taro','hanako','jiro']
# ages = [25,30,27]

# for name, age in zip(names, ages):
#     print(name, age)

# ２つ以上のリストのインデックスを取得できる。(インデックスとは？　索引、見出し、指数、指標)
# names = ['taro','hanako','jiro']
# ages = [25,30,27]
# address = ['tokyo','nagoya','kanagawa']

# for name, age, addr in zip(names, ages, address):
#     print(name, age, addr)

# インデックスの数が異なる場合
# インデックス数が少ない値が返され、その分の値は処理されない。
# names = ['taro','hanako','jiro','takeshi','maiko']
# ages = [25,30,27]

# for name, age, in zip(names, ages):
#     print(name, age)

# zip関数はタプル(tuple)としても取得できる。
# names = ['taro','hanako','jiro','takeshi']
# ages = [25,30,27]

# # リストを結合する
# tp = zip (names, ages)

# # タプルの要素を取得
# for val in tp:
#     print(val)
