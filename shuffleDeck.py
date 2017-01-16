import random

# O(n) time complexity. Linear space complexity. Constant auxiliary space.
# We switch the ith element with the randomly selected element, and we only
# search in the slice of deck[i:], so we don't have any repeats.
def shuffleDeck(deck):
    remaining = len(deck)
    for i in range(len(deck)):
        pick = i + int(random.random()*remaining)
        deck[i], deck[pick] = deck[pick], deck[i]
        remaining -= 1
    return deck