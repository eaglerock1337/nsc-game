from random import shuffle

class Hand:
    """
    A simple class for managing a user's hand in NSC.
    """
    def __init__(self):
        self.cards = []
        self.discards = []

    def add_card(self, card):
        """
        Add a drawn card to the hand.
        """
        self.cards.append(card)

    def discard(self, card):
        """
        Discard a card from the hand and add it to the discard pile.
        """
        self.cards.remove(card)
        self.discards.append(card)

        return card

    def discard_hand(self):
        """
        Discard the entire hand. Discard in random order to randomize
        the showing discarded card.
        """
        shuffle(self.cards)
        for _ in range(len(self.cards)):
            card = self.cards.pop()
            self.discards.append(card)      

    def get_cards(self):
        """
        Return a dict of the card list, with the number of cards as the item.
        """
        result = {}
        for card in self.cards:
            if card in result:
                result[card] += 1
            else:
                result[card] = 1

        return result

    def get_discard(self):
        """
        Get the current visible discarded card.
        """
        if len(self.discards) == 0:
            return None
        else:
            return self.discards[-1]

    def shuffle_discards(self):
        """
        Return all discards for shuffling the deck except the showing discard.
        """
        top_discard = self.discards.pop()
        other_discards = self.discards
        self.discards = [top_discard]

        return other_discards

    def reset(self):
        """
        Reset the hand to the starting values.
        """
        self.cards = []
        self.discards = []