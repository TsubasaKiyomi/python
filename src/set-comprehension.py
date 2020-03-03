s = set ()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

# 内容は同じだけど　{}　[]　の違い
# 集合内包表記
s = {i for i in range(10) if i % 2 == 0}
print(s)

# リストではないので結果がバラバラに表示される
s = {i**2 for i in range(10)}
print(s)

# リスト内包表記
l = [i for i in range(10) if i % 2 == 0]
print(l)

l = [i**2 for i in range(10)]
print(l)
