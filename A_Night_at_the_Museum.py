n = input()
total = 0
current = 'a' 
for char in n:
    diff = abs(ord(char) - ord(current))
    total += min(diff, 26 - diff)
    current = char
print(total)