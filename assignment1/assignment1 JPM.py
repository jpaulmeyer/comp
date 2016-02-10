#J.Paul Meyer
#Pset1.py
import string

def swapchars(input_string):
    freq_dict = {}
    input_string = input_string.lower()
    illegal_chars = [' ','"',"'",',','.','?','!']
    for char in input_string:
        if char not in illegal_chars and char not in freq_dict.keys():
            freq_dict[char] = input_string.count(char)
    freq_sorted_chars = freq_dict.keys()
    freq_sorted_chars.sort(key=lambda r: freq_dict[r])
    most = freq_sorted_chars[-1]
    least = freq_sorted_chars[0]
    out = ''
    for char in input_string:
        if char == most:
            out += least
        elif char == least:
            out += most
        else:
            out += char
    return out

if __name__ == '__main__':
    print swapchars('I\'m just a chi-town coder with a nice flow.')

def sortcat(num, *args):
    len_dict = {arg:len(arg) for arg in args}
    if num == -1:
        return ''.join(args)
    else:
        a = list(args)
        a.sort(key=lambda r:len(r))
        a.reverse()
        n = min(len(a),num)
        out = ''
        for i in range(n):
            out += a[i]
    return out

if __name__ == '__main__':
    print sortcat(2,'hey','wassup','hello')

with open('states.txt', 'r') as f:
    out = []
    for line in f:
        out.append(line.strip('\n'))
    #Format is {'AL':'Alabama'}
    abbrev = {state[-2:]:state[:-3] for state in out}

def unabbrev(state_abrv):
    return abbrev[state_abrv]

if __name__ == '__main__':
    print unabbrev('PA')

def abbrevify(state_name):
    return {val:key for key,val in abbrev.items()}[state_name]

if __name__ == '__main__':
    print abbrevify('Nebraska')

