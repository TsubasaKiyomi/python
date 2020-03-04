# while ・条件を指定して　”条件が真の間は「繰り返し処理が実行」できる”

# for文との違い　
# 　foe文は「指定した”回数のループ”」が完了すればループを抜ける。

# while文は「条件を指定し」その条件が”False”になればループを抜ける。条件がTrueの間はループが続く。

# countが５より小さい間はループする。
"""
count = 0

while count < 5:
    print(count)
    count += 1

# countが５以上になった場合は”break”でループから抜ける
count = 0

while True:
    if count >= 5:
        break
    print(count)
    count += 1

# countinueは”スキップ”する！！
count = 0

while True:
    if count >= 5:
        break

    if count == 3:
        count += 1
        continue
    print(count)
    count += 1


# while else
"""

# elseは whlie ループ中breakしなければ（抜けなければ）else('')が出力される

# count = 0

# while count < 5:
#     if count == 6:
#         break
#     print(count)
#     count += 1
# else:
#     print('done')
count = 0

while count < 5:
    if count == 6:
        break
    elif count ==3:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('done')



