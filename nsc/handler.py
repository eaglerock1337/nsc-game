import os


class Handler:
    """
    The generic Handler class for handling output.
    Can be inherited by other classes for specific types
    of output (command-line, web, etc.).
    """

    def __init__(self):
        pass

    def print_header(self, deck):
        """
        Print the game status before any prompt.
        """
        self.clear_screen()
        print(f"\nDraw Pile Cards: {len(deck.draw)}")
        print(f"White Discard:   {deck.hands['White'].discards[-1]}")
        print(f"# of Discards:   {len(deck.hands['White'].discards)}")
        print(f"Black Discard:   {deck.hands['Black'].discards[-1]}")
        print(f"# of Discards:   {len(deck.hands['Black'].discards)}\n")

    def show_draw(self, color, card):
        """
        Print out the drawn card for the chosen color.
        """
        print(f"{color}'s Turn:")
        print(f"{color} drew a {card}.\n")
        input("Press Enter once you've taken your move!")

    def choose_play(self, color, hand):
        """
        Prompt for a color to play and return a card to play for the color.
        """
        print(f"{color}'s Turn:")
        print(f"Your hand: {hand.cards}")
        

    def play_card(self, card, difficulty):
        pass

    def clear_screen(self):
        """
        Clear the screen.
        """
        os.system("clear")

    def end_turn(self, color):
        """
        End of turn prompt.
        """
        print(f"{color}'s turn is over.")
        input("Pass the machine to the other player and hit Enter when ready. ")
