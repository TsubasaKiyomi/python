# 「for」「break」「countinue」
# 例
# some_list = [1,2,3,4,5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
# forループでもっと簡単にできる！！！

some_list = [1,2,3,4,5]
for i in some_list:
    print(i)

# 文字列でもforループできる

for s in 'abcde':
    print(s)

# ワードやリストでもループできる

for word in ['my','name','is','mike']:
    print(word)


# 「break」
for word in ['my','name','is','mike']:
    if word == 'name':
        break
    print(word)
# "name"がループで回ってきたらbreakする抜ける


# 「continue」
for word in ['my','name','is','mike']:
    if word == 'name':
        continue
    print(word)
# "name"がループで回ってきたらcontinueするスキップする。

# 「for else文」

for fruit in ['apple','banana','orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    else:
        print('i ate all')