from card import Card
from logic import find_set

class Board:
    def __init__(self):
        self.cards = []

    def refresh(self, cards):
        self.cards = cards

    def find(self):
        return find_set(self.cards)
