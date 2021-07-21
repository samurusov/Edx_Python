fname = input("Enter File Name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for w in words:
        if w in lst: continue
        else:
        	lst.append(w)
lst.sort()
print (lst)