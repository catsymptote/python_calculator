import re


class Calculator:
    legal_operator = "+ - * / % ^"
    legal_chars = "+ - * / % ^ 0 1 2 3 4 5 6 7 8 9"

    inp_str = ""
    elements = []
    solution = None


    def __init__(self, inp_str=None):
        if inp_str != None:
            self.from_str(inp_str)


    def do(self, problem="0"):
        self.from_str(problem)
        self.calc_list()
        return self.solution


    def from_str(self, inp_str):
        #self.elements = inp_str.split(self.operator_symbols)
        #self.elements = re.split(self.legal_operator, inp_str)
        chars = list(inp_str)


        i = 0
        while i < len(chars) - 1:
            if self.is_float(chars[i]) and self.is_float(chars[i + 1]):
                chars[i + 1] = chars[i] + chars[i + 1]
                chars.pop(i)
            else:
                i += 1
            if i > 1000:
                print("Killed loop in from_str()")
                return
        print("len(chars) :", len(chars))
        self.elements = chars


        for j in range(len(self.elements)):
            if self.is_float(self.elements[j]):
                self.elements[j] = float(self.elements[j])


    def check_input(self):
        i = 0
        while " " in self.inp_str:
            self.inp_str.replace(" ", "")
            i += 1
            if i > 1000:
                print("Killed loop in check_input()")
                return


    def basic_operations(self, num1, op, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return None
        elif op == "%":
            if num2 != 0:
                return num1 % num2
            else:
                return None
        elif op == "^":
            if num1 == num2 == 0:
                print("0^0 is undefined, but let's pretend it's 1.")
            return num1**num2
        else:
            print("whut")
        

    def calc_list(self):
        print(self.elements)
        i = 0
        while len(self.elements) > 2:
            num1, op, num2 = self.elements[0:3]
            self.elements[2] = self.basic_operations(num1, op, num2)
            self.elements = self.elements[2:]
            i += 1
            if i > 1000:
                print("Killed loop in calc_list()")
                return

        if len(self.elements) == 1:
            self.solution = self.elements[0]
        else:
            print("Len:", len(self.elements))


    def is_float(self, a):
        return a.isdigit()
        try:
            float(a)
            return True
        except:
            return False
