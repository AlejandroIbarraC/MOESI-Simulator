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

    # Find instances of CPUs that have a copy of desired address
    def find_copies(self, address, cpu_number):
        result = []

        for cpu in self.cpus:
            # Don't include CPU that is making the update request. It already updated its own cache!
            if cpu.number != cpu_number and cpu.controller.find_data(address, boolean=True):
                result.append(cpu)

        print("BUS: REQ FROM CPU " + str(cpu_number) + ": FOUND COPIES " + str(result))

        return result

    # Bus can only be used by one instance at a time. Call this to lock.
    def lock_bus(self):
        self.lock.acquire()

    # Bus reads a data from memory
    def read_from_mem(self, address, cpu_number):
        result = self.memory.read(address)
        print("BUS: REQ FROM CPU " + str(cpu_number) + ": READING " + str(address) + " FROM MEMORY")
        return result

    # Unlock bus to be used by another instance
    def unlock_bus(self):
        self.lock.release()

    # Updates all processors depending on signal
    def update(self, address, cpu_list, update_type, cpu_number):
        for cpu in cpu_list:
            print("BUS: REQ FROM CPU " + str(cpu_number) + ": UPDATING CPU: " + str(cpu.number) + " ADDRESS: " + str(address) + " TYPE: " + str(update_type))
            block = cpu.controller.cache.get_block_by_address(address)
            match update_type:
                case "RHP":
                    # Change copy E -> S and M -> O
                    block_state = block.get_state()
                    match block_state:
                        case "E":
                            block.set_state("S")
                        case "M":
                            block.set_state("O")
                case "WM":
                    # Change all copies to I
                    block.set_state("I")

    # Write to memory from bus
    def write_to_mem(self, address, data, cpu_number):
        self.memory.write(address, data)
        print("BUS: REQ FROM CPU " + str(cpu_number) + ": WRITING " + str(data) + " TO ADDRESS " + str(address))


