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
for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)