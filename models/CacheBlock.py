class CacheBlock:
    def __init__(self, number, state, address, data):
        self.number = number
        self.state = state
        self.address = address
        self.data = data

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def check_empty(self):
        return self.address == 0 and self.data == 0 and self.state == "I"
