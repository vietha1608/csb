class Card:
    def __init__(self,value, suit):
        self.value = value
        self.suit = suit
        def __str__ (self):
            return f"{self.value} of {self.suit}"
class Deck:
    suit_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    value_order = ["heart", "diamond", "club", "spade"]
    def __init__(self, cards):
        self.cards = []
        for suit in Deck.suit_order:
            for value in Deck.value_order:
                self.cards.append(Card(value,suit))
    def display(self):
        for cards in self.cards:
            print(cards)
deck = Deck()
print("INITIALIZE DECK:", deck, "\n")


deck.shuffle()
print("DECK AFTER SHUFFLE:", deck, "\n")
deck.deal_a_card()

print("DECK AFTER DEAL:", deck, "\n")
deck.deal_a_card()


print("DECK AFTER DEAL:", deck, "\n")
deck.sort()


print("DECK AFTER SORT:", deck, "\n")