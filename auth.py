import random
from math import pow
import hashlib
import time
start = time.time()
a = 7
def gcd(a, b): 
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
# Generating large random numbers
def gen_key(q):
    key = 12345678998765432123456789
    #random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c
# Asymmetric encryption
def encrypt(msg, q, h, g):
    en_msg = []
    k = 19
    #gen_key(q) # Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i])
    print ('Encrypted pin : ', en_msg)
    output = hashlib.sha256(str(en_msg[1]).encode('utf-8')).hexdigest()
    print ('Hash generated : ',output)
    return en_msg, p, output
def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(int(en_msg[i])/h)))
    return dr_msg
# Driver code
def main():
    msg = input('Enter 4 digit pin : ')
    end = time.time()
    print("Original Message : ", msg)
    q = 123456789987654321234567898 
    #random.randint(pow(10, 20), pow(10, 50))
    g = 23931164504956447807213117212663825326210289577470
    key = gen_key(q) # Private key for receiver
    h = power(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)
    en_msg, p, out = encrypt(msg, q, h, g)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message : ", dmsg)
    print(end-start)
if __name__ == '__main__':
    main()
