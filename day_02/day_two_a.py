# Input = Encrypted strategy guide
#   OPPONENT YOU
#
#   opponent's side
#   A = ROCK
#   B = PAPER
#   C = SCISSORS
#
#   you side
#   X = ROCK
#   Y = PAPER
#   Z = SCISSORS
#
#   each round:
#       1 = ROCK
#       2 = PAPER
#       3 = SCISSORS
#       +
#       6 = WINNING
#       3 = DRAW
#       0 = LOSING
#
# PART A QUESTION:
#   CALCULATE HOW MANY POINTS YOU WILL GET


class Hand:
    def __init__(self, name, value, wins_against, loses_against) -> None:
        self.name = name
        self.value = value
        self.wins_against = wins_against
        self.loses_against = loses_against

    def get_name(self):
        return self.name

    def compete_with(self, other_hand):
        if other_hand.get_name() == self.name:
            return self.value + 3
        elif other_hand.get_name() == self.wins_against:
            return self.value + 6
        elif other_hand.get_name() == self.loses_against:
            return self.value + 0
        else:
            print("error")


rock = Hand("rock", 1, "scissors", "paper")
paper = Hand("paper", 2, "rock", "scissors")
scissors = Hand("scissors", 3, "paper", "rock")

you = {
    "A": rock,
    "B": paper,
    "C": scissors,
}

me = {
    "X": rock,
    "Y": paper,
    "Z": scissors,
}


my_scores = []
with open("day_02/input.txt") as file:
    for line in file:
        text = line.strip()
        your_choice = you[text[0]]
        my_choice = me[text[-1]]
        result = my_choice.compete_with(your_choice)
        my_scores.append(result)


print("Answer: ", sum(my_scores))
# correct answer: 13526
