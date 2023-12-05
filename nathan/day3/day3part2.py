input = open('inputDay3.txt', 'r').read().split('\n')
# input = open('/home/nshirts/Documents/advent2023/qa-coding-advent-2023/nathan/day3/testInput.txt', 'r').read().split('\n')
directions = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]
from collections import defaultdict
grid = []

for line in input:
    grid.append(list(line))


pot_gears = defaultdict(list)

def turnIntoNumber(digits):
    return int(''.join(digits))


def findSum(grid):
    max_row = len(grid[0])
    max_column = len(grid)

    for column in range(max_column):

        digits = []
        is_adjacent = []
        for row in range(max_row):
            currentItem = grid[column][row]
            

            if currentItem.isdigit():
                digits.append(currentItem)
                
                if is_adjacent:
                    continue

                for dx, dy in directions:

                    x, y = dx + row, dy + column

                    if 0 <= x < max_row and 0 <= y < max_column:
                        currentItem = grid[y][x]

                        if len(is_adjacent) == 0 and currentItem == '*':
                            is_adjacent.append((x,y))
                            break
            
            else:
                if len(is_adjacent) > 0:
                    part_number = turnIntoNumber(digits)
                    for xy in is_adjacent:
                        pot_gears[xy].append(part_number)
                digits = []
                is_adjacent = []

        if len(is_adjacent):
            part_number = turnIntoNumber(digits)
            for xy in is_adjacent:
                pot_gears[xy].append(part_number)
    


findSum(grid)

print(sum(gears[0] * gears[1] for gears in pot_gears.values() if len(gears) == 2))

# print(findSum(grid))
