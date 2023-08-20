def hash(num):
    snum = str(num)
    if len(snum)<= 4:
        if len(snum) < 4:    
        #if len(snum) == 4:  
            snum = snum.rjust(4, '0')
        #return int(snum)
        return snum
    result = ''
    for i in range(0, len(snum) - 1, 2):
        left = snum[i]
        right = snum[i + 1]
        left = int(left)
        right = int(right)
        result += str(left + right)
    return hash(result)

print(hash(32435465))    
print(hash(9_103_804_912_177_010))

num = 6_402_373_705_728_000
print(f"Original = {num}\nHash = {hash(num)}")
print(f"Original = {5}\nHash = {hash(5)}")
print(f"Original = {67_592_543_345}\nHash = {hash(67_592_543_345)}")