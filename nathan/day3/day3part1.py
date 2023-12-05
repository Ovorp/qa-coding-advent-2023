input = open('inputDay3.txt', 'r').read().split('\n')
# input = open('testInput.txt', 'r').read().split('\n')
directions = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]



grid = []

for line in input:
    grid.append(list(line))


def turnIntoNumber(digits):
    return int(''.join(digits))


def findSum(grid):
    max_row = len(grid[0])
    max_column = len(grid)
    sum = 0

    for column in range(max_column):
        is_adjacent = False
        digits = []

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

                        if not is_adjacent and currentItem != '.' and not currentItem.isdigit():
                            is_adjacent = True
                            break
            
            else:
                if is_adjacent:
                    sum += turnIntoNumber(digits)
                    print(sum)
                digits = []
                is_adjacent = False

        if is_adjacent:
            sum += turnIntoNumber(digits)
         

    return sum

# print(findSum(grid))

findSum(grid)