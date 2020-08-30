

def arithmetic_arranger(problems):

    for numbers in problems:
        if numbers.find('+') != -1:
            location = numbers.find('+')
            distance = (5-location)*" "
            print(distance, numbers[:location],'\n', numbers[location:], '\n-----','\n\n\n\n')
        elif numbers.find('-') != -1:
            location =  numbers.find('-')
            distance = (5-location)*" "
            print(distance, numbers[:location],'\n', numbers[location:], '\n-----','\n\n\n\n')
        elif numbers.find('*') != 1:
            print("Error: Operator must be '+' or '-'.")
        elif numbers.find('/') != 1:
            print("Error: Operator must be '+' or '-'.")


    # return arranged_problems
