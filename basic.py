"""
そもそも「変数とは？」
x = 10 　　 xと言う変数の入れ物に10を代入した
print(10)　　変数xから10を取り出す。
出力結果は10
つまり変数は入れ物のような物。値を＝で代入すれば変数。

変数名 = 値(または、式)

「関数とは」
ある集合の元。処理のまとまりの事。

pythonの型

int型：整数  integer　インテンジャー
小数点を含まない0や正負の数。
x = 10
print(type(x))


float型：小数点　フロート
0.0など、小数点の値、正負の全ての数。
x = 10.5
print(type(x))


str型：文字列 string ストリング
str型として代入された文字・記号・数値などは全て文字列となる。
""ダブルクォーテーションまたは''シングルクォーテーションで囲む
x = 'テキスト'
print(type(x))


bool型：真偽値　ブール
真「True」か偽「False」を判断する。
x = True
print(type(x))

x = False
print(type(x))

list型：リスト
1つの変数で複数の値を扱える。
[]で囲い「,」カンマで区切る。
[]ブランケット・スクエアブランケット
x = [10,20,30,'テキスト']
print(type(X))


tuple型：タプル
１度代入した値は後から変更することはできない
()で囲み代入し「,」カンマで区切る。
()パレンティス
x = (10,20,30,'テキスト')
print(type(x))


dict型：辞書　dictionary　ディクショナリー
リストのように1つの変数で複数の値を扱うことができ、それぞれにkeyキーとなる
ラベルを付けられる。
keyキーと代入値を「:」コロンでつなげ、「,」カンマで区切り
{}で囲む。
{}カーリーブランケット・ブレイス
x = {'a':10, 'b':20, 'c':30, "d":'テキスト'}
print(type(x))

pythonの予約語集
False / class / finally / is / return / None / continue / for /
lambda / try / True / def / from / nonlocal / while / and / 
del / global / not / with / as / elif / if / or / yield /
assert / else / import / pass / break / except / in /raise


グローバル変数
どの範囲からもアクセスできる変数。
1番自由度の高い変数。
グローバル変数を理解するには変数のスコープについて知っておく必要がある。

スコープとは
変数がアクセスできる範囲のこと。
変数はコードのどこに書いてもアクセスできるわけではなく、グローバル変数かローカル変数かに分けられる。
"""
# 例　グローバル変数
# gvar = 'abcdefg'

# def gfunc():
#     print(gvar)

# gfunc()
# print(gvar)

# 実行結果
# abcdefg :gfunc関数での表示
# abcdefg :print関数での表示
#gfunc関数の外にgvar変数を宣言して値を代入する。gfunc関数の外で宣言されたgvar変数は、gfunc関数の中でも表示（参照）させることができる


# ローカル変数
# グローバル変数と違いアクセス範囲が変わる

# def lfunc():
#     lvar = 'abcdefg'
#     print(lvar)
# lfunc()
# print(lvar)

# 実行結果
# abcdefg :lfunc関数での表示
# （エラー）：print関数表示

# lfunc関数の””中で宣言した変数””は、lfunc関数の外側ではprint関数で表示（参照）させることができない。
# この様な変数をローカル変数


# 関数の中からグローバル変数を書き換える方法

gvar = 'abcdefg'

def testfunc():
    gvar = '0123456'
    print (gvar)

print(gvar)
testfunc()
print(gvar)

# 実行結果
# abcdefg　：　print関数での表示
# 0123456　：　testfunc関数での表示
# abcdefg　：　print関数での表示
# 一見書き換わった様に見えるが、testfnuc関数が実行されたあとも
# グローバル変数で代入した値がそのまま表示される。

gvar = 'abcdefg'

def testfunc():
    global gvargvar = 




