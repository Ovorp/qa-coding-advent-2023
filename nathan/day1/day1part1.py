input = open('inputDay1.txt', 'r').read().split('\n')

def findSumOf(cordinates):
    pairs = []
    for line in cordinates:
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in line[::-1]:
            if char.isdigit():
                last_digit = char
                break
        pairs.append(int(first_digit + last_digit))
    return sum(pairs)

answer = findSumOf(input)
print('The sum of all the calibration values = ',  answer)