from tkinter import StringVar, ttk, constants
from services.calculator import Calculator

class GUI:
    def __init__(self, root):
        self._root = root
        self._label_var = None
        self.read_number = ""
        self.operand = ""
        self.operator = ""
        self.final_done = False
        self.done = False
        self.calculator = Calculator()

    def start(self):
        
        self.calculator.set_operand1(0)
        self._label_var = StringVar()
        self._label_var.set(self.calculator.get_operand1())
        calculator_screen = ttk.Label(master=self._root, textvariable=self._label_var)

        button_1 = ttk.Button(master=self._root,
        text="?",command=lambda: self._clear_button_click())
        button_2 = ttk.Button(master=self._root,
        text="?",command=lambda: self._clear_button_click())
        button_3 = ttk.Button(master=self._root,
        text="?",command=lambda: self._clear_button_click())
        button_4 = ttk.Button(master=self._root,
        text="STAT",command=lambda: self._stat_button_click())
        button_5 = ttk.Button(master=self._root,
        text="C",command=lambda: self._clear_button_click())
        button_6 = ttk.Button(master=self._root,
        text="+/-",command=lambda: self._negation_button_click())
        button_7 = ttk.Button(master=self._root,
        text="sq",command=lambda: self._one_operator_func_button_click("sqrt"))
        button_8 = ttk.Button(master=self._root,
        text="/",command=lambda: self._two_operator_func_button_click("/"))
        button_9 = ttk.Button(master=self._root,
        text="7",command=lambda: self._number_button_click("7"))
        button_10 = ttk.Button(master=self._root,
        text="8",command=lambda: self._number_button_click("8"))
        button_11 = ttk.Button(master=self._root,
        text="9",command=lambda: self._number_button_click("9"))
        button_12 = ttk.Button(master=self._root,
        text="*",command=lambda: self._two_operator_func_button_click("*"))
        button_13 = ttk.Button(master=self._root,
        text="4",command=lambda: self._number_button_click("4"))
        button_14 = ttk.Button(master=self._root,
        text="5",command=lambda: self._number_button_click("5"))
        button_15 = ttk.Button(master=self._root,
        text="6",command=lambda: self._number_button_click("6"))
        button_16 = ttk.Button(master=self._root,
        text="-",command=lambda: self._two_operator_func_button_click("-"))
        button_17 = ttk.Button(master=self._root,
        text="1", command=lambda: self._number_button_click("1"))
        button_18 = ttk.Button(master=self._root,
        text="2",command=lambda: self._number_button_click("2"))
        button_19 = ttk.Button(master=self._root,
        text="3",command=lambda: self._number_button_click("3"))
        button_20 = ttk.Button(master=self._root,
        text="+",command=lambda: self._two_operator_func_button_click("+"))
        button_21 = ttk.Button(master=self._root,
        text="0",command=lambda: self._number_button_click("0"))
        button_22 = ttk.Button(master=self._root,
        text=".",command=lambda: self._number_button_click("."))
        button_23 = ttk.Button(master=self._root,
        text="exp",command=lambda: self._one_operator_func_button_click("exp"))
        button_24 = ttk.Button(master=self._root,
        text="=",command=lambda: self._equation_button_click())

        calculator_screen.grid(row=0,column=0,columnspan=4,sticky=(constants.E))
        button_1.grid(row=1, column=0)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)
        button_4.grid(row=1, column=3)
        button_5.grid(row=2, column=0)
        button_6.grid(row=2, column=1)
        button_7.grid(row=2, column=2)
        button_8.grid(row=2, column=3)
        button_9.grid(row=3, column=0)
        button_10.grid(row=3, column=1)
        button_11.grid(row=3, column=2)
        button_12.grid(row=3, column=3)
        button_13.grid(row=4, column=0)
        button_14.grid(row=4, column=1)
        button_15.grid(row=4, column=2)
        button_16.grid(row=4, column=3)
        button_17.grid(row=5, column=0)
        button_18.grid(row=5, column=1)
        button_19.grid(row=5, column=2)
        button_20.grid(row=5, column=3)
        button_21.grid(row=6, column=0)
        button_22.grid(row=6, column=1)
        button_23.grid(row=6, column=2)
        button_24.grid(row=6, column=3)

    def _number_button_click(self,num):
        if not self.final_done:
            dot = "."
            if num == dot:
                if dot not in self.read_number:
                    self.read_number = self.read_number+num
            else:
                if self.read_number == "0" :
                    self.read_number = num
                elif self.read_number == "":
                    self.read_number = num
                else:
                    self.read_number = self.read_number + num   
            self._label_var.set(self.read_number)

    def _clear_button_click(self):
        self.calculator.set_operand1("0")
        self.done=False
        self.operator = ""
        self.read_number = self.calculator.get_operand1()
        self._label_var.set(self.read_number)
        self.final_done = False

    def _negation_button_click(self):
        if not self.final_done:
            if self.read_number != "0":
                dot="."
            if dot in self.read_number:
                self.read_number = str((float(self.read_number)*-1))
            else:
                self.read_number = str((int(self.read_number)*-1))
            self._label_var.set(self.read_number)

    def _one_operator_func_button_click(self, operator:str):
        if not self.done:
            self.calculator.set_operand1(self.read_number)
            #self.calculator.count_one_operands(operator)
            self.read_number=self.calculator.count_one_operands(operator)
            self._label_var.set(self.read_number)
            self.done = True

    def _two_operator_func_button_click(self, operator:str):
        if not self.done:
            self.operator = operator
            self.calculator.set_operand1(self.read_number)
            self.read_number = ""
            self._label_var.set(self.read_number)
            self.done = True

    def _equation_button_click(self):
        self._label_var.set(self.calculator.count_two_operands(self.operator,self.read_number))
        self.final_done = True

    def _stat_button_click(self):
        self.calculator.get_stats()
        self.final_done = True
