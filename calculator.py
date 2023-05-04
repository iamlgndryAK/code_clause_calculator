from tkinter import Tk, Button, Entry, END

operator_list = ["+", "-", "*", "/"]
count = 0
sign = ""


class App:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("325x350")
        self.window.title("Calc")
        self.window.configure(bg="#5F9EA0")
        self.display = Entry(self.window, width=20,  font=('Arial', 16), borderwidth=5)
        self.display.place(x=25, y=0)
        self.display.bind("<Return>", self.get_entry)

        self.result_display = Entry(self.window, width=20, font=('Arial', 16), borderwidth=5)
        self.result_display.config(state='disabled', disabledforeground='black', disabledbackground="gray")
        self.result_display.place(x=25, y=300)

        self.enter_button = Button(self.window, text="=", padx=20, pady=10, command=lambda: self.get_entry(""))
        self.enter_button.grid(row=1, column=3)

        self.button_1 = Button(self.window, text="1", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(1))
        self.button_2 = Button(self.window, text="2", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(2))
        self.button_3 = Button(self.window, text="3", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(3))
        self.button_4 = Button(self.window, text="4", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(4))
        self.button_5 = Button(self.window, text="5", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(5))
        self.button_6 = Button(self.window, text="6", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(6))
        self.button_7 = Button(self.window, text="7", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(7))
        self.button_8 = Button(self.window, text="8", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(8))
        self.button_9 = Button(self.window, text="9", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(9))
        self.button_0 = Button(self.window, text="0", font=('Arial', 16), padx=27, pady=10, command=lambda: self.button_click(0))

        self.button_1.grid(row=2, column=0)
        self.button_2.grid(row=2, column=1)
        self.button_3.grid(row=2, column=2)
        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        self.button_7.grid(row=4, column=0)
        self.button_8.grid(row=4, column=1)
        self.button_9.grid(row=4, column=2)
        self.button_0.grid(row=5, column=1)

        self.add_button = Button(self.window, text="+", font=('Arial', 14), padx=27, pady=10, command=lambda: self.display.insert(END, "+"))
        self.subtract_button = Button(self.window, text="-", font=('Arial', 16), padx=27, pady=10, command=lambda: self.display.insert(END, "-"))
        self.multiply_button = Button(self.window, text="*", font=('Arial', 16), padx=27, pady=10, command=lambda: self.display.insert(END, "*"))
        self.divide_button = Button(self.window, text="/", font=('Arial', 16), padx=27, pady=10, command=lambda: self.display.insert(END, "/"))

        self.add_button.grid(row=2, column=3)
        self.subtract_button.grid(row=3, column=3)
        self.multiply_button.grid(row=4, column=3)
        self.divide_button.grid(row=5, column=3)

        self.window.mainloop()

    def get_entry(self, _):
        text = self.display.get()
        self.display.delete(0, END)
        self.get_number(text)

    def get_number(self, text):
        global count, sign
        count = 0
        for i in text:
            if i in operator_list:
                sign = i
                count = count + 1
        if count == 1:
            x, y = self.extract(text)
            if self.convert_to_int(x) is not False and self.convert_to_int(y) is not False:
                if sign == "+":
                    result = self.add(int(x), int(y))
                    self.display_output(result)
                elif sign == "-":
                    result = self.subtract(int(x), int(y))
                    self.display_output(result)
                elif sign == "*":
                    result = self.multiply(int(x), int(y))
                    self.display_output(result)
                else:
                    result = self.divide(int(x), int(y))
                    self.display_output(result)
            elif x == "" and self.convert_to_int(y) is not False and sign in ["+", "-"]:
                self.display_output(f"{sign}{y}")
            else:
                error = "Syntax Error!"
                self.display_output(error)
        elif text == "":
            pass
        elif self.convert_to_int(text) is not False:
            self.display_output(self.convert_to_int(text))

        else:
            error = "Syntax Error!"
            self.display_output(error)

    def extract(self, text):
        operator_index = text.find(sign)
        x = text[:operator_index]
        y = text[operator_index + 1:]
        return x, y

    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, str(current) + str(number))

    def display_output(self, result):
        self.result_display.config(state='normal')
        self.result_display.delete(0, END)
        self.result_display.insert(0, str(result))
        self.result_display.config(state='disabled')

    def convert_to_int(self, number):
        try:
            return int(number)
        except ValueError:
            return False

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


app = App()
