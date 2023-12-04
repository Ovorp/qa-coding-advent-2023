import re

with open ('mike/day2/day2_input.txt') as file:
    # Input
    input = [x for x in file.read().splitlines()]

    game_ids = []

    COLORS = {'red':12, 'green':13, 'blue':14}
    running_total = 0
    possible = False

    # Split game header and cube color/amount pairs
    games = [(re.split(': |, |; ', x)) for x in input]
    
    # Iterate through each game
    for game in games:

        # If each cube amount is possible, extract the game id and contribute to running total. This will not be triggered before the first game is observed
        if possible:
            running_total += int(game_id.split(' ')[-1])
        else:
            possible = True
        
        # Iterate through each element of a game
        for item in game:

            # If the element does not contain a color, it is the game id
            if item.split(' ')[-1] not in COLORS:
                game_id = item
                continue
            
            item = item.split(' ')
            amount = int(item[0])
            color = item[-1]
            
            # Compare the cube amount to the associated maximum. If it is less or equal, move onto next element. If it is more, disqualify the game and move to the next one
            if amount <= COLORS.get(color):
                possible = True
                continue
            else:
                possible = False
                break
                
print(running_total)
