import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruina Kalkulator Sederhana")
        
        self.entry = tk.Entry(root, width=20, font=('Helvetica', 20))
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for label, row, col in buttons:
            button = tk.Button(self.root, text=label, width=5, height=2, font=('Helvetica', 15), command=lambda l=label: self.button_click(l))
            button.grid(row=row, column=col)
    
    def button_click(self, label):
        if label == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif label == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, label)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

