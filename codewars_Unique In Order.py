def unique_in_order(seq):
    unique_list = []
    prev = None
    for i in seq:
        if i != prev:
            unique_list.append(i)
            prev = i
    return unique_list

#print(unique_in_order('AAAABBBCCDAABBB'))