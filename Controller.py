import time

from Bus import Bus
from Cache import Cache


class Controller:
    def __init__(self, cpu_number):
        self.cache = Cache()
        self.bus = Bus()
        self.cpu_number = cpu_number

    # Checks to see if data is in cache in a valid state
    def find_data(self, address, boolean=False):
        if address % 2 == 0:
            a_list = [self.cache.get_block(0), self.cache.get_block(1)]
        else:
            a_list = [self.cache.get_block(2), self.cache.get_block(3)]
        result = False

        for a in a_list:
            if a.get_address() == address and a.get_state() != "I":
                # Check if address matches and line not in invalid state
                if boolean:
                    # Boolean mode for bus checking copies
                    result = True
                else:
                    result = a.get_data()

        return result

    # Handle read operation
    def read(self, address):
        cache_check = self.find_data(address, boolean=True)
        if cache_check:
            # READ HIT. Data was found on local blocks
            print("CPU " + str(self.cpu_number) + ": READ HIT")
            time.sleep(0.5)
        else:
            # READ MISS. Call bus to get data from somewhere else
            print("CPU " + str(self.cpu_number) + ": READ MISS. PROBING...")
            self.bus.lock_bus()
            cpus_with_copy = self.bus.find_copies(address, self.cpu_number)
            if len(cpus_with_copy) != 0:
                # READ HIT ON PROBE
                print("CPU " + str(self.cpu_number) + ": READ HIT ON PROBE")
                cpu = cpus_with_copy[0]
                data = cpu.controller.find_data(address)
                old_info = self.cache.write(address, data, "S")

                # Update all copies with READ HIT PROBE code
                self.bus.update(address, cpus_with_copy, "RHP", self.cpu_number)
            else:
                # READ MISS ON PROBE. READ FROM MEMORY
                print("CPU " + str(self.cpu_number) + ": READ MISS ON PROBE. READ FROM MEMORY.")
                data = self.bus.read_from_mem(address, self.cpu_number)
                old_info = self.cache.write(address, data, "E")

            # Verify that old info is not invalid and write back to memory
            old_state = old_info[0]
            old_address = old_info[1]
            old_data = old_info[2]

            if old_address != address and old_state == "O" or old_state == "M":
                # Only write back if state is O or M and expulsion is made
                self.bus.write_to_mem(old_address, old_data, self.cpu_number)

            self.bus.unlock_bus()

    # Handle write operation
    def write(self, address, data):
        cache_check = self.find_data(address, boolean= True)
        if cache_check:
            state = self.cache.get_state_by_address(address)
            old_info = [-1]

            self.bus.lock_bus()
            if state == "E":
                print("WRITE HIT")
                # E -> M then WRITE
                state = "M"
                old_info = self.cache.write(address, data, state)
            elif state == "M":
                # M stays in M. Just write
                print("WRITE HIT")
                old_info = self.cache.write(address, data, state)
            elif state == "S" or state == "O":
                print("WRITE MISS")
                # S or O -> M. WRITE on local cache. Tell bus to change copies to I
                state = "M"
                old_info = self.cache.write(address, data, state)
                cpus_with_copy = self.bus.find_copies(address, self.cpu_number)
                self.bus.update(address, cpus_with_copy, "WM", self.cpu_number)

            # Verify that old info is not invalid and write back to memory
            old_state = old_info[0]
            old_address = old_info[1]
            old_data = old_info[2]

            if old_address != address and old_state == "O" or old_state == "M":
                # Only write back if state is O or M and expulsion is made
                self.bus.write_to_mem(old_address, old_data, self.cpu_number)

            self.bus.unlock_bus()

        else:
            # Address is not in local cache
            # Throw someone away from local cache. Check if we need to write back (M or O)
            state = "M"

            self.bus.lock_bus()
            old_info = self.cache.write(address, data, state)

            old_state = old_info[0]
            old_address = old_info[1]
            old_data = old_info[2]

            if old_address != address and old_state == "O" or old_state == "M":
                # Only write back if state is O or M and expulsion is made
                self.bus.write_to_mem(old_address, old_data, self.cpu_number)

            # Invalidate all other copies
            cpus_with_copy = self.bus.find_copies(address, self.cpu_number)
            self.bus.update(address, cpus_with_copy, "WM", self.cpu_number)

            self.bus.unlock_bus()
