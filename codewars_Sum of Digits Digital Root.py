#способ chatgpt
def digital_root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n       
print(digital_root(942))


#способ, по которому можно решить
def digital_root(n):
    j = 0
    while n > 9:
        for i in str(n):
            j += int(i)
        n = j
        j = 0
    return n