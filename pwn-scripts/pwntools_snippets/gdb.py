from pwn import *

# p2 is your process, this will interactively open gdb at the desired breakpoint


gdb.attach(p2, '''
    set disassembly-flavor intel
                 # oder Adresse der verwundbaren Funktion
    continue
''')