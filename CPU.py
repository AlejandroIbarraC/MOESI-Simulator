import threading
import time

from Controller import Controller
import util.InstructionGenerator as Gen


class CPU:
    def __init__(self, number):
        self.controller = Controller()
        self.running = True
        self.number = number

        self.debug_instrs = ["READ 111"]
        self.status = "Idle"

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

    # Thread function to be called over and over
    def thread_clock(self):
        for instr in self.debug_instrs:
            decoded_instr = self.analyze_instruction(instr)
            self.status = instr
            if len(decoded_instr) > 0:
                operation = decoded_instr[0]
                if operation == "CALC":
                    print("Decoded CALC")
                elif operation == "READ":
                    print("Decoded READ")
                    address = decoded_instr[1]
                    self.controller.read(address)
                else:
                    print("Decoded WRITE")
                    address = decoded_instr[1]
                    data = decoded_instr[2]
                    self.controller.write(address, data)
                time.sleep(1)
            else:
                print("Error with instruction " + instr)

    # Main entry point to start CPU
    def play(self):
        engine = threading.Thread(target=self.thread_clock, daemon=True)
        engine.start()

