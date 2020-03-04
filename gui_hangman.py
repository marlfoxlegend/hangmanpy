import typing as Tp
from tkinter import ttk as ttk
from tkinter.ttk import tkinter as tk
from itertools import starmap

# Top structure classes


class LeftFrame(ttk.Frame):
    """Child of MainApplication. It contains the Canvas widget"""

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=400, height=400, padding='0.25i', borderwidth=1, relief=tk.RIDGE)
        self.grid(column=0, row=0, sticky=tk.NSEW, padx=20, pady=20)


class RightFrame(ttk.Frame):
    """Child of MainApplication. It contains the remaining widgets"""

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=400, height=400, padding='0.25i', borderwidth=1, relief=tk.GROOVE)
        # 1x3 Grid to fit widgets
        self.rowconfigure([0, 1, 2], weight=1)
        self.columnconfigure(0, weight=1)
        # Grid into column 2 of MainApp
        self.grid(column=1, row=0, sticky=tk.NSEW, padx=20, pady=20)


class HangmanCanvas(tk.Canvas):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.grid(sticky=tk.NSEW)
        line = []
        for y in range(5, 125, 5):
            line.append([5, y])
        self.create_line(line)


class GuessesLabel(ttk.Label):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)


class GuessEntry(ttk.Entry):
    def __init__(self, master=None, widget=None, **kw):
        super().__init__(master=master, widget=widget, **kw)


class SubmitButton(ttk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)


class ClearButton(ttk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)


class MainApplication(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1, minsize=100)
        top.columnconfigure(0, weight=1, minsize=100)
        self.rowconfigure(0, weight=1, minsize=100)
        self.columnconfigure([0, 1], weight=1, minsize=100)
        self.grid(sticky=tk.NSEW, padx=25, pady=25)

        self.left = LeftFrame(self)
        self.right = RightFrame(self)
        self.hangmanCanvas = HangmanCanvas(self.left)
        self.guessesLabel = GuessesLabel(self.right)
        self.guessEntry = GuessEntry(self.right)
        self.submitButton = SubmitButton(self.right)
        self.clearButton = ClearButton(self.right)


if __name__ == '__main__':
    main = MainApplication()
    main.mainloop()
