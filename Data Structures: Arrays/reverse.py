# reverse string
def reverse(string):
    if type(string) != str:
        return None
    
    lst = []
    
    for i in range(len(string)-1, -1, -1):
        lst.append(string[i])
    
    return ''.join(lst)

def reverse2(string):
    if type(string) != str:
        return None
    return string[::-1]
