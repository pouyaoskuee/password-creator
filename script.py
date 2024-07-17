import random
import string
y=int(input("chand ta ramz mikhai?"))
n=int(input("chand ta adad dashte bashe?"))
a=int(input("chand ta kalame dashte bashe?"))
r=int(input("chand ta simbol dashte bashe?"))


def func():
    z=open("paswoords.txt","w")
    for t in range(y):
        d = ("")
        for i in range(a):
            b = (random.choice(string.ascii_letters))
            d += b
        for i in range(n):
            c = str(random.randrange(0, 9))
            d += c
        for i in range(r):
            s = (random.choice(string.punctuation))
            d+=s
        z.writelines([d,"\n"])
    z.close()
    
func()
print("ba movfagyat anjam shod")
