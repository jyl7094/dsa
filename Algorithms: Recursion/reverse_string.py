def reverse_string_recursive(s):
    if type(s) != str:
        raise TypeError
    if len(s) == 0:
        return ''
    return s[-1] + reverse_string_recursive(s[:-1])


def reverse_string_iterative(s):
    if type(s) != str:
        raise TypeError
    reverse = ''
    for i in range(len(s)-1, -1, -1):
        reverse += s[i]
    return reverse
