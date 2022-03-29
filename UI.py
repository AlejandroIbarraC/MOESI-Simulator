
from tkinter import *
from tkinter import ttk

from Bus import *
from CPU import *
import util.InstructionGenerator as Gen
from util.Util import *


class UI:
    def __init__(self, master):
        # Tkinter window components
        self.master: Tk = master
        self.master.title("MOESI Simulator")
        self.master.geometry("1500x900")
        self.master.resizable(False, False)

        # Define string variables
        # Processor 0
        # Instructions
        self.p0_exec_var = StringVar()
        self.p0_exec_var.set("CurrentExec0")
        self.p0_last_exec_var = StringVar()
        self.p0_last_exec_var.set("LastExec0")
        # Cache
        # Block 0
        self.p0_c0_state_var = StringVar()
        self.p0_c0_state_var.set("P0C0State")
        self.p0_c0_address_var = StringVar()
        self.p0_c0_address_var.set("P0C0Address")
        self.p0_c0_data_var = StringVar()
        self.p0_c0_data_var.set("P0C0Data")
        # Block 1
        self.p0_c1_state_var = StringVar()
        self.p0_c1_state_var.set("P0C1State")
        self.p0_c1_address_var = StringVar()
        self.p0_c1_address_var.set("P0C1Address")
        self.p0_c1_data_var = StringVar()
        self.p0_c1_data_var.set("P0C1Data")
        # Block 2
        self.p0_c2_state_var = StringVar()
        self.p0_c2_state_var.set("P0C2State")
        self.p0_c2_address_var = StringVar()
        self.p0_c2_address_var.set("P0C2Address")
        self.p0_c2_data_var = StringVar()
        self.p0_c2_data_var.set("P0C2Data")
        # Block 3
        self.p0_c3_state_var = StringVar()
        self.p0_c3_state_var.set("P0C3State")
        self.p0_c3_address_var = StringVar()
        self.p0_c3_address_var.set("P0C3Address")
        self.p0_c3_data_var = StringVar()
        self.p0_c3_data_var.set("P0C3Data")

        # Processor 1
        # Instructions
        self.p1_exec_var = StringVar()
        self.p1_exec_var.set("CurrentExec1")
        self.p1_last_exec_var = StringVar()
        self.p1_last_exec_var.set("LastExec1")
        # Cache
        # Block 0
        self.p1_c0_state_var = StringVar()
        self.p1_c0_state_var.set("P1C0State")
        self.p1_c0_address_var = StringVar()
        self.p1_c0_address_var.set("P1C0Address")
        self.p1_c0_data_var = StringVar()
        self.p1_c0_data_var.set("P1C0Data")
        # Block 1
        self.p1_c1_state_var = StringVar()
        self.p1_c1_state_var.set("P1C1State")
        self.p1_c1_address_var = StringVar()
        self.p1_c1_address_var.set("P1C1Address")
        self.p1_c1_data_var = StringVar()
        self.p1_c1_data_var.set("P1C1Data")
        # Block 2
        self.p1_c2_state_var = StringVar()
        self.p1_c2_state_var.set("P1C2State")
        self.p1_c2_address_var = StringVar()
        self.p1_c2_address_var.set("P1C2Address")
        self.p1_c2_data_var = StringVar()
        self.p1_c2_data_var.set("P1C2Data")
        # Block 3
        self.p1_c3_state_var = StringVar()
        self.p1_c3_state_var.set("P1C3State")
        self.p1_c3_address_var = StringVar()
        self.p1_c3_address_var.set("P1C3Address")
        self.p1_c3_data_var = StringVar()
        self.p1_c3_data_var.set("P1C3Data")

        # Processor 2
        # Instructions
        self.p2_exec_var = StringVar()
        self.p2_exec_var.set("CurrentExec2")
        self.p2_last_exec_var = StringVar()
        self.p2_last_exec_var.set("LastExec2")
        # Cache
        # Block 0
        self.p2_c0_state_var = StringVar()
        self.p2_c0_state_var.set("P2C0State")
        self.p2_c0_address_var = StringVar()
        self.p2_c0_address_var.set("P2C0Address")
        self.p2_c0_data_var = StringVar()
        self.p2_c0_data_var.set("P2C0Data")
        # Block 1
        self.p2_c1_state_var = StringVar()
        self.p2_c1_state_var.set("P2C1State")
        self.p2_c1_address_var = StringVar()
        self.p2_c1_address_var.set("P2C1Address")
        self.p2_c1_data_var = StringVar()
        self.p2_c1_data_var.set("P2C1Data")
        # Block 2
        self.p2_c2_state_var = StringVar()
        self.p2_c2_state_var.set("P2C2State")
        self.p2_c2_address_var = StringVar()
        self.p2_c2_address_var.set("P2C2Address")
        self.p2_c2_data_var = StringVar()
        self.p2_c2_data_var.set("P2C2Data")
        # Block 3
        self.p2_c3_state_var = StringVar()
        self.p2_c3_state_var.set("P2C3State")
        self.p2_c3_address_var = StringVar()
        self.p2_c3_address_var.set("P2C3Address")
        self.p2_c3_data_var = StringVar()
        self.p2_c3_data_var.set("P2C3Data")

        # Processor 3
        # Instructions
        self.p3_exec_var = StringVar()
        self.p3_exec_var.set("CurrentExec3")
        self.p3_last_exec_var = StringVar()
        self.p3_last_exec_var.set("LastExec3")
        # Cache
        # Block 0
        self.p3_c0_state_var = StringVar()
        self.p3_c0_state_var.set("P3C0State")
        self.p3_c0_address_var = StringVar()
        self.p3_c0_address_var.set("P3C0Address")
        self.p3_c0_data_var = StringVar()
        self.p3_c0_data_var.set("P3C0Data")
        # Block 1
        self.p3_c1_state_var = StringVar()
        self.p3_c1_state_var.set("P3C1State")
        self.p3_c1_address_var = StringVar()
        self.p3_c1_address_var.set("P3C1Address")
        self.p3_c1_data_var = StringVar()
        self.p3_c1_data_var.set("P3C1Data")
        # Block 2
        self.p3_c2_state_var = StringVar()
        self.p3_c2_state_var.set("P3C2State")
        self.p3_c2_address_var = StringVar()
        self.p3_c2_address_var.set("P3C2Address")
        self.p3_c2_data_var = StringVar()
        self.p3_c2_data_var.set("P3C2Data")
        # Block 3
        self.p3_c3_state_var = StringVar()
        self.p3_c3_state_var.set("P3C3State")
        self.p3_c3_address_var = StringVar()
        self.p3_c3_address_var.set("P3C3Address")
        self.p3_c3_data_var = StringVar()
        self.p3_c3_data_var.set("P3C3Data")

        # Memory
        self.mem_b0_var = StringVar()
        self.mem_b0_var.set("M0")
        self.mem_b1_var = StringVar()
        self.mem_b1_var.set("M1")
        self.mem_b2_var = StringVar()
        self.mem_b2_var.set("M2")
        self.mem_b3_var = StringVar()
        self.mem_b3_var.set("M3")
        self.mem_b4_var = StringVar()
        self.mem_b4_var.set("M4")
        self.mem_b5_var = StringVar()
        self.mem_b5_var.set("M5")
        self.mem_b6_var = StringVar()
        self.mem_b6_var.set("M6")
        self.mem_b7_var = StringVar()
        self.mem_b7_var.set("M7")

        # Entries
        self.entry_instr = Entry(self.master, width=18)
        self.entry_instr.place(x=1320, y=280)

        # Combobox
        self.selected_processor = "P0"
        self.processor_cb = ttk.Combobox(self.master)
        self.processor_cb["values"] = ("P0", "P1", "P2", "P3")
        self.processor_cb.set(self.selected_processor)
        self.processor_cb.bind("<<ComboboxSelected>>", self.update_processor_cb)
        self.processor_cb["state"] = "readonly"
        self.processor_cb.configure(width=6)
        self.processor_cb.place(x=1250, y=280)

        # DEBUG ELEMENTS
        # Entries
        self.entry_instr_time = Entry(self.master, width=30)
        self.entry_instr_time.place(x=1250, y=530)

        # Variables
        self.instr_time = StringVar()
        self.instr_time.set(str(1))
        self.cpus = []
        self.bus = Bus()

        # Initialize UI
        self.init_ui()
        self.init_ui_debug()

        # Initialize CPUs
        self.init_cpus()

    def init_ui(self):
        # Font tuples
        subtitle_header_font = ("Arial", 13, "italic")
        subtitle_font = ("Arial", 11)
        var_font = ("Arial", 11, "bold")

        # Title label
        label_title = Label(self.master, text="MOESI Simulator", font=("Arial", 18))
        label_title.place(x=20, y=10)

        # Processor 0 Labels
        label_p0_title = Label(self.master, text="CPU 0", font=("Arial", 14))
        # Instructions
        label_p0_instructions_title = Label(self.master, text="Instructions:", font=subtitle_header_font)
        label_p0_exec_title = Label(self.master, text="Executing:", font=subtitle_font)
        label_p0_exec_var = Label(self.master, textvariable=self.p0_exec_var, font=var_font)
        label_p0_last_exec_title = Label(self.master, text="Last executed:", font=subtitle_font)
        label_p0_last_exec_var = Label(self.master, textvariable=self.p0_last_exec_var, font=var_font)
        # Cache
        # Block 0
        label_p0_c0_title = Label(self.master, text="L1 - Block 0:", font=subtitle_header_font)
        label_p0_c0_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p0_c0_state_var = Label(self.master, textvariable=self.p0_c0_state_var, font=var_font)
        label_p0_c0_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p0_c0_address_var = Label(self.master, textvariable=self.p0_c0_address_var, font=var_font)
        label_p0_c0_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p0_c0_data_var = Label(self.master, textvariable=self.p0_c0_data_var, font=var_font)
        # Block 1
        label_p0_c1_title = Label(self.master, text="L1 - Block 1:", font=subtitle_header_font)
        label_p0_c1_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p0_c1_state_var = Label(self.master, textvariable=self.p0_c1_state_var, font=var_font)
        label_p0_c1_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p0_c1_address_var = Label(self.master, textvariable=self.p0_c1_address_var, font=var_font)
        label_p0_c1_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p0_c1_data_var = Label(self.master, textvariable=self.p0_c1_data_var, font=var_font)
        # Block 2
        label_p0_c2_title = Label(self.master, text="L1 - Block 2:", font=subtitle_header_font)
        label_p0_c2_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p0_c2_state_var = Label(self.master, textvariable=self.p0_c2_state_var, font=var_font)
        label_p0_c2_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p0_c2_address_var = Label(self.master, textvariable=self.p0_c2_address_var, font=var_font)
        label_p0_c2_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p0_c2_data_var = Label(self.master, textvariable=self.p0_c2_data_var, font=var_font)
        # Block 3
        label_p0_c3_title = Label(self.master, text="L1 - Block 3:", font=subtitle_header_font)
        label_p0_c3_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p0_c3_state_var = Label(self.master, textvariable=self.p0_c3_state_var, font=var_font)
        label_p0_c3_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p0_c3_address_var = Label(self.master, textvariable=self.p0_c3_address_var, font=var_font)
        label_p0_c3_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p0_c3_data_var = Label(self.master, textvariable=self.p0_c3_data_var, font=var_font)

        # Place labels
        label_p0_title.place(x=20, y=50)
        # Instructions
        xi = 20
        yi = 80
        label_p0_instructions_title.place(x=xi, y=yi)
        label_p0_exec_title.place(x=xi, y=yi + 30)
        label_p0_exec_var.place(x=xi + 120, y=yi + 30)
        label_p0_last_exec_title.place(x=xi, y=yi + 60)
        label_p0_last_exec_var.place(x=xi + 120, y=yi + 60)
        # Cache
        # Block 0
        xi = 300
        label_p0_c0_title.place(x=xi, y=yi)
        label_p0_c0_state_title.place(x=xi, y=yi + 30)
        label_p0_c0_state_var.place(x=xi + 110, y=yi + 30)
        label_p0_c0_address_title.place(x=xi, y=yi + 60)
        label_p0_c0_address_var.place(x=xi + 110, y=yi + 60)
        label_p0_c0_data_title.place(x=xi, y=yi + 90)
        label_p0_c0_data_var.place(x=xi + 110, y=yi + 90)
        # Block 1
        xi = 520
        label_p0_c1_title.place(x=xi, y=yi)
        label_p0_c1_state_title.place(x=xi, y=yi + 30)
        label_p0_c1_state_var.place(x=xi + 110, y=yi + 30)
        label_p0_c1_address_title.place(x=xi, y=yi + 60)
        label_p0_c1_address_var.place(x=xi + 110, y=yi + 60)
        label_p0_c1_data_title.place(x=xi, y=yi + 90)
        label_p0_c1_data_var.place(x=xi + 110, y=yi + 90)
        # Block 2
        xi = 740
        label_p0_c2_title.place(x=xi, y=yi)
        label_p0_c2_state_title.place(x=xi, y=yi + 30)
        label_p0_c2_state_var.place(x=xi + 110, y=yi + 30)
        label_p0_c2_address_title.place(x=xi, y=yi + 60)
        label_p0_c2_address_var.place(x=xi + 110, y=yi + 60)
        label_p0_c2_data_title.place(x=xi, y=yi + 90)
        label_p0_c2_data_var.place(x=xi + 110, y=yi + 90)
        # Block 3
        xi = 960
        label_p0_c3_title.place(x=xi, y=yi)
        label_p0_c3_state_title.place(x=xi, y=yi + 30)
        label_p0_c3_state_var.place(x=xi + 110, y=yi + 30)
        label_p0_c3_address_title.place(x=xi, y=yi + 60)
        label_p0_c3_address_var.place(x=xi + 110, y=yi + 60)
        label_p0_c3_data_title.place(x=xi, y=yi + 90)
        label_p0_c3_data_var.place(x=xi + 110, y=yi + 90)

        # Processor 1 Labels
        label_p1_title = Label(self.master, text="CPU 1", font=("Arial", 14))
        # Instructions
        label_p1_instructions_title = Label(self.master, text="Instructions:", font=subtitle_header_font)
        label_p1_exec_title = Label(self.master, text="Executing:", font=subtitle_font)
        label_p1_exec_var = Label(self.master, textvariable=self.p1_exec_var, font=var_font)
        label_p1_last_exec_title = Label(self.master, text="Last executed:", font=subtitle_font)
        label_p1_last_exec_var = Label(self.master, textvariable=self.p1_last_exec_var, font=var_font)
        # Cache
        # Block 0
        label_p1_c0_title = Label(self.master, text="L1 - Block 0:", font=subtitle_header_font)
        label_p1_c0_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p1_c0_state_var = Label(self.master, textvariable=self.p1_c0_state_var, font=var_font)
        label_p1_c0_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p1_c0_address_var = Label(self.master, textvariable=self.p1_c0_address_var, font=var_font)
        label_p1_c0_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p1_c0_data_var = Label(self.master, textvariable=self.p1_c0_data_var, font=var_font)
        # Block 1
        label_p1_c1_title = Label(self.master, text="L1 - Block 1:", font=subtitle_header_font)
        label_p1_c1_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p1_c1_state_var = Label(self.master, textvariable=self.p1_c1_state_var, font=var_font)
        label_p1_c1_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p1_c1_address_var = Label(self.master, textvariable=self.p1_c1_address_var, font=var_font)
        label_p1_c1_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p1_c1_data_var = Label(self.master, textvariable=self.p1_c1_data_var, font=var_font)
        # Block 2
        label_p1_c2_title = Label(self.master, text="L1 - Block 2:", font=subtitle_header_font)
        label_p1_c2_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p1_c2_state_var = Label(self.master, textvariable=self.p1_c2_state_var, font=var_font)
        label_p1_c2_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p1_c2_address_var = Label(self.master, textvariable=self.p1_c2_address_var, font=var_font)
        label_p1_c2_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p1_c2_data_var = Label(self.master, textvariable=self.p1_c2_data_var, font=var_font)
        # Block 3
        label_p1_c3_title = Label(self.master, text="L1 - Block 3:", font=subtitle_header_font)
        label_p1_c3_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p1_c3_state_var = Label(self.master, textvariable=self.p1_c3_state_var, font=var_font)
        label_p1_c3_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p1_c3_address_var = Label(self.master, textvariable=self.p1_c3_address_var, font=var_font)
        label_p1_c3_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p1_c3_data_var = Label(self.master, textvariable=self.p1_c3_data_var, font=var_font)

        # Place labels
        label_p1_title.place(x=20, y=230)
        # Instructions
        xi = 20
        yi = 260
        label_p1_instructions_title.place(x=xi, y=yi)
        label_p1_exec_title.place(x=xi, y=yi + 30)
        label_p1_exec_var.place(x=xi + 120, y=yi + 30)
        label_p1_last_exec_title.place(x=xi, y=yi + 60)
        label_p1_last_exec_var.place(x=xi + 120, y=yi + 60)
        # Cache
        # Block 0
        xi = 300
        label_p1_c0_title.place(x=xi, y=yi)
        label_p1_c0_state_title.place(x=xi, y=yi + 30)
        label_p1_c0_state_var.place(x=xi + 110, y=yi + 30)
        label_p1_c0_address_title.place(x=xi, y=yi + 60)
        label_p1_c0_address_var.place(x=xi + 110, y=yi + 60)
        label_p1_c0_data_title.place(x=xi, y=yi + 90)
        label_p1_c0_data_var.place(x=xi + 110, y=yi + 90)
        # Block 1
        xi = 520
        label_p1_c1_title.place(x=xi, y=yi)
        label_p1_c1_state_title.place(x=xi, y=yi + 30)
        label_p1_c1_state_var.place(x=xi + 110, y=yi + 30)
        label_p1_c1_address_title.place(x=xi, y=yi + 60)
        label_p1_c1_address_var.place(x=xi + 110, y=yi + 60)
        label_p1_c1_data_title.place(x=xi, y=yi + 90)
        label_p1_c1_data_var.place(x=xi + 110, y=yi + 90)
        # Block 2
        xi = 740
        label_p1_c2_title.place(x=xi, y=yi)
        label_p1_c2_state_title.place(x=xi, y=yi + 30)
        label_p1_c2_state_var.place(x=xi + 110, y=yi + 30)
        label_p1_c2_address_title.place(x=xi, y=yi + 60)
        label_p1_c2_address_var.place(x=xi + 110, y=yi + 60)
        label_p1_c2_data_title.place(x=xi, y=yi + 90)
        label_p1_c2_data_var.place(x=xi + 110, y=yi + 90)
        # Block 3
        xi = 960
        label_p1_c3_title.place(x=xi, y=yi)
        label_p1_c3_state_title.place(x=xi, y=yi + 30)
        label_p1_c3_state_var.place(x=xi + 110, y=yi + 30)
        label_p1_c3_address_title.place(x=xi, y=yi + 60)
        label_p1_c3_address_var.place(x=xi + 110, y=yi + 60)
        label_p1_c3_data_title.place(x=xi, y=yi + 90)
        label_p1_c3_data_var.place(x=xi + 110, y=yi + 90)

        # Processor 2 Labels
        label_p2_title = Label(self.master, text="CPU 2", font=("Arial", 14))
        # Instructions
        label_p2_instructions_title = Label(self.master, text="Instructions:", font=subtitle_header_font)
        label_p2_exec_title = Label(self.master, text="Executing:", font=subtitle_font)
        label_p2_exec_var = Label(self.master, textvariable=self.p2_exec_var, font=var_font)
        label_p2_last_exec_title = Label(self.master, text="Last executed:", font=subtitle_font)
        label_p2_last_exec_var = Label(self.master, textvariable=self.p2_last_exec_var, font=var_font)
        # Cache
        # Block 0
        label_p2_c0_title = Label(self.master, text="L1 - Block 0:", font=subtitle_header_font)
        label_p2_c0_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p2_c0_state_var = Label(self.master, textvariable=self.p2_c0_state_var, font=var_font)
        label_p2_c0_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p2_c0_address_var = Label(self.master, textvariable=self.p2_c0_address_var, font=var_font)
        label_p2_c0_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p2_c0_data_var = Label(self.master, textvariable=self.p2_c0_data_var, font=var_font)
        # Block 1
        label_p2_c1_title = Label(self.master, text="L1 - Block 1:", font=subtitle_header_font)
        label_p2_c1_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p2_c1_state_var = Label(self.master, textvariable=self.p2_c1_state_var, font=var_font)
        label_p2_c1_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p2_c1_address_var = Label(self.master, textvariable=self.p2_c1_address_var, font=var_font)
        label_p2_c1_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p2_c1_data_var = Label(self.master, textvariable=self.p2_c1_data_var, font=var_font)
        # Block 2
        label_p2_c2_title = Label(self.master, text="L1 - Block 2:", font=subtitle_header_font)
        label_p2_c2_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p2_c2_state_var = Label(self.master, textvariable=self.p2_c2_state_var, font=var_font)
        label_p2_c2_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p2_c2_address_var = Label(self.master, textvariable=self.p2_c2_address_var, font=var_font)
        label_p2_c2_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p2_c2_data_var = Label(self.master, textvariable=self.p2_c2_data_var, font=var_font)
        # Block 3
        label_p2_c3_title = Label(self.master, text="L1 - Block 3:", font=subtitle_header_font)
        label_p2_c3_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p2_c3_state_var = Label(self.master, textvariable=self.p2_c3_state_var, font=var_font)
        label_p2_c3_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p2_c3_address_var = Label(self.master, textvariable=self.p2_c3_address_var, font=var_font)
        label_p2_c3_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p2_c3_data_var = Label(self.master, textvariable=self.p2_c3_data_var, font=var_font)

        # Place labels
        label_p2_title.place(x=20, y=410)
        # Instructions
        xi = 20
        yi = 440
        label_p2_instructions_title.place(x=xi, y=yi)
        label_p2_exec_title.place(x=xi, y=yi + 30)
        label_p2_exec_var.place(x=xi + 120, y=yi + 30)
        label_p2_last_exec_title.place(x=xi, y=yi + 60)
        label_p2_last_exec_var.place(x=xi + 120, y=yi + 60)
        # Cache
        # Block 0
        xi = 300
        label_p2_c0_title.place(x=xi, y=yi)
        label_p2_c0_state_title.place(x=xi, y=yi + 30)
        label_p2_c0_state_var.place(x=xi + 110, y=yi + 30)
        label_p2_c0_address_title.place(x=xi, y=yi + 60)
        label_p2_c0_address_var.place(x=xi + 110, y=yi + 60)
        label_p2_c0_data_title.place(x=xi, y=yi + 90)
        label_p2_c0_data_var.place(x=xi + 110, y=yi + 90)
        # Block 1
        xi = 520
        label_p2_c1_title.place(x=xi, y=yi)
        label_p2_c1_state_title.place(x=xi, y=yi + 30)
        label_p2_c1_state_var.place(x=xi + 110, y=yi + 30)
        label_p2_c1_address_title.place(x=xi, y=yi + 60)
        label_p2_c1_address_var.place(x=xi + 110, y=yi + 60)
        label_p2_c1_data_title.place(x=xi, y=yi + 90)
        label_p2_c1_data_var.place(x=xi + 110, y=yi + 90)
        # Block 2
        xi = 740
        label_p2_c2_title.place(x=xi, y=yi)
        label_p2_c2_state_title.place(x=xi, y=yi + 30)
        label_p2_c2_state_var.place(x=xi + 110, y=yi + 30)
        label_p2_c2_address_title.place(x=xi, y=yi + 60)
        label_p2_c2_address_var.place(x=xi + 110, y=yi + 60)
        label_p2_c2_data_title.place(x=xi, y=yi + 90)
        label_p2_c2_data_var.place(x=xi + 110, y=yi + 90)
        # Block 3
        xi = 960
        label_p2_c3_title.place(x=xi, y=yi)
        label_p2_c3_state_title.place(x=xi, y=yi + 30)
        label_p2_c3_state_var.place(x=xi + 110, y=yi + 30)
        label_p2_c3_address_title.place(x=xi, y=yi + 60)
        label_p2_c3_address_var.place(x=xi + 110, y=yi + 60)
        label_p2_c3_data_title.place(x=xi, y=yi + 90)
        label_p2_c3_data_var.place(x=xi + 110, y=yi + 90)

        # Processor 3 Labels
        label_p3_title = Label(self.master, text="CPU 3", font=("Arial", 14))
        # Instructions
        label_p3_instructions_title = Label(self.master, text="Instructions:", font=subtitle_header_font)
        label_p3_exec_title = Label(self.master, text="Executing:", font=subtitle_font)
        label_p3_exec_var = Label(self.master, textvariable=self.p3_exec_var, font=var_font)
        label_p3_last_exec_title = Label(self.master, text="Last executed:", font=subtitle_font)
        label_p3_last_exec_var = Label(self.master, textvariable=self.p3_last_exec_var, font=var_font)
        # Cache
        # Block 0
        label_p3_c0_title = Label(self.master, text="L1 - Block 0:", font=subtitle_header_font)
        label_p3_c0_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p3_c0_state_var = Label(self.master, textvariable=self.p3_c0_state_var, font=var_font)
        label_p3_c0_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p3_c0_address_var = Label(self.master, textvariable=self.p3_c0_address_var, font=var_font)
        label_p3_c0_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p3_c0_data_var = Label(self.master, textvariable=self.p3_c0_data_var, font=var_font)
        # Block 1
        label_p3_c1_title = Label(self.master, text="L1 - Block 1:", font=subtitle_header_font)
        label_p3_c1_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p3_c1_state_var = Label(self.master, textvariable=self.p3_c1_state_var, font=var_font)
        label_p3_c1_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p3_c1_address_var = Label(self.master, textvariable=self.p3_c1_address_var, font=var_font)
        label_p3_c1_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p3_c1_data_var = Label(self.master, textvariable=self.p3_c1_data_var, font=var_font)
        # Block 2
        label_p3_c2_title = Label(self.master, text="L1 - Block 2:", font=subtitle_header_font)
        label_p3_c2_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p3_c2_state_var = Label(self.master, textvariable=self.p3_c2_state_var, font=var_font)
        label_p3_c2_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p3_c2_address_var = Label(self.master, textvariable=self.p3_c2_address_var, font=var_font)
        label_p3_c2_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p3_c2_data_var = Label(self.master, textvariable=self.p3_c2_data_var, font=var_font)
        # Block 3
        label_p3_c3_title = Label(self.master, text="L1 - Block 3:", font=subtitle_header_font)
        label_p3_c3_state_title = Label(self.master, text="State:", font=subtitle_font)
        label_p3_c3_state_var = Label(self.master, textvariable=self.p3_c3_state_var, font=var_font)
        label_p3_c3_address_title = Label(self.master, text="Address:", font=subtitle_font)
        label_p3_c3_address_var = Label(self.master, textvariable=self.p3_c3_address_var, font=var_font)
        label_p3_c3_data_title = Label(self.master, text="Data:", font=subtitle_font)
        label_p3_c3_data_var = Label(self.master, textvariable=self.p3_c3_data_var, font=var_font)

        # Place labels
        label_p3_title.place(x=20, y=590)
        # Instructions
        xi = 20
        yi = 620
        label_p3_instructions_title.place(x=xi, y=yi)
        label_p3_exec_title.place(x=xi, y=yi + 30)
        label_p3_exec_var.place(x=xi + 120, y=yi + 30)
        label_p3_last_exec_title.place(x=xi, y=yi + 60)
        label_p3_last_exec_var.place(x=xi + 120, y=yi + 60)
        # Cache
        # Block 0
        xi = 300
        label_p3_c0_title.place(x=xi, y=yi)
        label_p3_c0_state_title.place(x=xi, y=yi + 30)
        label_p3_c0_state_var.place(x=xi + 110, y=yi + 30)
        label_p3_c0_address_title.place(x=xi, y=yi + 60)
        label_p3_c0_address_var.place(x=xi + 110, y=yi + 60)
        label_p3_c0_data_title.place(x=xi, y=yi + 90)
        label_p3_c0_data_var.place(x=xi + 110, y=yi + 90)
        # Block 1
        xi = 520
        label_p3_c1_title.place(x=xi, y=yi)
        label_p3_c1_state_title.place(x=xi, y=yi + 30)
        label_p3_c1_state_var.place(x=xi + 110, y=yi + 30)
        label_p3_c1_address_title.place(x=xi, y=yi + 60)
        label_p3_c1_address_var.place(x=xi + 110, y=yi + 60)
        label_p3_c1_data_title.place(x=xi, y=yi + 90)
        label_p3_c1_data_var.place(x=xi + 110, y=yi + 90)
        # Block 2
        xi = 740
        label_p3_c2_title.place(x=xi, y=yi)
        label_p3_c2_state_title.place(x=xi, y=yi + 30)
        label_p3_c2_state_var.place(x=xi + 110, y=yi + 30)
        label_p3_c2_address_title.place(x=xi, y=yi + 60)
        label_p3_c2_address_var.place(x=xi + 110, y=yi + 60)
        label_p3_c2_data_title.place(x=xi, y=yi + 90)
        label_p3_c2_data_var.place(x=xi + 110, y=yi + 90)
        # Block 3
        xi = 960
        label_p3_c3_title.place(x=xi, y=yi)
        label_p3_c3_state_title.place(x=xi, y=yi + 30)
        label_p3_c3_state_var.place(x=xi + 110, y=yi + 30)
        label_p3_c3_address_title.place(x=xi, y=yi + 60)
        label_p3_c3_address_var.place(x=xi + 110, y=yi + 60)
        label_p3_c3_data_title.place(x=xi, y=yi + 90)
        label_p3_c3_data_var.place(x=xi + 110, y=yi + 90)

        # Memory Labels
        label_mem_title = Label(self.master, text="Memory", font=("Arial", 14))

        label_mem0_title = Label(self.master, text="Block 0", font=subtitle_header_font)
        label_mem0_var = Label(self.master, textvariable=self.mem_b0_var, font=var_font)
        label_mem1_title = Label(self.master, text="Block 1", font=subtitle_header_font)
        label_mem1_var = Label(self.master, textvariable=self.mem_b1_var, font=var_font)
        label_mem2_title = Label(self.master, text="Block 2", font=subtitle_header_font)
        label_mem2_var = Label(self.master, textvariable=self.mem_b2_var, font=var_font)
        label_mem3_title = Label(self.master, text="Block 3", font=subtitle_header_font)
        label_mem3_var = Label(self.master, textvariable=self.mem_b3_var, font=var_font)
        label_mem4_title = Label(self.master, text="Block 4", font=subtitle_header_font)
        label_mem4_var = Label(self.master, textvariable=self.mem_b4_var, font=var_font)
        label_mem5_title = Label(self.master, text="Block 5", font=subtitle_header_font)
        label_mem5_var = Label(self.master, textvariable=self.mem_b5_var, font=var_font)
        label_mem6_title = Label(self.master, text="Block 6", font=subtitle_header_font)
        label_mem6_var = Label(self.master, textvariable=self.mem_b6_var, font=var_font)
        label_mem7_title = Label(self.master, text="Block 7", font=subtitle_header_font)
        label_mem7_var = Label(self.master, textvariable=self.mem_b7_var, font=var_font)

        xi = 20
        yi = 800
        sp = 150
        label_mem_title.place(x=xi, y=yi - 30)
        label_mem0_title.place(x=xi, y=yi)
        label_mem0_var.place(x=xi, y=yi + 30)
        label_mem1_title.place(x=xi + sp, y=yi)
        label_mem1_var.place(x=xi + sp, y=yi + 30)
        label_mem2_title.place(x=xi + (sp * 2), y=yi)
        label_mem2_var.place(x=xi + (sp * 2), y=yi + 30)
        label_mem3_title.place(x=xi + (sp * 3), y=yi)
        label_mem3_var.place(x=xi + (sp * 3), y=yi + 30)
        label_mem4_title.place(x=xi + (sp * 4), y=yi)
        label_mem4_var.place(x=xi + (sp * 4), y=yi + 30)
        label_mem5_title.place(x=xi + (sp * 5), y=yi)
        label_mem5_var.place(x=xi + (sp * 5), y=yi + 30)
        label_mem6_title.place(x=xi + (sp * 6), y=yi)
        label_mem6_var.place(x=xi + (sp * 6), y=yi + 30)
        label_mem7_title.place(x=xi + (sp * 7), y=yi)
        label_mem7_var.place(x=xi + (sp * 7), y=yi + 30)

        # Actions menu
        label_actions_title = Label(self.master, text="Actions", font=("Arial", 14, "bold"))
        label_actions_title.place(x=1250, y=40)

        button_start = Button(self.master, text="Start Simulation", command=self.start_sim, width=25)
        button_stop = Button(self.master, text="Stop Simulation", command=self.stop_sim, width=25)
        button_single_step = Button(self.master, text="Single Step", command=self.single_step, width=25)
        label_entry_instr_title = Label(self.master, text="Custom instruction:", font=("Arial", 12))
        button_add_instr = Button(self.master, text="Add", command=self.add_instr, width=25)

        button_start.place(x=1250, y=90)
        button_stop.place(x=1250, y=140)
        button_single_step.place(x=1250, y=190)
        label_entry_instr_title.place(x=1245, y=240)
        button_add_instr.place(x=1250, y=315)

    # Tkinter Debug UI labels and components
    def init_ui_debug(self):
        label_debug_title = Label(self.master, text="Debug Options", font=("Arial", 14, "bold"))
        label_debug_title.place(x=1250, y=400)

        label_instr_time_title = Label(self.master, text="Instruction time (s):", font=("Arial", 12))
        label_instr_time = Label(self.master, textvariable=self.instr_time, font=("Arial", 12, "bold"))
        label_entry_instr_time_title = Label(self.master, text="Change instruction time (s):", font=("Arial", 12))
        button_change_instr_time = Button(self.master, text="Change", command=self.change_instr_time, width=25)

        label_instr_time_title.place(x=1247, y=450)
        label_instr_time.place(x=1390, y=450)
        label_entry_instr_time_title.place(x=1245, y=490)
        button_change_instr_time.place(x=1250, y=560)

        button = Button(self.master, text="Generate Instruction", command=self.gen_test, width=25)
        button.place(x=1250, y=630)

    # Initialize CPU instances
    def init_cpus(self):
        # Create CPU instances
        cpu0 = CPU(0)
        cpu1 = CPU(1)
        cpu2 = CPU(2)
        cpu3 = CPU(3)

        # Store them in a local list and send them to the bus
        self.cpus = [cpu0, cpu1, cpu2, cpu3]
        self.bus.cpus = self.cpus

        # Debug instruction mode
        # cpu0.debug_instrs = ["WRITE 010 FFFF"]
        # cpu1.debug_instrs = ["CALC", "CALC", "READ 010", "WRITE 010 0010"]

        # Thread to update UI vars in real time
        update_thread = threading.Thread(target=self.update_ui_vars, daemon=True)
        update_thread.start()

    def add_instr(self):
        n_instr = self.entry_instr.get()
        if len(n_instr) > 0:
            self.entry_instr.delete(0, END)
            cpu_name = self.selected_processor
            print("UI: ADDED INSTRUCTION " + cpu_name + ": " + n_instr)
            match cpu_name:
                case "P0":
                    self.cpus[0].set_custom_instr(n_instr)
                case "P1":
                    self.cpus[1].set_custom_instr(n_instr)
                case "P2":
                    self.cpus[2].set_custom_instr(n_instr)
                case "P3":
                    self.cpus[3].set_custom_instr(n_instr)
        else:
            print("No instruction written")

    def change_instr_time(self):
        n_time = self.entry_instr_time.get()
        if len(n_time) > 0:
            self.entry_instr_time.delete(0, END)
            self.instr_time.set(n_time)
            for cpu in self.cpus:
                cpu.set_instr_time(n_time)
        else:
            print("No time written")

    # Debug test to check random instruction generator
    def gen_test(self):
        instr = Gen.generate_random_instruction()
        print(instr)

    # Single step mode. Each CPU generates a single instruction and executes it
    def single_step(self):
        for cpu in self.cpus:
            cpu.play(True)

    # Continuous execution mode. Each CPU generates multiple infinite random instructions and executes them
    def start_sim(self):
        for cpu in self.cpus:
            cpu.play()

    # Pauses/Stops the simulation
    def stop_sim(self):
        for cpu in self.cpus:
            cpu.stop()

    # Called when combobox of processor selection is changes
    def update_processor_cb(self, *args):
        n_value = self.processor_cb.get()
        self.selected_processor = n_value
        print(n_value)

    # Called by thread to update all UI variables
    def update_ui_vars(self):
        while 1:
            cpu0 = self.cpus[0]
            self.p0_exec_var.set(cpu0.status)
            self.p0_last_exec_var.set(cpu0.last_instr)
            self.p0_c0_state_var.set(str(cpu0.controller.cache.block_0.state))
            self.p0_c0_address_var.set(dec_to_bin(cpu0.controller.cache.block_0.address))
            self.p0_c0_data_var.set(dec_to_hex(cpu0.controller.cache.block_0.data))
            self.p0_c1_state_var.set(str(cpu0.controller.cache.block_1.state))
            self.p0_c1_address_var.set(dec_to_bin(cpu0.controller.cache.block_1.address))
            self.p0_c1_data_var.set(dec_to_hex(cpu0.controller.cache.block_1.data))
            self.p0_c2_state_var.set(str(cpu0.controller.cache.block_2.state))
            self.p0_c2_address_var.set(dec_to_bin(cpu0.controller.cache.block_2.address))
            self.p0_c2_data_var.set(dec_to_hex(cpu0.controller.cache.block_2.data))
            self.p0_c3_state_var.set(str(cpu0.controller.cache.block_3.state))
            self.p0_c3_address_var.set(dec_to_bin(cpu0.controller.cache.block_3.address))
            self.p0_c3_data_var.set(dec_to_hex(cpu0.controller.cache.block_3.data))

            cpu1 = self.cpus[1]
            self.p1_exec_var.set(cpu1.status)
            self.p1_last_exec_var.set(cpu1.last_instr)
            self.p1_c0_state_var.set(str(cpu1.controller.cache.block_0.state))
            self.p1_c0_address_var.set(dec_to_bin(cpu1.controller.cache.block_0.address))
            self.p1_c0_data_var.set(dec_to_hex(cpu1.controller.cache.block_0.data))
            self.p1_c1_state_var.set(str(cpu1.controller.cache.block_1.state))
            self.p1_c1_address_var.set(dec_to_bin(cpu1.controller.cache.block_1.address))
            self.p1_c1_data_var.set(dec_to_hex(cpu1.controller.cache.block_1.data))
            self.p1_c2_state_var.set(str(cpu1.controller.cache.block_2.state))
            self.p1_c2_address_var.set(dec_to_bin(cpu1.controller.cache.block_2.address))
            self.p1_c2_data_var.set(dec_to_hex(cpu1.controller.cache.block_2.data))
            self.p1_c3_state_var.set(str(cpu1.controller.cache.block_3.state))
            self.p1_c3_address_var.set(dec_to_bin(cpu1.controller.cache.block_3.address))
            self.p1_c3_data_var.set(dec_to_hex(cpu1.controller.cache.block_3.data))

            cpu2 = self.cpus[2]
            self.p2_exec_var.set(cpu2.status)
            self.p2_last_exec_var.set(cpu2.last_instr)
            self.p2_c0_state_var.set(str(cpu2.controller.cache.block_0.state))
            self.p2_c0_address_var.set(dec_to_bin(cpu2.controller.cache.block_0.address))
            self.p2_c0_data_var.set(dec_to_hex(cpu2.controller.cache.block_0.data))
            self.p2_c1_state_var.set(str(cpu2.controller.cache.block_1.state))
            self.p2_c1_address_var.set(dec_to_bin(cpu2.controller.cache.block_1.address))
            self.p2_c1_data_var.set(dec_to_hex(cpu2.controller.cache.block_1.data))
            self.p2_c2_state_var.set(str(cpu2.controller.cache.block_2.state))
            self.p2_c2_address_var.set(dec_to_bin(cpu2.controller.cache.block_2.address))
            self.p2_c2_data_var.set(dec_to_hex(cpu2.controller.cache.block_2.data))
            self.p2_c3_state_var.set(str(cpu2.controller.cache.block_3.state))
            self.p2_c3_address_var.set(dec_to_bin(cpu2.controller.cache.block_3.address))
            self.p2_c3_data_var.set(dec_to_hex(cpu2.controller.cache.block_3.data))

            cpu3 = self.cpus[3]
            self.p3_exec_var.set(cpu3.status)
            self.p3_last_exec_var.set(cpu3.last_instr)
            self.p3_c0_state_var.set(str(cpu3.controller.cache.block_0.state))
            self.p3_c0_address_var.set(dec_to_bin(cpu3.controller.cache.block_0.address))
            self.p3_c0_data_var.set(dec_to_hex(cpu3.controller.cache.block_0.data))
            self.p3_c1_state_var.set(str(cpu3.controller.cache.block_1.state))
            self.p3_c1_address_var.set(dec_to_bin(cpu3.controller.cache.block_1.address))
            self.p3_c1_data_var.set(dec_to_hex(cpu3.controller.cache.block_1.data))
            self.p3_c2_state_var.set(str(cpu3.controller.cache.block_2.state))
            self.p3_c2_address_var.set(dec_to_bin(cpu3.controller.cache.block_2.address))
            self.p3_c2_data_var.set(dec_to_hex(cpu3.controller.cache.block_2.data))
            self.p3_c3_state_var.set(str(cpu3.controller.cache.block_3.state))
            self.p3_c3_address_var.set(dec_to_bin(cpu3.controller.cache.block_3.address))
            self.p3_c3_data_var.set(dec_to_hex(cpu3.controller.cache.block_3.data))

            mem = self.bus.memory
            self.mem_b0_var.set(dec_to_hex(mem.block_0.get_data()))
            self.mem_b1_var.set(dec_to_hex(mem.block_1.get_data()))
            self.mem_b2_var.set(dec_to_hex(mem.block_2.get_data()))
            self.mem_b3_var.set(dec_to_hex(mem.block_3.get_data()))
            self.mem_b4_var.set(dec_to_hex(mem.block_4.get_data()))
            self.mem_b5_var.set(dec_to_hex(mem.block_5.get_data()))
            self.mem_b6_var.set(dec_to_hex(mem.block_6.get_data()))
            self.mem_b7_var.set(dec_to_hex(mem.block_7.get_data()))

            time.sleep(0.1)

