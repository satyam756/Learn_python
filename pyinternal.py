'''

Python inner working

> python chai.py #(interpreter program/script file)

|-------|                 ------------------
|-------|                 |   python VM    |
|-------| => byte code => |                |
|-------|                 ------------------ 

1. Compile to byte code -> low level and platform independent

2. Byte code runs faster

3. .pye -> compiled python (frozen binaries)

4. __pycache__ (for internal use of python )

5. Source chang and python version (only the changed part gets created)

6. hello_chai.cpython-312.pyc

7. works only for imported files

8. not for the top level files

9. cpython - standard version of python 

'''

'''

1. PVM - Python virtual machine

2. code loop to iterate byte code

3. run time engine

4. also known as python interpreter

5. Byte code is not machine code

6. python specific interpretation

7. cpython(standard),jpython(java binaries),ironpython,stackless(concurrency),pypy(performance orianted)

'''

'''
# python shell (IDLE)

# for direct run from the IDLE

> code is not saved here 

> no suggestions

> executes commands directly - immediate after line

> from importlib import reload

> reload(helloworld)

'''

'''

# Mutable and unmutable in python 

> Mutable: which can be changed 

> immutable: which cannot be changed

12:00 - chai or python

x = 10

y = x

x = 15

print(x) # 15
print(y) # 10

'''

