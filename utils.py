cryptTable = [0] * 0x500

def prepareCryptTable():
    seed, index1, index2 = 0x00100001, 0, 0
    i = 0 
    while index1 < 0x100:
      index2 = index1  
      while i < 5:
        seed = (seed * 125 + 3) % 0x2AAAAB;
        temp1 = (seed & 0xFFFF) << 0x10;
        seed = (seed * 125 + 3) % 0x2AAAAB;
        temp2 = (seed & 0xFFFF);
        cryptTable[index2] = (temp1 | temp2);  
        # print(temp1|temp2, index2)
        i+=1
        index2+=0x100
      index1+=1

def HashString(key, dwHashType):
    seed1, seed2 = 0x7FED7FED, 0xEEEEEEEE
    key = key.upper()
    for i in range(len(key)):
        seed1 = cryptTable[(dwHashType << 8) + ord(key[i])] ^ (seed1 + seed2);
        seed2 = ord(key[i]) + seed1 + seed2 + (seed2 << 5) + 3;

    return seed1
