import tkinter as tk


def donothing():
    return


class Notepad:
    def __init__(self, path):
        with open(path) as f:
            self.contents = f.read()
        self.handle = open(path, "w")
        self.window = tk.Tk()
        self.textbox = tk.Text(self.window, font=("Courier New", 16))

        def save():
            a = self.textbox.get("1.0", "end")
            self.handle.write(a)

        self.menubar = tk.Menu(self.window)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=save)
        self.filemenu.add_command(label="Save as...", command=save)
        self.filemenu.add_command(label="Close", command=self.window.quit)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.window.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=donothing)

        self.editmenu.add_separator()

        self.editmenu.add_command(label="Cut", command=donothing)
        self.editmenu.add_command(label="Copy", command=donothing)
        self.editmenu.add_command(label="Paste", command=donothing)
        self.editmenu.add_command(label="Delete", command=donothing)
        self.editmenu.add_command(label="Select All", command=donothing)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.window.config(menu=self.menubar)

    def run(self):
        self.textbox.insert("insert", self.contents)
        self.textbox.pack()
        self.window.mainloop()

# a = Notepad("test.txt")
# a.run()