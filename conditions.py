""" a simple program to return sum of positive integers less than the input but divisible by 3 or 5 """

# take input

def Solution(number):
    # empty list
    answers = []
    
    # loop through numbers in range
    for i in range(number):
        
        # test positive integers in range for divisibility by 3 or 5 (or NOT AND, include the ones divisible by both only once!)
        if (i%3==0 or i%5==0) and i < number and i > 0:
            # add to the empty list 
            answers.append(i)
    # return sum
    return sum(answers)
