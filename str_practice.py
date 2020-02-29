print('test')

print("i don't know")
# シングルクォートで繋ぐとエラー
# print('i don't know')
# 解消するには\を使う
print('i don\'t know')
# 隙間ができるので\で改行する。
print("""\
line1
line2
line3\
""")
print('hi' * 4) #hihihihi
print('hi' * 4 + 'mike') #hihihihimike


# No12 文字列のインデックスとスライス
#インデックス
#       0123456
word = 'python'
print(word) #python 
print(word[0]) #p
print(word[1]) #y
print(word[-1]) #n
#スライス
print(word[0:3]) #pyt
print(word[0:]) #python
print(word[:5]) #pytho
print(word[:]) #python
word = 'j' + word [1:]
print(word) #jython
n = len(word)
print(n) #6



a = 'hello'
print(a)
print(a[3:])
a = 'M' + (a[1:])
print(a)

n = len(a)
print(n)

# 文字のメソッド

s = 'My name is Mike, Hi Mike'
print(s)

# .startswith  ('')[指定したもの]から始まっているか？ 
is_start = s.startswith('My')
print(is_start)

# .find ('')[指定したものが]何番目にあるか？
print(s.find('Mike'))

# .rfind ('')[指定したものが(２個以上ある場合)]何番目にあるか？
print(s.rfind('Mike'))

# .count('')[指定したもの]いくつあるのか？
print(s.count('Mike'))

# .capitalize()最初の文字は大文字、その他は小文字
print(s.capitalize())

# .title()全ての頭文字が大文字
print(s.title())

# .upper()全て大文字
print(s.upper())

# lower()全て小文字
print(s.lower())

# .replace()指定したものを変更する
print(s.replace('Mike','Bob'))