with open ('mike/day1_input.txt') as file:
    # Input
    input = [x for x in file.read().splitlines()]


    def replace_nums(data):
        data  = (
        data.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
        )
        return data


    def get_first_and_last(input):
        answers = []
        running_total = 0
        for i in range(len(input)):
            answers.append("")
            input[i] = replace_nums(input[i])
            for character in input[i]:
                if character.isdigit():
                    answers[i] += character
            answers[i] = answers[i][0] + answers[i][-1]
            running_total += int(answers[i])

        return(running_total)
    

    print(get_first_and_last(input))