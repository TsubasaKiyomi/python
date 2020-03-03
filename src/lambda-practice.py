l = ['pig', 'Dog','cat','bird','Bear']

def change_words(words,func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())



l = ['mike', 'Bob','suzuki','Satou','takahasi']

def a_names(names,func):
    for name in names:
        print(func(name))

a_names(l, lambda name: name.capitalize())