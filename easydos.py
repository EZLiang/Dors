import inspect
import os


def parse(cmd):
    command = cmd.split(" ")[0]
    args = " ".join(cmd.split(" ")[1:])
    return command, args


def _donothing():
    return


class Application:
    def __init__(self):
        self.commands = {}
        self.environment = {"cwdir": os.getcwd(), "echo": True}
        self.onerror = _donothing
        self.base = os.getcwd()

    def set(self, name, value):
        self.environment[name] = value

    def error(self, fun):
        self.onerror = fun
        return fun

    def command(self, name):
        def f(fun):
            self.commands[name] = fun
            return fun

        return f

    def run(self):
        while True:
            try:
                directory = "C:" + self.environment["cwdir"][len(self.base):] if self.environment["echo"] else ""
                cmd = input(directory + r"> ")
                parts = cmd.split(" | ")
                carryover = ""
                for i in parts:
                    command, args = parse(i)
                    if (args != "") or (carryover == ""):
                        args += carryover
                    else:
                        args = carryover[1:]
                    if command in self.commands:
                        handler = self.commands[command]
                        b = ""
                        if len(inspect.signature(handler).parameters) == 1:
                            b = handler(args)
                        else:
                            b = handler(args, self.environment)
                            if b is None:
                                b = ""
                        carryover = " " + b
                        print(b)
                    else:
                        print("Command not found")
                        break
            except KeyboardInterrupt:
                break
            except:
                if len(inspect.signature(self.onerror).parameters) == 0:
                    self.onerror()
                else:
                    self.onerror(self.environment)
