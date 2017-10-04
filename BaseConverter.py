'''
Base Converter
By:         Vasili B
Started:    1/16/2015
Finished:   -

Desctription:
Useful functions for converting between bases, both the
whole and fractional parts of a number. Currently only
supports bases up to 32 and can only convert from decimal.
'''

def extractDigitsBackward(num,group=1): #extracts digits in reverse order
    numbers=[]
    while int(num)>0:
        numbers.append(int(0.1+(float(num)/(10.0**group)-num/(10**group))*(10**group))) #backward
        num/=(10**group)
    return numbers

def extractDigitsForward(num,group=1): #extracts digits in order
    numbers=[]
    while int(num)>0:
        numbers.insert(0,int(0.1+(float(num)/(10.0**group)-num/(10**group))*(10**group))) #forward
        num/=(10**group)
    return numbers

def DecTo64(x):
    characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    

def DecToI(x,i): #convert x from base i to base 10, cannot convert to bases higher than 32
    characters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    whole=int(x)
    frac=x-int(x)
    r=[]
    y=""
    while whole>0: #calculate whole number part
        r.insert(0,whole-int(whole/i)*i)
        whole=int(whole/i)
    if frac>0:
        r.append(".")
        for j in range(50): #calculate decimal part if it exists
            if frac==0: break
            frac*=i
            r.append(int(frac))
            frac-=int(frac)
    for k in range(len(r)): #put whole part together
        if r[k]==".":y+="."
        else: y+=characters[r[k]]
    return y

print extractDigitsBackward(131235,4)
