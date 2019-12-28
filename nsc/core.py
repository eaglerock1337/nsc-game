from nsc.deck import Deck


COLORS = ["White", "Black"]

DIFFICULTY = {
    1: 0,
    2: 3,
    3: 5,
}


class Core:
    """
    The core NSC class that handles the game logic.
    Can work with multiple output handlers for command-line or
    a web interface.
    """

    def __init__(self, handler, difficulty=1):
        self.deck = Deck()
        self.handler = handler
        self.set_difficulty(difficulty)
        self.turn = "White"
        self.play = True

    def set_difficulty(self, difficulty):
        """
        Set the difficulty mode of NSC:
        Level 1 - No hand, can only play the drawn card
        Level 2 - 3 cards in hand, draw per turn, and choose between the 4 cards
        Level 3 - 5 cards in hand, draw per turn, and choose between the 6 cards
        """
        self.difficulty = difficulty
        self.hand_size = DIFFICULTY[difficulty]

    def new_game(self):
        """
        Set up a new game based on the set difficulty.
        """
        self.deck.new_game()
        self.turn = "White"
        for _ in range(self.hand_size):
            for color in COLORS:
                self.deck.draw_card(color)

    def take_turn(self, color):
        """
        Take a turn for the provided color.
        """
        self.deck.draw_card(color)
        self.handler.print_header(self.deck)

        if self.difficulty == 1:
            card = self.deck.hands[color].cards[0]
            self.deck.hands[color].discard(card)
            self.handler.show_draw(color, card)
        else:
            card = self.handler.choose_play(color, self.deck.hands[color])
            self.deck.hands[color].discard(card)
            self.handler.print_header(self.deck)
            self.handler.play_card(self, card, self.difficulty)

    def move_prompt(self, color):
        """
        Prompt for the next move.
        """
        pass

    def play_game(self):
        """
        Main routine for playing a game of NSC.
        """
        while self.play:
            self.take_turn(self.turn)

            self.handler.print_header(self.deck)
            self.handler.end_turn(self.turn)

            if self.turn == "White":
                self.turn == "Black"
            else:
                self.turn == "White"
