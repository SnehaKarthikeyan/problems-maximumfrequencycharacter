Coding:

test_str = str(input())
all_freq = {}
for i in test_str:
    if i!=" ":
     if i in all_freq:
        all_freq[i] += 1
     else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get) 
print (str(res))
