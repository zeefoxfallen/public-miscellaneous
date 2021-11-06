file = open("input.txt","rt")
f = file.read()
flist = f.split(". ")

shortest = 999999999999999999999999999999
longest = 0

for sentence in flist:
    length = len(sentence)
    if length < shortest:
        shortest = length
    if length > longest:
        longest = length

print("the shortest was {} characters".format(shortest))
print("the longest was {} characters".format(longest))