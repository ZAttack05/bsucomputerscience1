def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

jump = {"1":f1,"2":f2,"3":f3}

def runCommand(command):
    jump[command]()

runCommand("3")
