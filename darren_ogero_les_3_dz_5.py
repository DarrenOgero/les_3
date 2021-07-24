from random import choice


def get_jokes(n):
   nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
   adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
   adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
   bonus = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
   for i in range(n):
      print()

print(get_jokes(2))

