from GUI import Window, Button, Label, application

class PyGUIApp(Window):
    def __init__(self):
        super().__init__(title="PyGUI Example", width=300, height=200)

        self.label = Label(text='Hello, PyGUI!', position=(20, 100))
        self.add(self.label)

        self.button = Button(text='Click me', position=(100, 50))
        self.button.on_click = self.on_click
        self.add(self.button)

    def on_click(self, btn):
        self.label.text = 'Button Clicked!'

if __name__ == '__main__':
    app = application()
    window = PyGUIApp()
    window.show()
    app.run()
