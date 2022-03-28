from MemoryBlock import MemoryBlock


class Memory:
    def __init__(self):
        self.block_0 = MemoryBlock(0, 0)
        self.block_1 = MemoryBlock(1, 0)
        self.block_2 = MemoryBlock(2, 0)
        self.block_3 = MemoryBlock(3, 0)
        self.block_4 = MemoryBlock(4, 0)
        self.block_5 = MemoryBlock(5, 0)
        self.block_6 = MemoryBlock(6, 0)
        self.block_7 = MemoryBlock(7, 0)

    # Read data from memory address
    def read(self, address):
        match address:
            case 0:
                result = self.block_0.get_data()
            case 1:
                result = self.block_1.get_data()
            case 2:
                result = self.block_2.get_data()
            case 3:
                result = self.block_3.get_data()
            case 4:
                result = self.block_4.get_data()
            case 5:
                result = self.block_5.get_data()
            case 6:
                result = self.block_6.get_data()
            case 7:
                result = self.block_7.get_data()
            case _:
                result = -1
        return result

    # Write data to memory address
    def write(self, address, data):
        match address:
            case 0:
                self.block_0.set_data(data)
            case 1:
                self.block_1.set_data(data)
            case 2:
                self.block_2.set_data(data)
            case 3:
                self.block_3.set_data(data)
            case 4:
                self.block_4.set_data(data)
            case 5:
                self.block_5.set_data(data)
            case 6:
                self.block_6.set_data(data)
            case 7:
                self.block_7.set_data(data)
            case _:
                return -1
