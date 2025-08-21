def substrings(s):
    substring = []

    count = 0

    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substring.append(s[i:j])
            count += 1
        return substring
    
s = input()
result = substrings(s)

for sub in substrings:
    print(sub)    


