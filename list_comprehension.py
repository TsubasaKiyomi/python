t = (1,2,3,4,5)
 

r = []
for i in t:
    r.append(i)

print(r)

r = [i for i in t]
print(r)

t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# リスト内包表記は１行で表示できる
# forループで取り出してきたiをそのままリストに追記してる。
# r = [i for i in t]
# ２で割ったあまりが0
r = [i for i in t if i % 2 == 0]
print(r)

# list内包表記の基本的な書き方
# list_example = [iの処理 for i in 配列]

# 例  0〜10までの数字の２乗をlistに追加する
list_1 = [i**2 for i in range(10)]
print(list_1)
# 上記を普通に書いたら
list_1 = []
for i in range(10):
    i = i**2
    list_1.append(i)
print(list_1)


# for文・内包表記
# list_example = [iの処理 fro i in 配列]
# 1〜10までの数字で２の倍数の物だけをlist_2に入れる
list_2 = [i for i in range(2,11,2)]
print(list_2)

# forの２重ループ
#

list_3 = [[i,j] for i in range(10) for j in range(10)]
print(list_3)

list_3 = [print("{}x{}={}".format(i,j,i*j))for i in range(1,10) for j in range(1,10)]

