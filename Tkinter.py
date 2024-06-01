import tkinter as tk

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tkinter Example')

        self.label = tk.Label(root, text='Hello, Tkinter!')
        self.label.pack(pady=20)

        self.button = tk.Button(root, text='Click me', command=self.on_click)
        self.button.pack(pady=20)

    def on_click(self):
        self.label.config(text='Button Clicked!')

if __name__ == '__main__':
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
