number_of_gains = 0
def square(number):
    if not 1 <= number <= 64 :
        raise ValueError("square must be between 1 and 64")

    return pow(2,number -1)

def total():
    total_gains = 0
    for i in range(1,65):
        total_gains += square(i)
    return total_gains
