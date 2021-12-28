import random as r

class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(value+suit)

    def __len__(self):
        return len(self.cards)
        
    def shuffle(self):
        r.shuffle(self.cards)
    
    def deal(self, n):
        if n > len(self.cards):
            return self.cards
        return [self.cards.pop() for i in range(n)]

    def copy(self):
        new = Deck()
        new.cards = self.cards.copy()
        return new

    def get_cards(self):
        return self.cards.copy()
    
    def contains(self, card):
        return card in self.cards

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )
                
