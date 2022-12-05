# Input = List of all the items in each rucksack
#    loading rucksacks w supples
#    items need to be rearranged
#    1 rucksack, 2 large comparments
#        all items of a given type (represented by one letter only) go into exactly one of the two compartments
#        he failed in 1 item per rucksack
#        item type identified by a SINGLE LOWERCASE OR UPPERCASE
#            a and A are two different items
#        first half of letters is the first compartment, second the second
#        a-z priority 1-26
#        A-Z priority 27-52
#
#    elfs divided in groups of three
#    each elf has a badge that identifies the group
#    THE BADGE IS:the only item type carried by all three elfs (the badge will be "somehwere in the racksack")
#
# B BART B QUESTION:
#   Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

import string

# creating priority dict
items_priority = {}
letters_low = list(string.ascii_lowercase)
for letter in letters_low:
    items_priority[letter] = ord(letter) - 96
letters_upp = list(string.ascii_uppercase)
for letter in letters_upp:
    items_priority[letter] = ord(letter) - 38


def find_badge(elf_group):
    elf_one = elf_group[0]
    elf_two = elf_group[1]
    elf_three = elf_group[2]
    duplicate_items = []
    for item in elf_one:
        if item in elf_two and item in elf_three:
            duplicate_items.append(item)
    duplicate_items = [*set(duplicate_items)]
    if len(duplicate_items) == 1:
        return duplicate_items[0]
    else:
        raise Exception("More than one badge in the group: %s", duplicate_items)


elf_no = 0
elf_group = []
priority_values = []
with open("day_03/input.txt") as file:
    for line in file:
        elf_no += 1
        this_elf = line.strip()
        elf_group.append(this_elf)
        if elf_no == 3:
            priority_values.append(items_priority[find_badge(elf_group)])
            elf_group = []
            elf_no = 0

print("Answer: ", sum(priority_values))
# correct answer:2569
