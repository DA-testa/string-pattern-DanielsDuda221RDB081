# python3

def read_input():
    text = input()
    if "I" in text:
        pattern = input()
        text = input()
    elif "F" in text:
        text2 = input()
        if "a" in text2:
            return()
        with open ("tests/"+text2, encoding="utf-8") as fails:
            pattern = fails.readline()
            text = fails.readline()
            
    else:
        return()
    
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    a = len(pattern)
    b = len(text)
    c = 13
    d = 256
    p_hash=0
    t_hash=0
    result = []
    multiplier = 1
    
    for i in range(1,a):
        multiplier = (multiplier*d) % c
        
    #Rēķinam hash vertību paternam un tekstam 
    for i in range(a):
        p_hash = (d*p_hash+ord(pattern[i])) % c
        t_hash = (d*t_hash+ord(text[i])) % c
        
    #Meklējam sakritības tekstā
    for i in range(b - a + 1):
        if p_hash == t_hash:
            for j in range(a):
                if text[i+j]!=pattern[j]:
                    break
            if j == a-1:
                result.append(i)
        #Ja nav teksta beigas, atjaunojām t_hash vertību
        if i < b - a:
            t_hash = (d*(t_hash-ord(text[i])*multiplier)+ord(text[i+a])) % c

    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

