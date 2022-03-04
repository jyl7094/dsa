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


# test
assert reverse('a') == 'a'
assert reverse(2) == None
assert reverse('hello aloha') == 'ahola olleh'

assert reverse2('ab') == 'ba'
assert reverse2(3.14) == None
assert reverse2('hello aloha') == 'ahola olleh'
