class Blackjack():
    def __init__(self, cards):
        self.cards = cards

    def hand(self):
        """makes a list of your card values

        Returns:
            list: e.g. [1, 12]
        """
        deck = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            'j': 10,
            'q': 10,
            'k': 10,
            'a': 11
        }
        result = []

        for i in self.cards:
            result.append(deck[i])

        return result

    def hand_value(self):
        """returns the sum of hand values

        Returns:
            int: simple hand value
        """
        hand = self.hand()
        result = sum(hand)

        if 'a' in self.cards and result > 21:
            result -= 10
        return result
    

