import threading
import time

from Controller import Controller
import util.InstructionGenerator as Gen


class CPU:
    def __init__(self, number):
        self.number = number
        self.controller = Controller(self.number)
        self.is_running = False
        self.instr_time = 1

        self.status = "Idle"
        self.last_instr = " - "
        self.custom_instr = ""

    # Analyzes string instruction and converts it to list format
    def analyze_instruction(self, instr):
        first_char = instr[0]

        match first_char:
            case "R":
                address = int(instr[5:], 2)
                result = ["READ", address]
            case "W":
                address = int(instr[6:9], 2)
                data = int(instr[10:], 16)
                result = ["WRITE", address, data]
            case "C":
                result = ["CALC"]
            case _:
                result = []

        return result

    def get_controller(self):
        return self.controller

    # Called by the thread when in continuous execution mode
    def thread_handler(self):
        while self.is_running:
            self.thread_clock()

    # Called by the thread when in single step mode
    def thread_handler_single_step(self):
        self.thread_clock()

    # Thread function to be called once if single step is active
    def thread_clock(self):
        # Check if a custom instruction is introduced to execute it first
        if self.custom_instr == "":
            instr = Gen.generate_random_instruction()
        else:
            instr = self.custom_instr
            self.custom_instr = ""

        # Decode instruction
        decoded_instr = self.analyze_instruction(instr)

        # Update object variables
        self.last_instr = self.status
        self.status = instr

        # Determine if instruction was successfully decoded
        if len(decoded_instr) > 0:
            operation = decoded_instr[0]
            if operation == "CALC":
                # Do nothing
                print("CPU " + str(self.number) + ": DECODED CALC")
            elif operation == "READ":
                # Call the controller READ operation
                address = decoded_instr[1]
                print("CPU " + str(self.number) + ": DECODED READ " + str(address))
                self.controller.read(address)
            else:
                # Call the controller WRITE operation
                address = decoded_instr[1]
                data = decoded_instr[2]
                print("CPU " + str(self.number) + ": DECODED WRITE " + str(address) + " " + str(data))
                self.controller.write(address, data)
            time.sleep(self.instr_time)
        else:
            print("CPU: " + str(self.number) + ": ERROR DECODING " + str(instr))

    # Main entry point to start CPU
    def play(self, single_step=False):
        if not self.is_running:
            if not single_step:
                # Check for single step mode
                self.is_running = True
                engine = threading.Thread(target=self.thread_handler, daemon=True)
            else:
                engine = threading.Thread(target=self.thread_handler_single_step, daemon=True)

            engine.start()
        else:
            print("CPU " + str(self.number) + " is already running!")

    def set_custom_instr(self, instr):
        self.custom_instr = instr

    def set_instr_time(self, num):
        self.instr_time = float(num)

    # Stops CPU execution
    def stop(self):
        if self.is_running:
            self.is_running = False
        else:
            print("CPU " + str(self.number) + " is already stopped!")

