r =[1,2,3,4,5,1,2,3]
print(r.index(3)) #3は r のどこにあるか（何番目）？ 2
print(r.index(3,3))#2つ目の3は何番目にあるか？ 7

print(r.count(3))#rのなかに3は何個ある？　2

# ソート順の並べ替えてくれる
r.sort()
print(r)

# 逆順に並べる
r.sort(reverse=True)
print(r)

# 上記を更に元に戻す
r.reverse()
print(r)

# split「分ける」　s.split(' ')スペースで分ける　＃['Mi', 'name', 'is', 'Mike.']
s = 'Mi name is Mike.'
to_split = s.split(' ')
print(to_split)

# 上記を戻す  .join 繋げる　x = ' 'スペースで繋げる
x = ' '.join(to_split)
print(x)


test = 'apple banana orange.'
#[]()は必要ないエラーとなる
to_split = test.split(' ')
 #無意味な文字を入れても何も変わらない
print(to_split)

v = ' '.join(to_split)
print(v)