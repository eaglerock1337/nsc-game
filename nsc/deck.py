from random import shuffle

DECK_CONFIG = {
    "King":   7,
    "Queen":  8,
    "Rook":   8,
    "Bishop": 8,
    "Knight": 8,
    "Pawn":   11,
    "Same":   6,
}

class Deck:
    """
    A class for managing the deck of cards used by NSC.
    """
    def __init__(self):
        self.deck = []
        for card_type in DECK_CONFIG.keys():
            for _ in range(DECK_CONFIG[card_type]):
                self.deck.append(card_type)
        self.draw = []
        self.white_discard = []
        self.black_discard = []
        self.difficulty = 0

    def set_difficulty(self, difficulty):
        """
        Set the difficulty mode of NSC:
        Level 1 - No hand, can only play the drawn card
        Level 2 - 3 cards in hand, draw per turn, and choose between the 4 cards
        Level 3 - 5 cards in hand, draw per turn, and choose between the 6 cards
        """
        self.difficulty = difficulty

    def shuffle(self):
        self.draw = self.deck.copy()
        shuffle(self.deck)
        
    