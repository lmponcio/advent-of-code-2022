# Input = datastream buffer
#   handheld device - communication system
#   malfunctioning
#   lock onto their signal - seemingly random characters (one at the time)
#   detect start of packet marker in the datastream: sequence of 4 characters all different
# PART A QUESTION:
#   How many characters need to be processed before the first start-of-packet marker is detected?


def check_marker(data, start):
    chars = list(data[start : start + 4])
    if len([*set(chars)]) == 4:
        return True
    else:
        return False


with open("day_06/input.txt") as file:
    data = file.readline()


for start_char in range(len(data) - 3):
    marker_found = check_marker(data, start_char)
    if marker_found:
        result = start_char + 4
        break

print("Answer:", result)
# correct answer:1965
