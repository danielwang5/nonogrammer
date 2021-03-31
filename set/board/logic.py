from card import Card

def is_set(cards):
    if len(cards) != 3:
        Exception('Needs 3 cards in a set')
        return False

    if sum(c.color for c in cards) % 3 != 0:
        return False

    if sum(c.shape for c in cards) % 3 != 0:
        return False

    if sum(c.texture for c in cards) % 3 != 0:
        return False

    if sum(c.count for c in cards) % 3 != 0:
        return False

    return True


'''
Given a set of cards, returns three indices of cards that make a set, or (-1,-1,-1).
'''
def find_set(cards):
    NOT_FOUND = (-1,-1,-1)
    if len(cards) < 3:
        return NOT_FOUND

    for x in range(len(cards)-2):
        for y in range(x+1,len(cards)-1):
            for z in range(y+1,len(cards)):
                if is_set([cards[x], cards[y], cards[z]]):
                    return (x,y,z)

    return NOT_FOUND
