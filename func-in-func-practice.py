def func(a,b,e):

    def func2(c,d,e):
        return c + d + e

    o1= func2 (a,b,e)
    o2= func2 (a,b,e)
    # o3= func3 (a,b,e)
#３つ目のo3を入れるとエラーになる
 
    print(o1 + o2 - o1)

func(3,5,5)
