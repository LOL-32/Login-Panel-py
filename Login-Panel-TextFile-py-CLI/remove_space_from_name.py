
def remove_space(x):
    alist=""
    for i in range(0,len(x)):
        a=(x[i])
        b=ord(a)
        if((b >= 65) and (b <= 90)):
            alist += a
        elif((b >= 97) and (b <= 122)):
            alist += a
        elif((b >= 48) and (b <=57)):
            alist += a
        else:
            continue
    return alist
        
    
