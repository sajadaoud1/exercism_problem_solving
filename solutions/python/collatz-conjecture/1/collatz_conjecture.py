def steps(number):
    counter = 0
    if number > 1:
        while number != 1 :
            if number % 2 == 0:
                number = number//2
                counter+=1
            else:
                number = (number * 3) + 1 
                counter+=1
    elif number <= 0 :
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        print ("the number is already = 1 ")

    return counter
