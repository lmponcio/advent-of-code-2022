# Input = List of all the items in each rucksack
#   each section an ID number
#   each Elf assigned a range of section IDs
#   many assignments overlap
# PART A QUESTION:
#   In how many assignment pairs do the ranges overlap?


def overlaps(elf_one, elf_two):
    for section in elf_one:
        if section in elf_two:
            return True
    return False


overlaps_counter = 0
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

        if overlaps(elf_one, elf_two):
            overlaps_counter += 1


print("Answer:", overlaps_counter)
# correct answer: 907
