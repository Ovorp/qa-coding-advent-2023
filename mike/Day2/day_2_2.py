import re

with open ('mike/day2/day2_input.txt') as file:
    # Input
    input = [x for x in file.read().splitlines()]

    game_ids = []
    running_total = 0

    # Split game header and cube color/amount pairs
    games = [(re.split(': |, |; ', x)) for x in input]
    
    # Iterate through each game
    for game in games:
        COLORS = {'red':0, 'green':0, 'blue':0}
        index = 0

        # Iterate through each element of a game
        for item in game:
            index += 1
            # If the element does not contain a color, it is the game id
            if item.split(' ')[-1] not in COLORS:
                game_id = item
                continue
            
            pair = item.split(' ')
            amount = int(pair[0])
            color = pair[-1]

            if amount > COLORS.get(color):
                COLORS.update({color:amount})

            if index == len(game):        
                totals = list(COLORS.values())
                power = 1
                for total in totals:
                    power *= total
                running_total += power
                              
    print(running_total)
