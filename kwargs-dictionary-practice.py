"""
def my_sum(*args):
    return sum(args)

print(my_sum(1,2,3,4),(5,6,7,8,9))

# print(my_sum(1,2,3,4,5,6,7,8))

def my_sum2(*args):
    print('args:', args)
    print('type:',type(args))
    print('sum :', sum(args))

my_sum2(1,2,3,4)
# my_sum2(1,2,3,4)　は　my_sum2(*args)に渡して合計を出している。
def func_args(arg1,arg2,*args):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('args:', args)

func_args(0,1,2,3,4)
#rag1: 0  位置指定
#arg2: 1　位置指定
#args: (2, 3, 4) その他をまとめる。タプルで。

func_args(0,1)
# arg1: 0　位置指定
# arg2: 1　位置指定
# args: ()　その他の物が無いので空の（）となっている
"""
# **kwargs
# 'arg1', 'arg2', key1=1, key2=2, key3=3 )
# kwargs: {'key1': 1, 'key2': 2, 'key3': 3}
# type: <class 'dict'>
# 関数の中では、引数名がキーkey 値がvalue　型は辞書として受け取られる。


def animals(anm, *args, **kwargs):
    print(anm)
    print(args)
    print(kwargs)
animals('dog','cat','pig',big='tiger',small='rabbit')
# 実行結果
dog
('cat', 'pig')
{'big': 'tiger', 'small': 'rabbit'}