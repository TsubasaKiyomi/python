# 「enumerate関数」
# enumerate 直訳　数え上げる、列挙する。
# apple,banana,orangeが表示される。
# for fruit in ['apple','banana','orange']:
#     print(fruit)

# 各fruitに番号を付随。
# i=0にしてループすると+1される。
# i=0
# for fruit in ['apple','banana','orange']:
#     print(i,fruit)
#     i += 1

# i=0  i += 1　としなくても、enumerate関数でできる。
# for i,fruit in enumerate(['apple','banana','orange']):
#     print(i,fruit)

# 「zip関数」
# days = ['man','tue','wed']
# fruits=['apple','banana','orange']
# drinks=['coffee','tea','beer']

# [i]ばかりで分かりにくい
# for i in range(len(days)):
#     print(days[i],fruits[i],drinks[i])

# for day,fruit,drink in zip (days,fruits,drinks):
#     print(day,fruit,drink)

# 「47辞書をfor文で処理する」
# d={'x':100 , 'y':200}
# for v in d:
#     print(v)
# for k,v in d.items():
    # print(k,':',v)

# 「48関数定義」
# def say_samething():
#     print('hi')
# say_samething()

