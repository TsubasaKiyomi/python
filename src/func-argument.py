def add_num(a: int ,b: int)-> int:
    return a+b
r = add_num(10,20)
print(r)

# int型で関数を定義しているのに　r = add_num('a','b')で文字列にしている。
r = add_num('a','b')
print(r)
# エラーにじゃならないが、intではなくstr型で返ってくる。



