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
# PART A QUESTION:
#   Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

import string

# creating priority dict
items_priority = {}
letters_low = list(string.ascii_lowercase)
for letter in letters_low:
    items_priority[letter] = ord(letter) - 96
letters_upp = list(string.ascii_uppercase)
for letter in letters_upp:
    items_priority[letter] = ord(letter) - 38


def find_duplicate(comp_one, comp_two):
    duplicate_items = []
    for item_c_one in comp_one:
        for item_c_two in comp_two:
            if item_c_one == item_c_two:
                duplicate_items.append(item_c_one)
    duplicate_items = [*set(duplicate_items)]
    if len(duplicate_items) == 1:
        return duplicate_items[0]
    else:
        raise Exception("More than one duplicate in a rucksack")


priority_values = []
with open("day_03/input.txt") as file:
    for line in file:
        line = line.strip()
        length = len(line)
        half_length = int(length / 2)
        # first_half_length = int(round(length / 2, 0))
        # second_half_length = length - first_half_length
        # print("half lengths: ", first_half_length, second_half_length)
        comp_one = line[:half_length]
        comp_two = line[-half_length:]
        # print(comp_one)
        # print(comp_two)
        duplicate = find_duplicate(comp_one, comp_two)
        # print(duplicate)
        # print(items_priority[duplicate])
        priority_values.append(items_priority[duplicate])


print("Answer: ", sum(priority_values))
# correct answer: 7763
