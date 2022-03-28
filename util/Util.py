# Collection of utility functions

# Converts decimal number to binary
def dec_to_bin(num):
    # Convert number to binary string and remove 0b prefix
    result = bin(num).replace("0b", "")

    # Ensure that result is 3 bit binary string, as there are 7 possible memory positions (000 to 111)
    while len(result) < 3:
        result = "0" + result

    return result


# Converts decimal number to hexadecimal
def dec_to_hex(num):
    # Convert number to hex string and remove 0x prefix
    result = hex(num).replace("0x", "")

    # Ensure that result is 4 bit binary string, as there are 65535 possible data values to write (FFFF)
    while len(result) < 4:
        result = "0" + result

    return result
