from pwn import *

# p2 is your process, this will interactively open gdb at the desired breakpoint


gdb.attach(p2, '''
    set disassembly-flavor intel
    break *pwnme+138             # oder Adresse der verwundbaren Funktion
    continue
''')