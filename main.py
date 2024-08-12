from tkinter import *
root = Tk()
root.title("My Simple Calculator")
root.geometry("466x400")

entryText = Text(root, height = 2, width = 25, font =("Times New Roman", 16))
entryText.grid(row = 0, column = 0, columnspan = 3)

def Click(symbol) :
    current = entryText.get("1.0", "end-1c")
    entryText.delete("1.0", "end")
    entryText.insert("1.0", current + str(symbol))

def Addition() :
    firstNumber = entryText.get("1.0", "end-1c")
    global fnumb
    global math
    math = "Add"
    fnumb = int(firstNumber)
    entryText.delete("1.0", "end")

def Subtraction() :
    firstNumber = entryText.get("1.0", "end-1c")
    global fnumb
    global math
    math = "Subtract"
    fnumb = int(firstNumber)
    entryText.delete("1.0", "end")

def Multiplication() :
    firstNumber = entryText.get("1.0", "end-1c")
    global fnumb
    global math
    math = "Multiply"
    fnumb = int(firstNumber)
    entryText.delete("1.0", "end")

def Division() :
    firstNumber = entryText.get("1.0", "end-1c")
    global fnumb
    global math
    math = "Divide"
    fnumb = int(firstNumber)
    entryText.delete("1.0", "end")

def Remainder() :
    firstNumber = entryText.get("1.0", "end-1c")
    global fnumb
    global math
    math = "Rest"
    fnumb = int(firstNumber)
    entryText.delete("1.0", "end")

def Clear() :
    entryText.delete("1.0", "end")

def Equal() :
    secondNumber = entryText.get("1.0", "end-1c")
    entryText.delete("1.0", "end")
    if math == "Add" :
        result = fnumb + int(secondNumber)
    elif math == "Subtract" :
        result = fnumb - int(secondNumber)
    elif math == "Multiply" :
        result = fnumb * int(secondNumber)
    elif math == "Divide" :
        result = fnumb / int(secondNumber)
    elif math == "Rest" :
        result = fnumb % int(secondNumber)
    entryText.insert("1.0", result)

button1 = Button(root, text = "1", padx = 39, pady = 20, command = lambda : Click(1))
button2 = Button(root, text = "2", padx = 39, pady = 20, command = lambda : Click(2))
button3 = Button(root, text = "3", padx = 39, pady = 20, command = lambda : Click(3))

button4 = Button(root, text = "4", padx = 39, pady = 20, command = lambda : Click(4))
button5 = Button(root, text = "5", padx = 39, pady = 20, command = lambda : Click(5))
button6 = Button(root, text = "6", padx = 39, pady = 20, command = lambda : Click(6))

button7 = Button(root, text = "7", padx = 39, pady = 20, command = lambda : Click(7))
button8 = Button(root, text = "8", padx = 39, pady = 20, command = lambda : Click(8))
button9 = Button(root, text = "9", padx = 39, pady = 20, command = lambda : Click(9))

button0 = Button(root, text = "0", padx = 39, pady = 20, command = lambda : Click(0))

buttonAdd = Button(root, text = "+", padx = 39, pady = 20, command = Addition)
buttonSubtract = Button(root, text = "-", padx = 40, pady = 20, command = Subtraction)
buttonMultiply = Button(root, text = "x", padx = 39, pady = 20, command = Multiplication)
buttonDivide = Button(root, text = "/", padx = 40, pady = 20, command = Division)

buttonRemainder = Button(root, text = "%", padx = 38, pady = 20, command = Remainder)

buttonClear = Button(root, text = "Clear", padx = 75, pady = 20, command = Clear)
buttonClear.grid(row = 5, column = 1, columnspan = 2)

buttonEqual = Button(root, text = "=", padx = 38, pady = 20, command = Equal)
buttonEqual.grid(row = 5, column = 3)

button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)

button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

button0.grid(row = 5, column = 0)

buttonRemainder.grid(row = 1, column = 2)

buttonAdd.grid(row = 1, column = 3)
buttonSubtract.grid(row = 2, column = 3)

buttonMultiply.grid(row = 3, column = 3)
buttonDivide.grid(row = 4, column = 3)

root.mainloop()
