with open ('mike/day1_input.txt') as file:
    # Input
    input = [x for x in file.read().splitlines()]

    # Part 1

    
    def get_first_and_last(input):
        answers = []
        running_total = 0

        for i in range(len(input)):
            answers.append("")
            for character in input[i]:
                if character.isdigit():
                    answers[i] += character
            answers[i] = answers[i][0] + answers[i][-1]
            running_total += int(answers[i])

        return(running_total)
    
    print(get_first_and_last(input))
   