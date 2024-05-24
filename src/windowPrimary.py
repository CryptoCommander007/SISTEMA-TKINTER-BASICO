import tkinter as tk
from window1 import Window1
from window2 import Window2
from window3 import Window3
from window4 import Window4

class WindowPrimary:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana Principal")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        button1 = tk.Button(self.root, text="Abrir Ventana 1", command=self.open_window1)
        button1.pack(pady=10)
        
        button2 = tk.Button(self.root, text="Abrir Ventana 2", command=self.open_window2)
        button2.pack(pady=10)
        
        button3 = tk.Button(self.root, text="Abrir Ventana 3", command=self.open_window3)
        button3.pack(pady=10)
        
        button4 = tk.Button(self.root, text="Abrir Ventana 4", command=self.open_window4)
        button4.pack(pady=10)

    def open_window1(self):
        win1 = Window1()
        win1.run()
    
    def open_window2(self):
        win2 = Window2()
        win2.run()

    def open_window3(self):
        win3 = Window3()
        win3.run()

    def open_window4(self):
        win4 = Window4()
        win4.run()

    def run(self):
        self.root.mainloop()
