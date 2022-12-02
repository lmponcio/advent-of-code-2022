# Input = Encrypted strategy guide
#   OPPONENT YOU
#
#   opponent's side
#   A = ROCK
#   B = PAPER
#   C = SCISSORS
#
#   how the round needs to end
#   X = you lose
#   Y = you draw
#   Z = you win
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
# PART B QUESTION:
#   CALCULATE HOW MAY POINTS YOU WILL GET


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


def get_winner(contestant):
    if contestant.loses_against == "rock":
        return rock
    if contestant.loses_against == "paper":
        return paper
    if contestant.loses_against == "scissors":
        return scissors


def get_loser(contestant):
    if contestant.wins_against == "rock":
        return rock
    if contestant.wins_against == "paper":
        return paper
    if contestant.wins_against == "scissors":
        return scissors


you = {
    "A": rock,
    "B": paper,
    "C": scissors,
}

me = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


my_scores = []
with open("day_02/input.txt") as file:
    for line in file:
        text = line.strip()
        your_choice = you[text[0]]
        outcome = me[text[-1]]
        if outcome == "draw":
            my_choice = your_choice
        elif outcome == "lose":
            my_choice = get_loser(your_choice)
        elif outcome == "win":
            my_choice = get_winner(your_choice)
        result = my_choice.compete_with(your_choice)
        my_scores.append(result)

print("Answer: ", sum(my_scores))
# correct answer:14204
