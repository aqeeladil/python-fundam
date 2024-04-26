# Example-3: Strings that starts with 'a' and ends with 'y'

options = ['any', 'hello', 'albany', 'apple', 'world', '']
ans = []

for s in options:
    if len(s) <= 1:
        continue
    if s[0] != 'a':
        continue
    if s[-1] != 'y':
        continue
    ans.append(s)

print(ans)


# Using list comprehension 

ans2 = [
    s
    for s in options
    if len(s) >= 2
    if s[0] == 'a'
    if s[-1] == 'y'
]

print(ans2)