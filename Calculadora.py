# Encoding: UTF-8
from math import pi, e
from tkinter import Tk, Label, Button


class Calculator:

    FONT = 30
    HEIGHT = 1
    DBL_HEIGHT = int(HEIGHT * 2.2)
    WIDTH = 5
    DBL_WIDTH = int(WIDTH * 2.2)
    MAX_SCREEN_LENGTH = 27

    def __init__(self):

        self.__A = None
        self.__B = None
        self.__C = None
        self.__D = None

        self.janela = Tk(screenName="Calculadora")
        self.janela.title("Calculadora")
        self.janela['bg'] = '#e0e0ff'
        self.janela.geometry("261x330+1100+100")

        self.screen = Label(self.janela, text='', font=7, height=2, highlightbackground='#777777', background='#e0e0ff')
        self.screen.grid(row=0, column=0, columnspan=4)

        self.__row1()
        self.__row2()
        self.__column4()
        self.__number_pad()
        self.__vars()

        self.janela.mainloop()

    # Criação dos Botões
    def __click(self, x):
        if len(self.screen['text']) < Calculator.MAX_SCREEN_LENGTH:
            try:
                if self.screen['text'][-2] in '^X÷+-(' and str(x)[1] in '^X÷+-':
                    self.screen['text'] = self.screen['text'][:-3] + str(x)
                elif self.screen['text'] or not str(x)[1] in '^X÷+-':
                    self.screen['text'] += str(x)
            except IndexError:
                try:
                    if self.screen['text'] or not str(x)[1] in '^X÷+-':
                        self.screen['text'] += str(x)
                except IndexError:
                    self.screen['text'] += str(x)
        while self.screen['text'].startswith('0') and len(self.screen['text']) != 1:
            self.screen['text'] = self.screen['text'][1:]

    def __create_num_button(self, num):
        row = int((num - 1) / 3) + 3
        column = num % 3 - 1
        columnspan = 1
        width = Calculator.WIDTH

        if num == 0:
            row = 6
            column = 0
            columnspan = 2
            width = Calculator.DBL_WIDTH

        if column == -1:
            column = 2

        btn = Button(self.janela, text=f"{num}", font=Calculator.FONT, height=Calculator.HEIGHT, width=width,
                     command=lambda: self.__click(num), bg='#dddddd')
        btn.grid(row=row, column=column, columnspan=columnspan)
        return btn

    def __row1(self):

        Button(self.janela, text="Clear", font=Calculator.FONT, height=Calculator.HEIGHT,
               width=Calculator.DBL_WIDTH,
               command=self.__clear, bg='orange').grid(row=1, column=0, columnspan=2)

        Button(self.janela, text="⌫", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.DBL_WIDTH,
               command=self.__delete, bg='green').grid(row=1, column=2, columnspan=2)

    def __row2(self):

        def pi_e(item):
            try:
                if self.screen['text'][-2] in '^X÷+-(':
                    self.screen['text'] += f' {item} '
                else:
                    self.screen['text'] += f' X {item} '
            except IndexError:
                if self.screen['text']:
                    self.screen['text'] += f' X {item} '
                else:
                    self.screen['text'] += f' {item} '

        Button(self.janela, text="π", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: pi_e("π"), bg='green').grid(row=2, column=0)

        Button(self.janela, text="e", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: pi_e("e"), bg='green').grid(row=2, column=1)

        Button(self.janela, text="xʸ", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: self.__click(" ^ "), bg='green').grid(row=2, column=2)

    def __column4(self):

        begin_at = 2

        Button(self.janela, text="÷", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: self.__click(" ÷ "), bg='green').grid(row=begin_at, column=3)

        Button(self.janela, text="X", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: self.__click(" X "), bg='green').grid(row=begin_at + 1, column=3)

        Button(self.janela, text="-", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: self.__click(" - "), bg='green').grid(row=begin_at + 2, column=3)

        Button(self.janela, text="+", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=lambda: self.__click(" + "), bg='green').grid(row=begin_at + 3, column=3)

        def equal():
            self.screen['text'] = self.__calc(self.screen['text'])

        Button(self.janela, text="=", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=equal, bg='orange').grid(row=begin_at + 4, column=3)

    def __vars(self):

        Button(self.janela, text="A", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=self.__a, bg='red').grid(row=7, column=0)

        Button(self.janela, text="B", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=self.__b, bg='red').grid(row=7, column=1)

        Button(self.janela, text="C", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=self.__c, bg='red').grid(row=7, column=2)

        Button(self.janela, text="D", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=self.__d, bg='red').grid(row=7, column=3)

    def __number_pad(self):
        for i in range(10):
            self.__create_num_button(i)

        Button(self.janela, text=",", font=Calculator.FONT, height=Calculator.HEIGHT, width=Calculator.WIDTH,
               command=self.__virgula, bg='#aaaaaa').grid(row=6, column=2)

    # Funcionamento dos Botões

    def __virgula(self):
        try:
            if ',' not in self.screen['text'].split()[-1]:
                self.screen['text'] += ','
        except IndexError:
            pass

    def __delete(self):
        if self.screen['text'][-1] == ' ':
            ult = -3
        else:
            ult = -1
        self.screen['text'] = self.screen['text'][:ult]

    def __clear(self):
        self.screen['text'] = ''

    # Efetuar o Cálculo

    def __calc(self, string):

        def validacao(calc):
            # Values
            try:
                float(string[0])
            except ValueError:
                if string[0] != '(':
                    raise ValueError("Expressão Inválida")
            for n in string:
                try:
                    float(n)
                except ValueError:
                    if n not in '()**/+-':
                        raise ValueError(f"Expressão Inválida: {n}")

            # Valid_parentheses
            cont = 0
            for char in calc:
                if char == '(':
                    cont += 1
                elif char == ')':
                    cont -= 1
                if cont < 0:
                    raise ValueError("Parenteses não válidos")
            if cont:
                raise ValueError("Parenteses não válidos")

        def find_parenthesis(calc):
            start = calc.index('(') + 1
            while True:
                back = calc.index(')', start)
                try:
                    front = calc.index('(', start)
                    start = front + 1
                except ValueError:
                    return start, back
                if back < front:
                    return start, back

        def subst(calc: str):
            calc = calc.replace('X', '*')
            calc = calc.replace('÷', '/')
            calc = calc.replace('^', '**')
            calc = calc.replace(',', '.')
            calc = calc.replace('  ', ' ')
            calc = calc.replace('π', str(pi))
            calc = calc.replace('e', str(e))
            return calc

        string = subst(string).strip().split()
        validacao(string)

        while '(' in string:
            ini, fim = find_parenthesis(string)
            new = string[ini:fim]
            for _ in range(ini, fim + 2):
                string.pop(ini - 1)
            insert = str(self.__calc(' '.join(new)))
            string.insert(ini - 1, insert)

        i = 1
        while '**' in string and i < len(string):
            if string[i] == '**':
                f1 = float(string.pop(i - 1))
                string.pop(i - 1)
                f2 = float(string.pop(i - 1))
                string.insert(i - 1, str(f1 ** f2))
                i -= 1
            i += 1
        i = 1
        while ('*' in string or '/' in string) and i < len(string):
            if string[i] == '*':
                f1 = float(string.pop(i - 1))
                string.pop(i - 1)
                f2 = float(string.pop(i - 1))
                string.insert(i - 1, str(f1 * f2))
                i -= 1
            elif string[i] == '/':
                f1 = float(string.pop(i - 1))
                string.pop(i - 1)
                f2 = float(string.pop(i - 1))
                string.insert(i - 1, str(f1 / f2))
                i -= 1
            i += 1
        i = 1
        while ('+' in string or '-' in string) and i < len(string):
            if string[i] == '+':
                f1 = float(string.pop(i - 1))
                string.pop(i - 1)
                f2 = float(string.pop(i - 1))
                string.insert(i - 1, str(f1 + f2))
            elif string[i] == '-':
                f1 = float(string.pop(i - 1))
                string.pop(i - 1)
                f2 = float(string.pop(i - 1))
                string.insert(i - 1, str(f1 - f2))

        string = string[0].replace(',', '.')
        try:
            if not int(string.split('.')[1]):
                return string.split('.')[0]
        except IndexError:
            pass
        finally:
            return string.replace('.', ',')

    def __pi(self):
        self.screen['text'] += 'π'  # str(pi)

    def __euler(self):
        self.screen['text'] += 'e'  # str(e)

    def __a(self):
        if self.screen['text'] != "":
            self.__A = self.screen['text']
        else:
            self.screen['text'] = self.__A

    def __b(self):
        if self.screen['text'] != "":
            self.__B = self.screen['text']
        else:
            self.screen['text'] = self.__B

    def __c(self):
        if self.screen['text'] != "":
            self.__C = self.screen['text']
        else:
            self.screen['text'] = self.__C

    def __d(self):
        if self.screen['text'] != "":
            self.__D = self.screen['text']
        else:
            self.screen['text'] = self.__D


Calculator()
