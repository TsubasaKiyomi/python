# 「コメント」
"""
print('xxxx')
間に記入しても反映されない。
print('xxxx')
"""
"""
appole price　＊暗黙の了解でコメントは上段に記入
some_value=100
"""

# 「行が長くなる場合」
"""
pythonは１行に”８０文字”までそれ以上は＼か（）で改行。

s='aaaaaaaaaaaa'\
     +'bbbbbbbbbb'

c=('aaaaaaaaaa'
+'mmmmmmmmmmmmmmm')
"""

# 「if文」　　もし
"""
もし x が 0よりも小さい場合は　negative　を表示それ以外は　表示されない。

x = -10
if x < 0:
    print('negative')
"""


"""
x = 20
# もし x が 0よりも小さい場合は　negative　を表示 
if x < 0:
    print('negative')
# もし x が 0と同じ場合は　zero　を表示 
elif x== 0:
    print('zero')
# もし x が 10と同じ場合は 10　を表示 
elif x == 10:
    print('10')
# （else）”そうでない場合"　上記以外の場合　positive　表示
else:
    print('positive')
#  else + if  elifはいくらでも追加できる。
# "インテント"　　　スペースが４つでないとエラーになる！５つなどはエラー。
"""
"""
# aとbが0よりも大きければ a is positive b is positive を表示 それ以外は表示されない。
a=5
b=-10
if a > 0:
    print('a is positive')
    if b >0:
        print('b is positive')
"""
# 「比較演算子と論理演算子」

"""
＜比較演算子＞　
＊２つの値を比較する時に使用。結果は「True」「False」を返す。

x == y  x　と　y　が等しいか
x != y  x　と　y　が等しくない。異なる。
x > y  x　は　y　より大きい
x < y  x　は　y　より小さい
x >= y  x　は　y　と等しいか大きい
x <= y  x　は　y　と等しいか小さい　
x in y  x　という要素が　y　に存在する
x not in y  x　という要素が　y　に存在しない

a=1
b=2

aがbと等しい場合は　True 等しくない場合は　False
print(a==b)

もしaとbが等しければequalを表示
if a==b:
    print('equal')

aとbが異なる場合は True 同じ場合は False
print(a != b)

aがbより小さい場合は　True
print(a < b)

aがbより大きい場合は　True
print(a > b)

aがbより小さい場合　または　等しい場合は True
print(a <= b)

aがbより大きい場合　または　等しい場合は True
print(a >= b)
"""
"""
＜論理演算子＞
＊論理演算（Bool演算）を行う演算子。"if文"で複数の条件の関数を記述する際に使う。
つまり  "if"  で使う。

〜論理和〜 "or"または
*演算子の左辺または右辺のどちらか１つでも、"True"なら"True"となり両方"False"の場合だけ"False"となる。
True or True  True
True or False True
False or True True
False or False False

〜論理積〜 "and"かつ
＊演算子の左辺および右辺がどちらもTrueならTrueそれ以外はFalse
True and True True
True and False False
False and True False
False and False False

~否定~"not"でない
＊演算子の左辺がTrueならFalse　左辺がFalseならTrueとなる
not True    False
not False   True

"""
"""
a = 3
b = 3
aとbは等しい
print(a==b)

aとbが等しければequalで返す。
if a==b:
    print('equal')

aとbは異なる
print(a!=b)

aがbより小さい
print(a<b)
aがbより大きい
print(a>b)

aがbと等しいかそれよりも小さいか
print(a<=b)

aがbと等しいかそれよりも大きいか
print(a>=b)


a=1
b=2

aもbも真であれば真　それ以外は偽   "and"
if a > 0 and b > 0:
    print('a and b are positive')

# andを使わなかった場合
if a > 0:
    if b > 0:
        print('a and b are positive')

aまたはbが真であれば真
if a > 0 or b > 0:
    print('a or b is positive')
orを使わなかった場合。
if a > 0:
    if b > 0:
        print('a or b is positive')
"""
"""
「inとnotの使い所」
y = [1,2,3]
x = 1

xはyのリストの中にあるか？
if x in y:
    print('in')

yのリストに100はあるか？
if 100 not in y:
    prtint('in)
    
"""
"""
a=2
b=1
aとbが等しくなければ　not equal　で返す。
しかしpythonではこの使い方は薦められていない。
if not a==b:
    print('not equal')

if a != b:
    print('equal')
if a < b:
    print('equal')

「not」も使える。　いつ使うか。
is_ok = True
if is_ok:
    print('hello')

"""

# 「値が入っていない判定をするテクニック」

# 値に変数が入っていたら"True"と判定、中身に何も入っていなかったら"False"
# False 0 0.0 '' [] () {} set()
# is_ok = ()
# if is_ok:
#     print('ok')
# else:
#         print('no')

# 「Noneを判定する場合」
# nullオブジェクトの判定
# pythonでは何も値が入っていないのことを"None"と表現
# is_empty = None
# print(is_empty)

# # ==を使用しての判定はダメ
# if is_empty==None:
#     print(None)

# # isf is_emptyはNoneというオブジェクトですか？
# if is_empty is  None:
#     print('None')
# # Nomeでない場合。
# if is_empty is not None:
#     print('None')

# 「is」って何？

# 1 == True
# # 値を１として”真”同士なのでTrue
# # print(1==True)

# print(1 is True)
# # オブジェクト同士が同じでなければ”真”とならないのでFalse
# print(True is True)
# print(None is None)
# 「is」で判定する時は「None」の時に使う。isはNoneオブジェクトの時に1番使う。
# a=1
# B=2
# 変数１や２が等しいかどうかを使う時には「＝＝」等号を使う

# a=None
#aの中に入っているオブジェクトが”None”かどうかを使う場合は「is」を使う。 


#「while文とbreak文とcontinue文」

# 「while文」（ループ・繰り返し・無限・何回も）

# count = 0
# while True:
# もし５以上ループしたらbreak抜ける。
#     if count > 5:
#         break
# もしカウント２が来たら、countinueスキップする。
#     if count == 2:
#         count += 1
#         continue
# カウント＋１する。
#     print (count)
#     count += 1
# 実行結果は01345

# 「while else文」 while:ループ　else:でない・その他
# count = 0
# while count < 5:
# カウント１の場合はbreak抜ける。
#     # if count == 1:
#     #     break
#     print (count)
#     count +=1
# "else"は"break"を抜けなければdoneの行にいく。
# else:
    #  print('done')
# breakはwhile全体から抜けることなので、結果としては、breakで抜けて終わるので、doneまで行かない。
# breakが無い場合はelseのdoneにいく。

# 「input関数」・while文と一緒によく使う。
# word = input ('ok')の('')内はなんでも入力していい。
# while True:
#     word = input ('ok')
# もしwordに「ok」が来たらbreak
#     if word == 'ok':
#         break
# print('next')
# コンソール上ではprint('next')でループしているが、okを入力するとbreakする。
# str型（文字列）なので、int型（整数）に変える。
# while True:
    # word = input('Enter:')
# int型（整数）に変える
    # num = int (word)
# もしnumが100ならbreakする。
    # if num == 100:
        # break
    # print('next')
# 100じゃない場合はコンソール上でループする。

# 「for文とbraek文とcontinue文」
# for文に行く前に・・・
# list[1,2,3,4,5]と定義してlen入力するのは面倒
# some_list = [1,2,3,4,5]
# i=0
# while i < len (some_list):
#     print(some_list[i])
#     i += 1

# for文
# for 〇〇 in print()
# 反復処理することをイテレータ
# イテレータをinで次々に入れていきループを回し、それが無くなった時点で終了。
# わざわざ自分でループするプログラムを書かなくてもいい
# イテレータを読み込んで出力できるのがforループのいい所。

# some_list = [1,2,3,4,5]
# for f in some_list:
#     print(f)

# 文字でforぶんにした場合
# for s in 'abcde':
#     print(s)

# for word in ['My','name','is','Mike']:
# もしnameが来たらbreakの場合は抜ける。continueの場合はスキップする。
#     if word =='name':
#         continue
#     print(word)

# 「for else文」・while else文と同じ
# for fruit in ('apple','banana','orange'):
#     if fruit == 'banana':
#         print('stop eating')
#         break
#     print(fruit)
# else:
    # print('i ate all')

# 「range関数」・forループと一緒によく使われる。
# range「範囲」
# 例0~9を出力するプログラムを書くとする。
# num_list = [0,1,2,3,4,5,6,7,8,9]
# for i in num_list:
#     print(i)
# [0~9]を書くのは面倒なのでrange関数を使う。
# renge(２,11,3)２から始まり11は0〜10の数字３は3こ飛ばしで表示する。
# for i in range(2,11,3):
#     print(i)

# iの数字と文字のhelloを出力する場合。
# for i in range(5,11,2):
#     print(i,'hello')

# プログラム上後々(i)が必要無くなった場合は'アンダーバーを入力する。(_)
# これはpython上自分だけじゃなく、周りの人も一見で見分けがつくように。
# for _ in range(5,11,2):
#     print('hello')




# print ('ksksksksjfuhsjafighijgojhijksdfjnhkn\
    # dskngknbdsimbpanpinhrgioshfibnsznbknisnhip')
# x = 3
# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# # elif x > 0:
#     # print('up')
# else:
#     print('positive')


# a=2
# b=2

# if a == b:
#     print('good')
# elif a!=b:
#     print('bad')
# elif a >= b:
#     print('equal')
# elif a <= b:
#     print('equal')
# else:
#     print('else')

# a=-8
# b=-7
# if a > 0 and b > 0:
#     print('positive')

# elif a < 0 and b < 0:
#     print('negative')
# elif a > 0 and b < 0:
#     print('True')
# elif a < 0 and b > 0:
#     print('Folse')
# else:
#     print('else')

# if a > 0 or b > 0:
#     print('positive')


# some_list =[1,2,3,4,5]
# i=1
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# a=4
# while True:
#     if a >=5:
#         break
#     print(a)
#     a += 1

# while True:
#     word = input('Enter')
#     if word =='ok':
#         break
#     print('next')
# while True:
#     word = input('Enter')
#     num = int (word)
#     if num == 100:
#         break
#     print('next')



# some_list = [1,2,3,4,5]
# for i in some_list:
#     print(i)

# for s in 'asdfrgg':
#     print(s)


# for i in ['my','name','is','ki']:
#     if i =='name':
#         break
#     print(i)

# for n in ['mf','am','pm','h','y']:
#     if n =='am':
#         continue
#     print(n)


# f=0
# while True:
#     if f > 5:
#         break
#     if f == 3:
#         f += 2
#         continue
#     elif f == 1:
#         f += 2
#         continue
#     print(f)
#     f +=1

