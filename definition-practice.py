"""
# 「関数定義」(definitionの略：定義の意味)
def say_something():
    print('hi')
#()パレンティスの（）が無いとprintされない。 
say_something()
# typeを調べられる。
print(type(say_something))
# <class 'function'>でprintされるので
f = say_something
f()

# 返り値
def say_something():
# sという変数を宣言し、sの中にhiを入れる。そのsを返したいのでreturn
# returnするとhiがsに入り
    s = 'hi'
# sがreturn s　に入って返してくれる。
    return s
# 返した物が、resultに入るので
result = say_something()
print(result)

 
# colorが「引数」
def what_is_this(color):
    print(color)
# ファンクション(関数)を呼び出す。what_is_this（関数値）のなかにredが入る。
what_is_this('red')


# result：結果

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'greenpepper'
    else:
        return "i don't know"

# if文などで、何回もコードを書かなくても、関数定義しておけば良い！
result = what_is_this('red')
result = what_is_this('green')
result = what_is_this('yellow')
print(result)



# def  関数名（引数１、引数２・・・):
    #    処理
    #    return 戻り値/返り値
# 呼び出し
# 関数名（引数１、引数２・・・・）
# 例。
def add (a,b):
    return a + b
x = add (3,4)
print(x)


def r (a,b,c):
    return a - b + c
x = r (3,7,9)
print(x)


# 位置引数とキーワード引数とデフォルト引数
# 関数定義:def　# menuという関数を作成　entreeという引数を作成
def menu(entree):
    print(entree)
# 値はbeefを出力。
menu('beef')

# 引数は複数実行可能
# 引数は「,」カンマで区切る。
def menu(entree, drink, dessert):
    # 実行する値（printされる）はenteree/drink/dessertだが、menuに入っているのは、beef/beer/ice
    print(entree)
    print(drink)
    print(dessert)
menu('beef','beer','ice')

# 仮に順序がバラバラになったら・・・・
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)
menu('ice','beer','beef')
# 結果が変わり、entree = ice / dessert = beefとなってしまう。
 
#  順序の間違えが起こらないように
#　キーワードアニュメント？
# キーワードを指定するとprintとmenuの順番が変わっていても、キーワードに沿った実行結果となる。
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)
menu(dessert='ice', drink='beer',entree='beef')

#位置引数とキーワード引数を混ぜて使用できる。 　
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)
#位置引数とキーワードで出力できるがキーワードは最初のワードのみ適応されるようだ。
menu('beef', drink='beer',dessert='ice')
# 以下２つはエラーとなった。
# menu(entree='beef','beer',dessert='ice')
# menu(entree='beef', drink='beer','ice')

# 「デフォルト引数」デフォルト：Default　/　基本
# 各引数にデフォルト（基本値）を与える。('beer','wine','ice')

def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)
# menuに何の引数を与えない場合はデフォルト値である('beer','wine','ice')が返ってくる。
# menu()

# 引数を与えれば、実行結果も変わる。
menu(entree='chicken')
# 位置引数・キーワード引数・デフォルト引数を混ぜて使える。
menu('chicken' , drink='beer') 
"""

# リストはデフォルト引数で与えては行けない。
# デフォルト引数で気を付けること。
# x,lの引数を作り、lはデフォルト引数にするl=[]

def test_func(x, l=[]):
# lのリストに対してxを入れる
# append = 追記
    l.append(x)
# xのリストを返す。
    return l

# リスト[1,2,3,]があったとして
# y = [1,2,3]
# test_funcを呼び出す時に100を追加したい場合
# r = test_func(100,y)
# print(r) 
#結果としては、yに入れた変数[1,2,3]がl=[]に代入されて、l.append(x)に100が返る。
# 値を追記しても大丈夫。
# y = [1,2,3]
# r = test_func(200,y)
# print(r)

# 全く同じ内容の値を入れると[100, 100]と返ってくる。これはバグに繋がる。
# r = test_func(100)
# print(r)
# r = test_func(100)
# print(r)

# リストは参照渡しなので、test_funcを始めに定義した時点で、l=[]の空を生成してまうので[100][100]となってしまい、バグに繋がる。
# pythonではdefやdicの参照渡しの物をデフォルトとして使用してはダメ。

# 解決としてNoneを使用
def test_func(x, l = None):
# もしif lがNone(ノン)であれば 
    if l is None:
# lにからのリストを初期化して入れる。
        l = []
    l.append(x)
    return l
#　引数として何かが入っていればappendする
# Noneの時だけ自分のプログラム内で初期化して空のリストを出す。

r = test_func(100)
print(r)
r = test_func(100)
print(r)
        

