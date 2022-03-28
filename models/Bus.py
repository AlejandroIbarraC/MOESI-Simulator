import threading

from Memory import *


class Bus:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Bus, cls).__new__(cls)
            cls.lock = threading.Lock()
            cls.memory = Memory()
            cls.cpus = []

        return cls._instance

    # Finds instances of CPUs that have a copy of desired address
    def find_copies(self, address):
        result = []

        for cpu in self.cpus:
            if cpu.controller.find_data(address, boolean=True):
                result.append(cpu)

        print("FOUND COPIES " + str(self.cpus))

        return result

    # Bus can only be used by one instance at a time. Call this to lock.
    def lock_bus(self):
        self.lock.acquire()

    # Bus reads a data from memory
    def read_from_mem(self, address):
        result = self.memory.read(address)
        return result

    # Unlock bus to be used by another instance
    def unlock_bus(self):
        self.lock.release()

    # Updates all processors depending on signal
    def update(self, address, cpu_list, update_type):
        for cpu in cpu_list:
            print("Updating CPU: " + str(cpu.number) + " memory pos: " + str(address) + " of type: " + str(update_type))
            block = cpu.controller.cache.get_block_by_address(address)
            match update_type:
                case "RHP":
                    # Change copy with E to S.
                    if block.get_state() == "E":
                        block.set_state("S")
                case "WM":
                    # Change all copies to I
                    block.set_state("I")

    # Write to memory from bus
    def write_to_mem(self, address, data):
        self.memory.write(address, data)


