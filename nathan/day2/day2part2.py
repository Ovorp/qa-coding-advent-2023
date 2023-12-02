input = open('inputDay2.txt', 'r').read().split('\n')

from day2part1 import createDataStructure as createDataStructure

games = createDataStructure(input)


def sumOfPowers(list):
    powerList = []

    for items in list:
        powerList.append(powers(items))
        

    return print('the sum of the powers is', sum(powerList))


def powers(list):
    red = 0
    green = 0
    blue = 0
    for items in list:
        if items[0] == 'red' and items[1] > red:
            red = items[1]
        if items[0] == 'green' and items[1] > green:
            green = items[1]
        if items[0] == 'blue' and items[1] > blue:
            blue = items[1]

    return (red * green * blue)

sumOfPowers(games)