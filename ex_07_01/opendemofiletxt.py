f = open('demofile.txt')

for lx in f:
    ly = lx.rstrip()
    print(ly.lstrip())
