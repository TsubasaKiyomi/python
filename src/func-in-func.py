"""
# 関数を定義する
def outer(a,b):
    print(a,b)
outer(1,2)

# 関数の中に関数を作る
# outer(1,2)がdef outer(a,b):のaとbに入り
def outer(a,b):
    # インナー定義された関数に渡す。
    def plus(c,d):
        return c + d
# 返り値は(r)なので　３
    r = plus(a,b)
    print(r)

outer(1,2)
"""
# 関数内だけで使う関数
# outerという関数の中で何回も使用できる。
def outer(a,b):

    def plus(c,d):
        return c + d

    r1 = plus(a,b)
    r2 = plus(b,a)
    print(r1+r2)

outer(1,2)