import os, sys, time, subprocess
# import notepad
from random import randint
from datetime import datetime
from colorama import Fore, Back, init  # pip install colorama

import easydos

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

if os.name == "nt":
    os.system("color")  # only for windows

init()  # whatever

app = easydos.Application()
app.set("base", os.getcwd())
app.set("date", datetime.today().strftime('%Y-%m-%d'))
app.set("mac", mac = ("%02x:%02x:%02x:%02x:%02x:%02x" % tuple([randint(0, 255) for i in range(6)])))
app.set("version", "v1.0.0")


print(Back.BLACK, Fore.WHITE)  # terminal style

dors = """{0}oooooooooo.
`888'   `Y8b
 888      888  {1}.ooooo.  {2}oooo d8b  {3}.oooo.o
{0} 888      888 {1}d88' `88b {2}`888""8P {3}d88(  "8
{0} 888      888 {1}888   888  {2}888     {3}`"Y88b.
{0} 888     d88' {1}888   888  {2}888     {3}o.  )88b
{0}o888bood8P'   {1}`Y8bod8P' {2}d888b    {3}8""888P'


                                          {4}""".format(Fore.RED, Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.WHITE)

if not ("nostartup" in sys.argv):
    print(dors)

    def loading_bar(n, start_msg, end_msg):
        print((start_msg), end="")
        print("|", end="")
        for i in range(n):
            print(Back.WHITE, " ", end="")
            time.sleep(randint(0, 1))
        print(Back.BLACK, "|")
        print(end_msg)


    loading_bar(15, "Starting: ", "Dors has been successfully loaded.")
    print()
    print("Dors", (version), "on", sys.platform)

@app.error(env)
    os.chdir(env["base"])
    env["cwdir"] = env["base"]
    print(f"{Fore.RED}System has encountered an error. RESTARTING{Fore.WHITE}")
    time.sleep(1) # change back later if needed

@app.command("exit")
def exitcmd(args):
    raise KeyboardInterrupt()

@app.command("dir")
def dircmd(args):
    out = ""
    rawdir = os.listdir(os.getcwd())
    folders, files = [], []
    for i in rawdir:
        if "." in i:
            files.append(i)
        else:
            folders.append(i)
    if not (folders == []):
        out += "<FOLDERS>\n"
        for i in folders:
            out += i
            out += "\n"
    if not (files == []):
        out += "\n<FILES>\n"
        for i in files:
            out += i
            out += "\n"
    return out

@app.command("cd")
def cdcmd(args, env):
    if args[0] == "/" or args[0] == "\\":
        os.chdir(env["base"] + args)
    else:
        os.chdir(args)
    if not (env["base"] in os.getcwd()):
        raise Exception()

@app.command("echo")
def echocmd(args, env):
    if args == "off":
        env["echo"] = False
    if args == "on":
        env["echo"] = True
    return args

@app.command("echo.")
def echodotcmd(args):
    return "\n"

@app.command("ping")
def pingcmd(args):
    param = '-n' if os.name.lower() == 'nt' else '-c'
    ping_cmd = ['ping', param, '1', args]
    if subprocess.call(ping_cmd) == 0:
        return "Response from" + args
    if subprocess.call(ping_cmd) == 68:
        return "Unknown host"
    if subprocess.call(ping_cmd) == 2:
        return "Request timed out"

@app.command("getmac")
def getmaccmd(args, env):
    return env["mac"]

@app.command("date")
def datecmd(args, env):
    if args == "":
        date_in = input("Enter new date: ")
        if validate_date(date_in) == True: # TODO: place function at bottom to get rid of error
            env["date"] = date_in
        else:
            return "Incorrect format"
    if args == "/t":
        return env["date"]

@app.command("ver")
def vercmd(args, env):
    return env["version"]

@app.command("exec")
def execcmd(args):
    return # TODO: improve easydos to allow exec


"""def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except:
        return False"""
