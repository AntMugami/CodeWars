def narcissistic( value ):
    nar_to_list = str(value)
    sum = 0
    for digit in nar_to_list:
        sum += int(digit) ** (len(nar_to_list))
    return True if sum == value else  False





print(narcissistic(371)) # TRUE
print(narcissistic(7)) # TRUE
print(narcissistic(122)) # False
print(narcissistic(4887)) # False
