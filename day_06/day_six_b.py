# Input = datastream buffer
#   handheld device - communication system
#   malfunctioning
#   lock onto their signal - seemingly random characters (one at the time)
#   detect start of packet marker in the datastream: sequence of 4 characters all different
# PART A QUESTION:
#   How many characters need to be processed before the first start-of-packet marker is detected?

marker_length = 14


def check_marker(data, start, length):
    chars = list(data[start : start + length])
    if len([*set(chars)]) == length:
        return True
    else:
        return False


with open("day_06/input.txt") as file:
    data = file.readline()


for start_char in range(len(data) - 3):
    marker_found = check_marker(data, start_char, marker_length)
    if marker_found:
        result = start_char + marker_length
        break

print("Answer:", result)
# correct answer:2773
