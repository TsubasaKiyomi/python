# 辞書型のメソッド

d = {'x':10, 'y':20}
# print(d)

# .keys　キーを返す
print(d.keys())

#  .values 値を返す
print(d.values())

# dictをアップデートさせる
d2 = {'x':1000, 'j':500}
d.update(d2)
print(d)

# 値を取り出す
print(d.get('x'))
print(d.pop('x'))

#値を消す  変数自体消してしまうと全てなくなるので、Errorになる
del d ['y']
print(d) 

# 値を消す　変数を消すとNoneとして返ってくる。
# tipe は<class 'dict'>で返ってくる
# 中身のない{}で返ってくる
d = {'x':100,'c':300}
print(d.clear())
print(type(d))
print(d)

d = {'a':100,'c':300}

# 辞書の使い所
# listリストと違い、「キーワード」（apple)が分かれば、「バリュー」（100円）が瞬時に分かる
fruits = {
    'apple':100,
    'banana':200,
    'orange':300,
}
print(fruits['apple'])