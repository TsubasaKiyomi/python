"""
 引数piを初めに決めてしまう！後々用途によって使い分ける。
 
# f = outer(1,2)はdef outer(a,b):に入り、return a + b　1 + 2　となるが、return inner　がまだ実行されていない
# return innerの返した物が　f = outer(1,2)の　f　にあるのでまだ、実行されない。
# r = f()を実行すると。def inner()　return a + b　が実行される　a + b には　1 と 2 が入っているので 3　が返ってくる。
#return innerでさらに返すので r = f()　の r に 3 が入る。
def outer(a,b):

    def inner():
        return a + b
# innerを実行するのではなく、ファンクションのオブジェクトを返す
    return inner

f = outer(1,2)
r = f()
print(r)

# どんな時に使うのか？
def outer(a,b):
    
    def inner():
        return a + b
    
     return inner
# () に入れた値を気にせずに実行したい場合に使用する
f = outer(1,2)
r = f()
print(r)
"""

# 例えば円の面積を調べたい時
# 引数をパイ pi

def circle_area_func(pi):
# インナーは半径
    def circle_area(radius):
        return pi * radius * radius

    return circle_area
# cl1には3.14の半径をca2にはさらに細かい数字を
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)
# 3.14を使いたい時はca1を　もっと細かい数字を使いたい時はca2を。
print(ca1(10))
print(ca2(10))
# 引数piを初めに決めてしまう！後々用途によって使い分ける。