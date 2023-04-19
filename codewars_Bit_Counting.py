#мое решение
def count_bits(n):
    count = 0
    if n > 0:
        result = bin(n)[2:]
        number = []
        for i in result:
            number.append(i)
        for b in number:
            if b == '1':
                count += 1
                
            else:
                count += 0    
        return count           
    else:
        return 0 
    
#второй способ как монжо было решить
def countBits(n):
    return bin(n).count("1")
       
