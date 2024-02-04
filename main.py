"""
Exercise: An implementation of a simple GUI-based calculator using Model/View/Controller design pattern.
"""
import tkinter as Tk


class Model:
    """
    Model class, abstracts the core data of the MVC pattern,
    Model maintains updates data based on events/calls it receives
    from Controller. Dependency should be one-way, Controller to Model,
    in other words, Model functions should NOT actively call methods of
    Controller or View
    """

    def __init__(self):
        self.expr = ''

    def event(self, x):
        self.expr += x

    def calculate(self):
        try:
            self.expr = str(eval(self.expr))
        except:
            self.expr = ''

    def clear(self):
        self.expr = ''

    @property
    def value(self):
        return 0 if self.expr == '' else self.expr


class View:
    """
    View in the MVC pattern assumes role of rendering user
    interface to the user, and maintaining an up-to-date view as
    it handles user interaction it receives from Controller.
    """

    def _add_calculator_display(self, frame):
        # Calculator Display
        self.display = Tk.Label(frame, text=0, width=12, height=1)
        self.display.grid(row=0, column=0, columnspan=10, pady=5)

    def _add_numbers_keypad(self, frame):
        # Calculator Numbers Pad
        self.one = Tk.Button(frame, text="1")
        self.one.grid(row=1, column=0)

        self.two = Tk.Button(frame, text="2")
        self.two.grid(row=1, column=1)

        self.three = Tk.Button(frame, text="3")
        self.three.grid(row=1, column=2)

        self.four = Tk.Button(frame, text="4")
        self.four.grid(row=2, column=0)

        self.five = Tk.Button(frame, text="5")
        self.five.grid(row=2, column=1)

        self.six = Tk.Button(frame, text="6")
        self.six.grid(row=2, column=2)

        self.seven = Tk.Button(frame, text="7")
        self.seven.grid(row=3, column=0)

        self.eight = Tk.Button(frame, text="8")
        self.eight.grid(row=3, column=1)

        self.nine = Tk.Button(frame, text="9")
        self.nine.grid(row=3, column=2)

        self.zero = Tk.Button(frame, text="0")
        self.zero.grid(row=4, column=1)

    def _add_operations_keypad(self, frame):
        # Operations Pad
        self.clear = Tk.Button(frame, text="C")
        self.clear.grid(row=4, column=0)

        self.equal = Tk.Button(frame, text="=")
        self.equal.grid(row=4, column=2)

        self.add = Tk.Button(frame, text="+")
        self.add.grid(row=2, column=5)

        self.sub = Tk.Button(frame, text="-")
        self.sub.grid(row=3, column=5)

        self.mul = Tk.Button(frame, text="*")
        self.mul.grid(row=2, column=6)

        self.div = Tk.Button(frame, text="/")
        self.div.grid(row=3, column=6)
        # my code for adding decimal on calculator display
        self.decimal_value = Tk.Button(frame, text=".")
        self.decimal_value.grid(row=4, column=5)

    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("MVC Exercise: Calculator")
        self.root.geometry()

        self._frame = Tk.Frame(self.root)
        self._frame.pack()
        self._add_calculator_display(self._frame)
        self._add_numbers_keypad(self._frame)
        self._add_operations_keypad(self._frame)

    def refresh(self, value):
        self.display.config(text=value)
        print('\n...Value: [ ', value, ' ]')

    def attach_keyboard(self, callback):
        self.root.bind("<Key>", callback)

    def start(self):
        self.root.mainloop()


class Controller:
    """
    Controller is the primary coordinator in the MVC patter, it collects
    user input, initiates necessary changes to model (data), and refreshes
    view to reflect any changes that might have happened.
    """

    def __init__(self, my_model, my_view):
        self.model = my_model
        self.view = my_view

        # Number Pad Button Events
        self.view.one.bind("<Button>", lambda event, n=1: self.number_pad_callback(n))
        self.view.two.bind("<Button>", lambda event, n=2: self.number_pad_callback(n))
        self.view.three.bind("<Button>", lambda event, n=3: self.number_pad_callback(n))
        self.view.four.bind("<Button>", lambda event, n=4: self.number_pad_callback(n))
        self.view.five.bind("<Button>", lambda event, n=5: self.number_pad_callback(n))
        self.view.six.bind("<Button>", lambda event, n=6: self.number_pad_callback(n))
        self.view.seven.bind("<Button>", lambda event, n=7: self.number_pad_callback(n))
        self.view.eight.bind("<Button>", lambda event, n=8: self.number_pad_callback(n))
        self.view.nine.bind("<Button>", lambda event, n=9: self.number_pad_callback(n))
        self.view.zero.bind("<Button>", lambda event, n=0: self.number_pad_callback(n))

        # Operator Pad Button Events
        self.view.add.bind("<Button>", lambda event, op='+': self.operation_pad_callback(op))
        self.view.sub.bind("<Button>", lambda event, op='-': self.operation_pad_callback(op))
        self.view.mul.bind("<Button>", lambda event, op='*': self.operation_pad_callback(op))
        self.view.div.bind("<Button>", lambda event, op='/': self.operation_pad_callback(op))
        # Decimal button event
        self.view.decimal_value.bind("<Button>", lambda event, op='.': self.operation_pad_callback(op))
        # Equal and Clear Button Events
        self.view.equal.bind("<Button>", self.equal)
        self.view.clear.bind("<Button>", self.clear)

        self.view.attach_keyboard(self.keystroke_callback)

    def keystroke_callback(self, event):
        """
        TODO: Make updates in this method for keyboard events!

        This is where you will handle keystroke events from user
        and then (the Controller) should invoke necessary methods
        on the View and and refresh the View
        """
        print('keystroke: {}'.format(event.keysym))

        if event.keysym in '0123456789':
            self.model.event(event.keysym)
        elif event.keysym == 'plus':
            self.model.event('+')
        elif event.keysym == 'minus':
            self.model.event('-')
        elif event.keysym == 'slash':
            self.model.event('/')
        elif event.keysym == 'asterisk':
            self.model.event('*')
        elif event.keysym == 'period':
            if '.' not in self.model.expr:
                self.model.event('.')
            print('decimal point pressed')
        elif event.keysym == 'Return':
            self.equal(event)

        elif event.keysym == 'c':
            self.clear(event)
        else:
            print('\n the key stroke is not number or value  '.format(event.keysym))
            return
        self.view.refresh(self.model.value)
        print('keystroke: {}'.format(event.keysym))

    def number_pad_callback(self, num):
        self.model.event(str(num))
        self.view.refresh(self.model.value)
        print('number {} is clicked'.format(num))

    def operation_pad_callback(self, operation):
        self.model.event(operation)
        self.view.refresh(self.model.value)
        print('operation: {}'.format(operation))

    def equal(self, event):
        self.model.calculate()
        self.view.refresh(self.model.value)
        print('equal pressed')

    def clear(self, event):
        self.model.clear()
        self.view.refresh(self.model.value)

    def run(self):
        self.view.start()


if __name__ == '__main__':
    """
    Main function, instantiate instances of Model, View and a Controller.
    """

    # This simply prints out your current Python version for awareness.
    import sys

    print('-----')
    print('Python Version: {python_version}'.format(python_version=sys.version))
    print('-----')

    # Instantiate the Model, View, and Controller
    model = Model()
    view = View()
    controller = Controller(my_model=model, my_view=view)
    controller.run()

