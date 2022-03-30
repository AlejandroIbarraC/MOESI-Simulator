from CacheBlock import CacheBlock
from InstructionGenerator import *


class Cache:
    def __init__(self):
        self.block_0 = CacheBlock(0, "I", 0, 0)
        self.block_1 = CacheBlock(1, "I", 0, 0)
        self.block_2 = CacheBlock(2, "I", 0, 0)
        self.block_3 = CacheBlock(3, "I", 0, 0)
        self.blocks = [self.block_0, self.block_1, self.block_2, self.block_3]

    # Get block by number
    def get_block(self, number):
        match number:
            case 0:
                result = self.block_0
            case 1:
                result = self.block_1
            case 2:
                result = self.block_2
            case 3:
                result = self.block_3
            case _:
                result = -1
        return result

    # Get block by address
    def get_block_by_address(self, address):
        for block in self.blocks:
            if block.address == address:
                return block

    # Get state by address
    def get_state_by_address(self, address):
        for block in self.blocks:
            if block.address == address:
                return block.get_state()

    # Writes on cache using random replacement policy and 2-way associativity
    def write(self, address, data, state):
        old_info = [-1]
        if address % 2 == 0:
            # Address is even
            if self.block_0.check_empty() or self.block_0.get_address() == address:
                old_info = [self.block_0.get_state(), self.block_0.address, self.block_0.get_data()]
                self.block_0.set_state(state)
                self.block_0.set_address(address)
                self.block_0.set_data(data)
            elif self.block_1.check_empty() or self.block_1.get_address() == address:
                old_info = [self.block_1.get_state(), self.block_1.address, self.block_1.get_data()]
                self.block_1.set_address(address)
                self.block_1.set_data(data)
                self.block_1.set_state(state)
            else:
                b_random = binomial_random(1, 0.5)
                match b_random:
                    case 0:
                        old_info = [self.block_0.get_state(), self.block_0.address, self.block_0.get_data()]
                        self.block_0.set_address(address)
                        self.block_0.set_data(data)
                        self.block_0.set_state(state)
                    case 1:
                        old_info = [self.block_1.get_state(), self.block_1.address, self.block_1.get_data()]
                        self.block_1.set_address(address)
                        self.block_1.set_data(data)
                        self.block_1.set_state(state)
        else:
            # Address is odd
            if self.block_2.check_empty() or self.block_2.get_address() == address:
                old_info = [self.block_2.get_state(), self.block_2.address, self.block_2.get_data()]
                self.block_2.set_address(address)
                self.block_2.set_data(data)
                self.block_2.set_state(state)
            elif self.block_3.check_empty() or self.block_3.get_address() == address:
                old_info = [self.block_3.get_state(), self.block_3.address, self.block_3.get_data()]
                self.block_3.set_address(address)
                self.block_3.set_data(data)
                self.block_3.set_state(state)
            else:
                b_random = binomial_random(1, 0.5)
                match b_random:
                    case 0:
                        old_info = [self.block_2.get_state(), self.block_2.address, self.block_2.get_data()]
                        self.block_2.set_address(address)
                        self.block_2.set_data(data)
                        self.block_2.set_state(state)
                    case 1:
                        old_info = [self.block_3.get_state(), self.block_3.address, self.block_3.get_data()]
                        self.block_3.set_address(address)
                        self.block_3.set_data(data)
                        self.block_3.set_state(state)
        return old_info
