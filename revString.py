def rev_string(string):
    newString = ""
    for i in range (len(string) - 1, -1, -1):
        newString += newString.join(string[i])
    return newString

print(rev_string("hello"))