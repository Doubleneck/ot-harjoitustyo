from tkinter import StringVar, ttk, constants
from services.calculator_service import CalculatorService

class GUI:
    def __init__(self, root):
        self._root = root
        self._label_var = None
        self.read_number = ""
        self.operator = ""
        self.done = False
        self.calculator = CalculatorService()

    def start(self):
        self.calculator.set_operand1(0)
        self._label_var = StringVar()
        self._label_var.set(self.calculator.get_operand1())
        calculator_screen = ttk.Label(master=self._root, textvariable=self._label_var)

        button_1 = ttk.Button(master=self._root,
        text="?",command=lambda: self._set_result())
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
        dot="."
        if self.read_number != "":
            if dot in self.read_number:
                self.read_number = str((float(self.read_number)*-1))
            else:
                if self.read_number != "0":
                    self.read_number = str((int(self.read_number)*-1))
            self._label_var.set(self.read_number)

    def _one_operator_func_button_click(self, operator:str):
        if not self.done:
            self.calculator.set_operand1(self.read_number)
            self.read_number = self.calculator.count_one_operands(operator)
            self._set_result()

    def _two_operator_func_button_click(self, operator:str):
        if self.read_number == "":
            self.done = False
            self.read_number = self.calculator.get_operand1()
        if not self.done:
            self.operator = operator
            self.calculator.set_operand1(self.read_number)
            self.read_number = ""
            self._label_var.set(self.read_number)
            self.done = True

    def _equation_button_click(self):
        if self.read_number != "":
            self._label_var.set(self.calculator.count_two_operands(self.operator,self.read_number))
            self._set_result()

    def _stat_button_click(self):
        res=self.calculator.get_stats()
        if res == 0:
            print("Ei laskettuja laskutoimituksia")
        else:
            add=format(int(res[1])*100/int(res[0]),".1f")
            sub=format(int(res[2])*100/int(res[0]),".1f")
            div=format(int(res[3])*100/int(res[0]),".1f")
            mul=format(int(res[4])*100/int(res[0]),".1f")
            sqrt=format(int(res[5])*100/int(res[0]),".1f")
            exp=format(int(res[6])*100/int(res[0]),".1f")
            print("***********LASKUTILASTOT************")
            print ("operaatiota '+' laskettu " + str(res[1]) +
                   " kertaa, "+ str(add) + "% kaikista")
            print ("operaatiota '-' laskettu " + str(res[2]) +
                   " kertaa, "+ str(sub) + "% kaikista")
            print ("operaatiota '/' laskettu " + str(res[3]) +
                   " kertaa, "+ str(div) + "% kaikista")
            print ("operaatiota '*' laskettu " + str(res[4]) +
                   " kertaa, "+ str(mul) + "% kaikista")
            print ("operaatiota 'sqrt' laskettu " + str(res[5]) +
                   " kertaa, "+ str(sqrt) + "% kaikista")
            print ("operaatiota 'exp' laskettu " + str(res[6]) +
                   " kertaa, "+ str(exp) + "% kaikista")
            print ("Yhteensä " + str(res[0])  + " laskua suoritettu")
        self._clear_button_click()

    def _set_result(self):
        self.done=False
        self.operator = ""
        self.read_number = self.calculator.get_operand1()
        self._label_var.set(self.read_number)
