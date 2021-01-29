class Hand:
    def __init__(self, dec_hand = 0, bust = -30):
        '''
        parameters:
        - hand : int
            the binary of hand represents the state of the hand. The position of bin(hand) denotes which card had been drawn. The encoding is given by `encoding`.
        '''
        self.__dec_hand = dec_hand
        self.__bust = bust
        self.__binary_hand = "0"*(26-len(bin(dec_hand)[2:])) + bin(dec_hand)[2:]
        self.__points = self.__calculate_points()
        self.__score = self.__calculate_score()

    # possibilities of outcomes for different combination of A's
    __A_possibilities = {
        (0, 0) : [0],
        (0, 1) : [-11, -1],
        (1, 0) : [1,11],
        (1, 1) : [-10, 0, 10]
    }

    __encoding = {
        0 : "A",
        1 : "B",
        2 : 2,
        3 : 3,
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 7,
        8 : 8,
        9 : 9,
        10 : 10,
        11 : 10,
        12 : 10,
        13 : 10,
        14 : -2,
        15 : -3,
        16 : -4,
        17 : -5,
        18 : -6,
        19 : -7,
        20 : -8,
        21 : -9,
        22 : -10,
        23 : -10,
        24 : -10,
        25 : -10
    }

    def calculate_points(self):
        '''Calculate the points given the hand'''
        points = sum([int(flag)*self.__encoding[index+2] for index,flag in enumerate(self.__binary_hand[2:])])

        # Processing A and B
        A = int(self.__binary_hand[0])
        B = int(self.__binary_hand[1])

        possible_points = [(A_B + points) for A_B in self.__A_possibilities[(A,B)] if A_B + points < 26]

        if len(possible_points) == 0:
            return self.__bust

        return max(possible_points)

    def __calculate_score(self):
        if self.__points <= 10:
            return self.__points
        elif self.points <= 15:
            return 10
        elif self.points <= 25:
            return self.__points
        else:
            return self.__bust

    def get_cards(self):
        '''Return list of cards in the hand'''
        return [self.__encoding[index] for index,flag in enumerate(self.__binary_hand) if flag == "1"]

    def get_hand(self):
        return self.__dec_hand

    def get_binary_hand(self):
        return self.__binary_hand

    def get_one_hot(self):
        return [bool(flag) for flag in self.__binary_hand]

    def get_points(self):
        return self.__points

    def get_score(self):
        return self.__score