import random

class Card:

    def __init__(self, name, line, lst_g):
        self.name = name
        self.line = line
        self.lst_g = lst_g
# метод
    def get_full_line(self):
        for i in range(1, 6):
            g = random.choice(lst_g)
            self.line.append(g)
            lst_g.remove(g)
        print(self.line)
        self.line.sort()
        # print(self.line)
        return self.line

# line = []
lst_g = [_ for _ in range(1, 91)]
print(lst_g)
Card1_line1 = Card('Player', [], lst_g)
Card1_line2 = Card('Player', [], lst_g)
Card1_line3 = Card('Player', [], lst_g)
Card2_line1 = Card('Player', [], lst_g)
Card2_line2 = Card('Player', [], lst_g)
Card2_line3 = Card('Player', [], lst_g)
print(len(lst_g))

# Card1.get_full_line()
Player_card = [(Card1_line1.get_full_line()), (Card1_line2.get_full_line()), (Card1_line3.get_full_line())]
Comp_card = [(Card2_line1.get_full_line()), (Card2_line2.get_full_line()), (Card2_line3.get_full_line())]

print(Player_card)
print(Comp_card)
print(len(lst_g))

