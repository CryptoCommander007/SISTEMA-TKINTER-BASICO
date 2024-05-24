import tkinter as tk

class Window4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana 4")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.root, text="Esta es la ventana 4", font=("Arial", 14))
        label.pack(pady=20)
        button = tk.Button(self.root, text="Cerrar", command=self.root.destroy)
        button.pack(pady=10)

    def run(self):
        self.root.mainloop()
