class MemoryBlock:
    def __init__(self, address, data):
        self.data = data
        self.address = address

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
        