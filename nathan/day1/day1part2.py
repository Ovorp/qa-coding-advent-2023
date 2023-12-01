# Tried with regex. It did not work.  Had some bugs on edge cases

# import re

# words2nums = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
#     '1': '1',
#     '2': '2',
#     '3': '3',
#     '4': '4',
#     '5': '5',
#     '6': '6',
#     '7': '7',
#     '8': '8',
#     '9': '9'
# }

# input = open('inputDay1.txt', 'r').read().split('\n')

# def findSumOfpart2(cordinates):
#     pairs = []
#     for line in cordinates:
#         all_digits = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', line, flags=re.IGNORECASE)
#         # first_digit = words2nums[all_digits[0]]
#         # last_digit = words2nums[all_digits[-1]]
#         # print(first_digit, last_digit)
#         print(all_digits)
#     #     print(line, first_digit, last_digit)
#     #     pairs.append(int(first_digit + last_digit))
#     # return sum(pairs)

# answer = findSumOfpart2(['28gtbkszmrtmnineoneightmx'])
# print('The sum of all the calibration values = ',  answer)


input = open('inputDay1.txt', 'r').read().split('\n')

def replaceWords(str): 
    return str.replace('one', 'o1ne').replace('two', 't2wo').replace('three', 't3hree').replace('four', 'f4our').replace('five', 'f5ive').replace('six', 's6ix').replace('seven', 's7even').replace('eight', 'e8ight').replace('nine', 'n9ine')


def findSumOfpart2(cordinates):
    pairs = []
    for line in cordinates:
        newLine = replaceWords(line)
        first_digit = None
        last_digit = None
        for char in newLine:
            if char.isdigit():
                first_digit = char
                break
        for char in newLine[::-1]:
            if char.isdigit():
                last_digit = char
                break
        pairs.append(int(first_digit + last_digit))
    return sum(pairs)

answer = findSumOfpart2(input)
print('The sum of all the calibration values = ',  answer)