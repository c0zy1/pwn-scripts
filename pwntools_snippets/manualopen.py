

#chain is your exploit, rop chain or whatever, exploit is the name of the generated file
# you can insert this into your exploit to generate a fresh file of your bytesequence 

with open ("exploit", "wb") as f:
    f.write(chain)