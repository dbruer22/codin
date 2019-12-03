# this is not my code full credit to Nate Jenson
def string_conversion(number):
    total = 0                             # this is where we accumulate the result
    pwr = len(number) - 1                 # start the exponent off as 2
    for digit in number:                  # digit is the str "5", "4", and "6"
        digitVal = ord(digit) - ord('0')  # using the ascii table, digitVal is the int value of 5,4, and 6.
                                          # add 500, then 40, then 6
        #pwr -= 1                          # make sure to drop the exponent down by one each time
    return total
