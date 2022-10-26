import random

# import  ex  - import random
#coin = random.choice(["heads","tails"])


# from    ex --  from random import choice
# from random import choice
'''
coin = choice(["heads","tails"])
print(coin)
'''

#randint
'''
number = random.randint(1,10)
print(number)
'''

# shuffle
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)