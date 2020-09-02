This is NOT a proper module. It simplify's it but it does have some more functions. Use kill() to stop a process, use write() to print() something out, ect,ect.
Setup:
Note: The installation instructions may be incorrect. Take care not to mess up your PC.
To install the module on windows, open cmd and type 'pip install miaw'.
To install it on mac, goto the mac Terminal and type 'sudo pip install miaw' and you will be ready to use it.

Files:
The github page is at https://github.com/RobDaMob/Miaw/
The module code itself, is located at the 2nd miaw folder or at https://github.com/RobDaMob/Miaw/tree/master/Miaw or at
miaw/miaw
The main file is located at Miaw/Miaw/Miaw.py
The setup file is located at Miaw/setup.py

Globals:
All of the module is located at the 2nd miaw folder(see line 2 for reference). Exceptions apply to setup files and info files.
All parameters can be replaced with None, if you don't need to specify them.
There are defaults for most parameters.


Commands:
1. The pip() command is used with the command pip('command','name','other').
2. The close() command exits the program, no parameters needed. It basically does the exit() command.
3. The kill() command exits a process with 2 parameters. parameters and process name/PID. The first one needs things like /t, /f, /n (which means /im), and PID.
The second one needs the PID or the name of the process.
4. The slow_write() command prints letters one at a time. The parameters are the thing(s) to print and the speed to write.
5. The write() command needs one parameter. What to write()/print()
