# Input = drawing of the starting stacks of crates and the rearrangement procedure
#   stacks of crates
#   crates to be rearranged (needed supplies buried)
#   giant cargo crane: moves crates between stacks
#   after the crates are rearranged, desired crates to be at top of EACH STACK
#   don't know which crate will end up where
#   crates are moved ONE AT THE TIME
# PART A QUESTION:
#   which crate will end up on top of each stack

# # test purposes
# stack_positions = [1 + x * 4 for x in range(3)]
# stacks = [[] for x in range(3)]

stack_positions = [1 + x * 4 for x in range(9)]
stacks = [[] for x in range(9)]
with open("day_05/input.txt") as file:
    line_no = 0
    for line in file:
        # first I gather the stacks into a list of lists (interpret the drawing)
        if "[" in line:
            for col_value in stack_positions:
                if line[col_value] != " ":
                    this_stack = line[col_value]
                    stack_no = stack_positions.index(col_value) + 1
                    stacks[stack_no - 1].append(this_stack)
        # once finished (line 10), I reorder them, to be able to work
        elif "" == line.strip():
            for index in range(len(stacks)):
                stacks[index].reverse()
        # finally, I follow the instructions of the input
        elif line.startswith("move"):
            line = line.strip()
            line = line.split(" ")
            amount = int(line[1])
            src = int(line[3]) - 1
            dst = int(line[-1]) - 1
            for _ in range(amount):
                stacks[dst].append(stacks[src].pop())

result = []
for stack in stacks:
    result.append(stack[-1])
print("Answer:", "".join(result))
# correct answer: MQSHJMWNH
