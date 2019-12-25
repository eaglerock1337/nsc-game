from random import shuffle

from nsc.hand import Hand

DECK_CONFIG = {
    "King": 7,
    "Queen": 8,
    "Rook": 8,
    "Bishop": 8,
    "Knight": 8,
    "Pawn": 11,
    "Same": 6,
}

COLORS = ["White", "Black"]


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
        self.hands = {}
        for hand in COLORS:
            self.hands[hand] = Hand()
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
        """
        Shuffle the discard piles into the draw pile.
        """
        for color in COLORS:
            discards = self.hands[color].shuffle_discards()
            self.draw.extend(discards)
        shuffle(self.draw)

    def new_game(self):
        """
        Prepare the deck and hands for a new game.
        """
        self.draw = self.deck.copy()
        shuffle(self.draw)
        for hand in COLORS:
            self.hands[hand].reset()

    def draw_card(self, color, amount=1):
        """
        Draw a card or cards for the specified color.
        """
        for _ in range(amount):
            card = self.draw.pop()
            self.hands[color].add_card(card)
