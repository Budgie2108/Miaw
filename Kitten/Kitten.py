import os
import sys
import time
def stutter(text):
    for c in text:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(.02)
stutter('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Hello from my cats!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
def write(x):
    print(x)
def kill(prm,prcss):
    if prm == '/n':
        os.system("taskkill /im  " + prcss)
    elif prm == '/n /f' or prm == '/f /n':
        os.system("taskkill /f /im  " + prcss)
    elif prm == '/PID':
        os.system("taskkill /PID  " + prcss)
    elif prm == '/PID /f' or prm == '/f /PID':
        os.system("taskkill /PID  /f  " + prcss)
    elif prm == '/PID /t' or prm == '/t /PID':
        os.system("taskkill /PID  /t  " + prcss)
    elif '/PID' in prm and '/f' in prm and '/t' in prm:
        os.system("taskkill /PID /f /t" + prcss)
    elif '/n' in prm and '/f' in prm and '/t' in prm:
        os.system("taskkill /im /f /t" + prcss)
    elif prm == '/t /n' or prm == '/n /t':
        os.system("taskkill /im /t" + prcss)
def close():
    exit()
def pip(op,n,re):
    if re == 'upgrade':
        os.system('start cmd /k python.exe -m pip ' + op + ' --upgrade')
    elif op == 'list' or op == 'freeze':
        os.system('start cmd /k python.exe -m pip list')
    elif re == 'version':
        if op != None and n != None:
            os.system('start cmd /k python.exe -m pip ' + op + ' --version')
        else:
            os.system('start cmd /k python.exe -m pip --version')
    else:
        os.system('start cmd /k python.exe -m pip ' + op + ' ' + n + re)
def add(n1,n2):
    pass
