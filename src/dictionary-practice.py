# 辞書
d = {'x':100, 'y':200}
for v in d:
    print(v)
# kyeであるx yが出力される。

# 　value値も出力させる・
d = {'x':100, 'y':200}
# メソッドdictionary辞書にはitemsと言うメソッドがある。itemsを使うと　k　には　key である 'x' が入り、 v には値である 100 が入る。
for k, v in d.items():
    print(k, ':', v)


d = {'x': 100, 'y': 200}
print(d.items())
# リストの中にタプルがあるx yはタプルのアンパッキングになっている。
# ([('x', 100), ('y', 200)])


for k, v in d.items():
    print(k, ':',v)