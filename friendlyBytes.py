from decimal import Decimal


# The function accepts values, some of which are optional
def friendly_bytes(num, decimals=2, binary=False, keep_width=False):
    # Definition of a dictionary containing the sizes
    sizes = {
        0: '',
        1: 'K',
        2: 'M',
        3: 'G',
        4: 'T',
        5: 'P',
        6: 'E',
        7: 'Z',
        8: 'Y',
    }

    base = 1024 if binary else 1000
    i = 0
    # Dividing the number in the base
    while (num) > base:
        num = num / base
        i += 1

    # The desired measure according to i
    size = f"{sizes[i]}iB" if binary and i else f"{sizes[i]}B"

    # Sending the number to the round function
    # The function accepts a long number and the desired length
    # and returns the rounded number
    myNum = round(num, decimals)


    # In case keep_width = TRUE
    if keep_width == True:
        str_num = str(num)
        # Finding the position of the decimal point
        fp_idx = str_num.find('.')
        num_len = len(str_num)
        difference = num_len - (fp_idx + 1)
        # Checking whether the number of places after the decimal point corresponds to decimals
        # If there is a difference in length, we will add zeros
        if difference != decimals:
            decimals_difference = decimals - difference
            for j in range(0,decimals_difference,1):
             str_num = str_num + '0'
        myNum = str_num


    return f"{myNum} {size}"


returnValue = friendly_bytes(1.222, decimals=4,keep_width=True)
print(returnValue)
