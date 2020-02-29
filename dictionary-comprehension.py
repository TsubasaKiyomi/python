w = ['mon', 'tue', 'wed']
f = ['coffe', 'milk', 'water']

d ={}
# zip 複数のイテラブルオブジェクト(リストやタプル)をまとめる物
for x, y in zip(w, f):
    d[x] = y
print(d)

# 上記の辞書型を内包表記にする
#  x: y = キー（x）とバリュー（y）
d = {x: y for x, y in zip(w, f)}
print(d)