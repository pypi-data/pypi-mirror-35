from tkinter import *
import tkinter.messagebox as messagebox
import math, time, sys, login

FONT = 'none 18'
folder = __file__.rstrip('calculatorTkinter.py')


class Calculator(login.ChangePassword):
    
    def __init__(self, window):
        
        window.title('Calculator')
        window.iconbitmap(folder+'logo.ico')
        self.justCalculated = False
        
        # Create the Entry box, and set focus on it
        self.entry = Entry(window, font=FONT)
        self.entry.grid(row=0, column=0, columnspan=6, pady=3)
        self.entry.focus()
        self.entry.bind('<Return>', self.equalFunction)
        
        # Number buttons
        self.zero = Button(window, text='0', width=9, font=FONT, command=lambda: self.display('0'))
        self.one = Button(window, text='1', width=4, font=FONT, command=lambda: self.display('1'))
        self.two = Button(window, text='2', width=4, font=FONT, command=lambda: self.display('2'))
        self.three = Button(window, text='3', width=4, font=FONT, command=lambda: self.display('3'))
        self.four = Button(window, text='4', width=4, font=FONT, command=lambda: self.display('4'))
        self.five = Button(window, text='5', width=4, font=FONT, command=lambda: self.display('5'))
        self.six = Button(window, text='6', width=4, font=FONT, command=lambda: self.display('6'))
        self.seven = Button(window, text='7', width=4, font=FONT, command=lambda: self.display('7'))
        self.eight = Button(window, text='8', width=4, font=FONT, command=lambda: self.display('8'))
        self.nine = Button(window, text='9', width=4, font=FONT, command=lambda: self.display('9'))
        
        
        # Standard Operator buttons
        self.percent = Button(window, text='%', width=4, font=FONT, command=lambda: self.display('%'))
        self.squareRoot = Button(window, text='√', width=4, font=FONT, command=self.squareRoot)
        self.square = Button(window, text='x²', width=4, font=FONT, command=self.square)
        self.reciprocal = Button(window, text='1/x', width=4, font=FONT, command=self.reciprocal)
        self.C = Button(window, text='C', width=4, font=FONT, command=self.clearAll)
        self.backspace = Button(window, text='⌫', width=4, font=FONT, command=self.clear)
        self.divide = Button(window, text='÷', width=4, font=FONT, command=lambda: self.display('÷'))
        self.multiply = Button(window, text='×', width=4, font=FONT, command=lambda: self.display('×'))
        self.subtract = Button(window, text='-', width=4, font=FONT, command=lambda: self.display('-'))        
        self.add = Button(window, text='+', width=4, font=FONT, command=lambda: self.display('+'))
        self.equal = Button(window, text='=', width=4, font=FONT, command=self.equalFunction)
        self.decimal = Button(window, text='.', width=4, font=FONT, command=lambda: self.display('.'))
        

        # Scientific add-ons        
        self.cube = Button(window, text='x³', width=4, font=FONT, command=self.cube)
        self.power = Button(window, text='xⁿ', width=4, font=FONT, command=lambda: self.display('^'))
        self.root = Button(window, text='y√x', width=4, font=FONT, command=self.root)
        self.standardForm = Button(window, text='×10ⁿ', width=4, font=FONT, command=lambda: self.display('×10^'))
        self.pi = Button(window, text='π', width=4, font=FONT, command=lambda: self.display('π'))
        self.e = Button(window, text='e', width=4, font=FONT, command=lambda: self.display('e'))
        self.mod = Button(window, text='Mod', width=4, font=FONT, command=lambda: self.display(' Mod '))
        self.fractionMode = Button(window, text='Fraction Mode', width=11, font='none 15', command=self.fractionMode)
        self.factorial = Button(window, text='x!', width=4, font=FONT, command=self.factorial)
        self.openBracket = Button(window, text='(', width=4, font=FONT, command=lambda: self.display('('))
        self.closeBracket = Button(window, text=')', width=4, font=FONT, command=lambda: self.display(')'))
        

        # Startup Screen
        self.entry.grid_remove()
        self.startLabel = Label(window, text='Click on a\ndrop down and\nselect command.', font='none 40')
        self.startLabel.grid()

        # Create Drop-Down Menu
        menu = Menu(window)
        window.config(menu=menu)

        # File Menu
        fileMenu = Menu(menu)
        menu.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='Change Password', command=lambda: self.displayChange(window, exit=False))

        # Open new window as current window has been destroyed
        self.window = Tk()
        self.window.withdraw() # Hide the window as it is currently blank
        self.window.title('Calculator')
        self.startLabel.grid()
        
        fileMenu.add_command(label='Exit', command=lambda: self.exitFunction(window))

        # Calculator Menu
        calculatorMenu = Menu(menu)
        menu.add_cascade(label='Calculator', menu=calculatorMenu)
        calculatorMenu.add_command(label='Standard', command=self.standard)
        calculatorMenu.add_command(label='Scientific', command=self.scientific)
        calculatorMenu.add_command(label='Programmer', command=self.programmer)

        # Converter Menu
        converterMenu = Menu(menu)
        menu.add_cascade(label='Converter', menu=converterMenu)
        converterMenu.add_command(label='Currency')
        converterMenu.add_command(label='Volume')
        converterMenu.add_command(label='Length')
        converterMenu.add_command(label='Weight and Mass')
        converterMenu.add_command(label='Temperature')
        converterMenu.add_command(label='Energy')
        converterMenu.add_command(label='Area')
        converterMenu.add_command(label='Speed')
        converterMenu.add_command(label='Time')
        converterMenu.add_command(label='Power')
        converterMenu.add_command(label='Data')
        converterMenu.add_command(label='Pressure')
        converterMenu.add_command(label='Angle')


    def standard(self):
        # Display screen for standard option
        
        # Ready Screen
        for widget in window.children.values(): # Clear screen
            widget.grid_remove()
        self.entry.grid()
        self.entry.configure(width=19)
        self.equal.configure(height=3)
        
        # Grid Standard buttons
        self.percent.grid(column=0, row=1)
        self.squareRoot.grid(column=1, row=1)
        self.square.grid(column=2, row=1)
        self.reciprocal.grid(column=3, row=1)

        self.C.grid(column=0, row=2)
        self.backspace.grid(column=1, row=2)
        self.divide.grid(column=2, row=2)
        self.multiply.grid(column=3, row=2)

        self.seven.grid(column=0, row=3)
        self.eight.grid(column=1, row=3)
        self.nine.grid(column=2, row=3)
        self.subtract.grid(column=3, row=3)

        self.four.grid(column=0, row=4)
        self.five.grid(column=1, row=4)
        self.six.grid(column=2, row=4)
        self.add.grid(column=3, row=4)

        self.one.grid(column=0, row=5)
        self.two.grid(column=1, row=5)
        self.three.grid(column=2, row=5)
        self.equal.grid(column=3, row=5, rowspan=2)

        self.zero.grid(column=0, row=6, columnspan=2)
        self.decimal.grid(column=2, row=6)


    def scientific(self):
        # Display screen for scientific option
        
        # Reset Screen
        for widget in window.children.values(): # Clear screen
            widget.grid_remove()
        self.entry.grid()
        self.entry.configure(width=24)
        self.equal.configure(height=1)
        
        # Grid Scientific buttons
        self.square.grid(column=0, row=1)
        self.cube.grid(column=1, row=1)
        self.power.grid(column=2, row=1)
        self.squareRoot.grid(column=3, row=1)
        self.root.grid(column=4, row=1)

        self.reciprocal.grid(column=0, row=2)
        self.standardForm.grid(column=1, row=2)
        self.pi.grid(column=2, row=2)
        self.e.grid(column=3, row=2)
        self.mod.grid(column=4, row=2)

        self.fractionMode.grid(column=0, row=3, columnspan=2)
        self.C.grid(column=2, row=3)
        self.backspace.grid(column=3, row=3)
        self.divide.grid(column=4, row=3)

        self.factorial.grid(column=0, row=4)
        self.seven.grid(column=1, row=4)
        self.eight.grid(column=2, row=4)
        self.nine.grid(column=3, row=4)
        self.multiply.grid(column=4, row=4)

        self.percent.grid(column=0, row=5)
        self.four.grid(column=1, row=5)
        self.five.grid(column=2, row=5)
        self.six.grid(column=3, row=5)
        self.subtract.grid(column=4, row=5)

        self.openBracket.grid(column=0, row=6)
        self.one.grid(column=1, row=6)
        self.two.grid(column=2, row=6)
        self.three.grid(column=3, row=6)
        self.add.grid(column=4, row=6)

        self.closeBracket.grid(column=0, row=7)
        self.zero.grid(column=1, row=7, columnspan=2)
        self.decimal.grid(column=3, row=7)
        self.equal.grid(column=4, row=7)


    def programmer(self):
        # Display screen for programmer option
        
        # Reset Screen
        for widget in window.children.values(): # Clear screen
            widget.grid_remove()

        # Make new buttons as other buttons are bound to entry widget which isn't used here
        zero = Button(window, text='0', width=9, font=FONT, command=lambda: self.programDisplay('0'))
        one = Button(window, text='1', width=4, font=FONT, command=lambda: self.programDisplay('1'))
        two = Button(window, text='2', width=4, font=FONT, command=lambda: self.programDisplay('2'))
        three = Button(window, text='3', width=4, font=FONT, command=lambda: self.programDisplay('3'))
        four = Button(window, text='4', width=4, font=FONT, command=lambda: self.programDisplay('4'))
        five = Button(window, text='5', width=4, font=FONT, command=lambda: self.programDisplay('5'))
        six = Button(window, text='6', width=4, font=FONT, command=lambda: self.programDisplay('6'))
        seven = Button(window, text='7', width=4, font=FONT, command=lambda: self.programDisplay('7'))
        eight = Button(window, text='8', width=4, font=FONT, command=lambda: self.programDisplay('8'))
        nine = Button(window, text='9', width=4, font=FONT, command=lambda: self.programDisplay('9'))

        a = Button(window, text='A', width=4, font=FONT, command=lambda: self.programDisplay('A'))
        b = Button(window, text='B', width=4, font=FONT, command=lambda: self.programDisplay('B'))
        c = Button(window, text='C', width=4, font=FONT, command=lambda: self.programDisplay('C'))
        d = Button(window, text='D', width=4, font=FONT, command=lambda: self.programDisplay('D'))
        e = Button(window, text='E', width=4, font=FONT, command=lambda: self.programDisplay('E'))
        f = Button(window, text='F', width=4, font=FONT, command=lambda: self.programDisplay('F'))

        deleteAll = Button(window, text='Delete all', width=9, font=FONT, command=self.programClearAll)
        backspace = Button(window, text='⌫', width=4, font=FONT, command=self.programClear)
        decimalLabel = Label(window, text='Decimal', width=9, font=FONT)
        decimalEntry = Entry(window, width=9, font=FONT, name='decimal'); decimalEntry.focus()
        binaryLabel = Label(window, text='Binary', width=9, font=FONT)
        binaryEntry = Entry(window, width=9, font=FONT, name='binary')
        hexadecimalLabel = Label(window, text='Hexadecimal', width=11, font='none 16')
        hexadecimalEntry = Entry(window, width=9, font=FONT, name='hexadecimal')
        calculate = self.calculateButton(window)

        # Grid widgets
        decimalLabel.grid(column=0, row=0, columnspan=2)
        binaryLabel.grid(column=2, row=0, columnspan=2)
        hexadecimalLabel.grid(column=4, row=0, columnspan=2)
        
        decimalEntry.grid(column=0, row=1, columnspan=2)
        binaryEntry.grid(column=2, row=1, columnspan=2)
        hexadecimalEntry.grid(column=4, row=1, columnspan=2)

        a.grid(column=0, row=2)
        b.grid(column=1, row=2)
        seven.grid(column=2, row=2)
        eight.grid(column=3, row=2)
        nine.grid(column=4, row=2)
        calculate.grid(column=5, row=2, rowspan=4)
        
        c.grid(column=0, row=3)
        d.grid(column=1, row=3)
        four.grid(column=2, row=3)
        five.grid(column=3, row=3)
        six.grid(column=4, row=3)
        
        e.grid(column=0, row=4)
        f.grid(column=1, row=4)
        one.grid(column=2, row=4)
        two.grid(column=3, row=4)
        three.grid(column=4, row=4)
        
        deleteAll.grid(column=0, row=5, columnspan=2)
        backspace.grid(column=2, row=5)
        zero.grid(column=3, row=5, columnspan=2)

        self.notDecimal = [a, b, c, d, e, f]
        self.notBinary = [a, b, c, d, e, f, two, three, four, five, six, seven, eight, nine]
        self.notHexadecimal = []

        entry = window.focus_get()
        if entry == decimalEntry:
            print('dv')
            for button in self.notDecimal:
                button.configure(state=DISABLED)
        elif entry == binaryEntry:
            for button in self.notBinary:
                button.configure(state=DISABLED)
        elif entry == hexadecimalEntry:
            for button in self.notHexadecimal:
                button.configure(state=DISABLED)


    def exitFunction(self, window):
        window.destroy()
        sys.exit()

    def display(self, character):
        # If just pressed equal, clear screen
        if self.justCalculated:
            if not character in ('+', '-', '×', '÷', '√', 'x²', ' Mod ', 'π', 'e', '^', '%'):
                self.entry.delete(0, END)
            self.justCalculated = False

            if character in ('+', '-', '×', '÷', '√', 'x²', ' Mod ', 'π', 'e', '^', '%'):
                self.entry.insert(END, self.lastAnswer)
        
        # Displays button pressed
        self.entry.insert(END, character)

    def equalFunction(self, *args):
        # Replace × and ÷ with * and /
        text = self.replace()
        
        try:
            answer = eval(text)
            answer = self.removeZero(answer)
            display = answer
        except ZeroDivisionError:
            display = 'Cannot divide by 0'
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def clear(self):
        # Backspace
        self.entry.delete(len(self.entry.get()) - 1)
    
    def clearAll(self):
        # C
        self.entry.delete(0,END)

    def replace(self):
        text = self.entry.get()
        newText = text.replace('×', '*')
        newText = newText.replace('÷', '/')
        newText = newText.replace('^', '**')
        pi = str(math.pi)
        newText = newText.replace('π', '*' + pi) if len(newText) != 1 else newText.replace('π', pi)
        e = str(math.e)
        newText = newText.replace('e', '*' + e) if len(newText) != 1 else newText.replace('e', e)

        while '%' in newText:
            digits = ''
            position = list(newText).index('%')
            for character in reversed(newText[:position]):
                if not character in '0123456789.' or newText.index(character) == 0:
                    if character in '0123456789.':
                        digits = character + digits
                    newText = newText.replace(digits + '%', str(float(digits) / 100))
                    break
                else:
                    digits = character + digits

        newText = newText.replace(' Mod ', '%')

        return newText

    def removeZero(self, num):
        # Remove .0 from end of answer if its there
        if num % 1 == 0:
            return int(num)
        return num

    def squareRoot(self):
        text = self.replace()
        
        try:
            value = eval(text)
            answer = math.sqrt(value)
            answer = self.removeZero(answer)
            display = answer
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def square(self):
        text = self.replace()
        
        try:
            value = eval(text)
            answer = math.pow(value, 2)
            answer = self.removeZero(answer)
            display = answer
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def reciprocal(self):
        text = self.replace()
        
        try:
            value = eval(text)
            answer = 1 / value
            answer = self.removeZero(answer)
            display = answer
        except ZeroDivisionError:
            display = 'Cannot divide by 0'
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def cube(self):
        text = self.replace()
        
        try:
            value = eval(text)
            answer = math.pow(value, 3)
            answer = self.removeZero(answer)
            display = answer
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def root(self):
        display = 'This function has yet been completed'
        self.entry.delete(0, END)
        self.entry.insert(0, display)
        self.lastAnswer = display
        self.justCalculated = True

    def fractionMode(self):
        display = 'This function has yet been completed'
        self.entry.delete(0, END)
        self.entry.insert(0, display)
        self.lastAnswer = display
        self.justCalculated = True

    def factorial(self):
        text = self.replace()
        
        try:
            value = eval(text)
            answer = math.factorial(value)
            answer = self.removeZero(answer)
            display = answer
        except SyntaxError or NameError:
            display = 'Invalid Input'
        finally:
            self.entry.delete(0, END)
            self.entry.insert(0, display)
            self.lastAnswer = display
            self.justCalculated = True

    def calculateButton(self, window):
        # Get width and height
        button = Button(window, width=7, height=12)
        button.pack()
        button.update()
        width, height = button.winfo_width(), button.winfo_height()
        button.pack_forget(); del button
        
        button = Canvas(window, background='SystemButtonFace', width=width, height=height, borderwidth=2, relief=RAISED)
        button.create_text(width//8, 6, angle='-90', anchor=SW, text='Calculate', fill='SystemButtonText', font='none 33')
        button.bind('<ButtonPress-1>', lambda event: event.widget.configure(relief=SUNKEN))
        button.bind('<ButtonRelease-1>', lambda event: event.widget.configure(relief=RAISED))
        button.bind('<ButtonPress-1>', lambda x: self.calculateFunction(), add='+')
        return button

    def calculateFunction(self):
        pass

    def programDisplay(self, character):
        entry = window.focus_get()
        entry.insert(END, character)

    def programClear(self):
        entry = window.focus_get()
        entry.delete(len(entry.get()) - 1)

    def programClearAll(self):
        entry = window.focus_get()
        entry.delete(0, END)

if __name__ == '__main__':
    login = login.Login()
    login.startup(); del login
    window = Tk()
    calculator = Calculator(window)
    window.mainloop()
