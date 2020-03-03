# 辞書forで処理する

# 単純にループさせるとキーワードのx.yしか出せない
d = {'x':100, 'y':200}
for  v in d:
    print(v)

# キーと値を出したい

d = {'x':100, 'y':200}
for k, v in  d.items():
    print(k, ':',v)

