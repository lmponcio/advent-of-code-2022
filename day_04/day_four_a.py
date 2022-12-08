# Input = List of all the items in each rucksack
#   each section an ID number
#   each Elf assigned a range of section IDs
#   many assignments overlap
# PART A QUESTION:
#   In how many assignment pairs does one range fully contain the other?


def fully_contains(parent, child):
    for child_element in child:
        if child_element not in parent:
            return False
    return True


fully_contains_counter = 0
with open("day_04/input.txt") as file:
    for line in file:
        line = line.strip()
        pair = line.split(",")
        elf_one = pair[0].split("-")
        elf_two = pair[1].split("-")
        elf_one = [int(x) for x in elf_one]
        elf_two = [int(x) for x in elf_two]
        elf_one = list(range(elf_one[0], elf_one[1] + 1))
        elf_two = list(range(elf_two[0], elf_two[1] + 1))

        if fully_contains(elf_one, elf_two) or fully_contains(elf_two, elf_one):
            fully_contains_counter += 1


print("Answer:", fully_contains_counter)
# correct answer: 567
