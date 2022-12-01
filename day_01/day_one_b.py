# Input = Number of Calories each elf is carrying (same as previous)
#   one item per line
#   each elf inventory separated by a blank line
# PART TWO QUESTION:
#   calories carried by the top three elves


class Elf:
    def __init__(self) -> None:
        self.food = []

    def add_food(self, new_food):
        self.food.append(new_food)

    def get_total_calories(self):
        return sum(self.food)


calories_per_elf = []
with open("day_one_a_input.txt") as file:
    this_elf = Elf()
    for line in file:
        text = line.strip()
        if text == "":
            calories_per_elf.append(this_elf.get_total_calories())
            this_elf = Elf()
        else:
            this_elf.add_food(int(text))

calories_per_elf.sort()

print("Top three elf calories: ", sum(calories_per_elf[-3:]))
# correct answer: 197301
