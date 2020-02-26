# iterater(反復処理する物)
# generator(反復処理と生成する)i　　teraterの要素　　一要素を取り出してそれを生成していく


l = ['Good morning','Good afternoon','Good night']

for i in l:
    print(i)

# yield (産出する)  greeting(挨拶)
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
    

# for g in greetingz():
    # print(g)

g = greeting()

print(next(g))

print('@@@@@@')
print(next(g))

print('@@@@@@')
print(next(g))


