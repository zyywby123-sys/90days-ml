sentence = "the quick brown fox jumps over the lazy dog"
words=sentence.split()
longest=""
for w in words :
    n=len(w)
    if n > len(longest):
        longest=w
print(longest)
print(len(longest))