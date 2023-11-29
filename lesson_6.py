#a = {2: 1, 'a': 4}
#b = a.pop('a')
#print(b)
#print(a)
word = input("Введите слово на немцком: ").capitalize()
deutch = {"Ich" : "Я", "Du": "Ты", "Er": "Он", "Schmetterling": "Бабочка"}
def translate(word):
    return deutch.get(word)
print(translate(word))