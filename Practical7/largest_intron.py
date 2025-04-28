import re
#set the sequence
seq = "ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA"
#find the longest sequence GT AG by using greedy match
target = re.findall(r'GT.+AG',seq)
print(target)
#find the length of seqence
#shift the target from list to str
l=''.join(map(str, target))
print(len(l))