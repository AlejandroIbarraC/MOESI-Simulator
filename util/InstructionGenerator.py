import random

from util.Util import *


# Calculates a random number using binomial distribution
def binomial_random(n, p):
    x = 0
    i = 0
    while i < n:
        if random.random() < p:
            x += 1
        i += 1

    return x


# Generates read instruction as string from address
def generate_read(p_number, address):
    address = dec_to_bin(address)
    result = "P" + str(p_number) + ": READ " + address
    return result


# Generates write instruction as string from address and data
def generate_write(p_number, address, data):
    address = dec_to_bin(address)
    data = dec_to_hex(data)
    result = "P" + str(p_number) + ": WRITE " + address + ";" + data
    return result


# Generates calc instruction as string from processor
def generate_calc(p_number):
    result = "P" + str(p_number) + ": CALC"
    return result


# Generates random instruction for processor as string
def generate_random_instruction():
    ins_type = binomial_random(2, 0.5)
    p_number = binomial_random(3, 0.5)

    match ins_type:
        case 0:
            # Read instruction
            address = binomial_random(7, 0.5)
            result = generate_read(p_number, address)
        case 1:
            # Write instruction
            address = binomial_random(7, 0.5)
            data = binomial_random(65535, 0.5)
            result = generate_write(p_number, address, data)
        case 2:
            # Calc instruction
            result = generate_calc(p_number)
        case _:
            result = "ERROR"

    return result[4:]
