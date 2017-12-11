

myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split(",")
#print(contents)

def howfarishe(contents):
    x = 0
    y = 0
    z = 0
    dmax = 0
    for c in contents:
        if c == "n":
            y += 1
            z -= 1
        elif c == "ne":
            x += 1
            z -= 1
        elif c == "se":
            x += 1
            y -= 1
        elif c == "s":
            y -= 1
            z += 1
        elif c == "sw":
            x -= 1
            z += 1
        else:
            x -= 1
            y += 1
        if (abs(x)+abs(y)+abs(z))/2 > dmax:
            dmax = (abs(x)+abs(y)+abs(z))/2
    
    print(dmax)
    
howfarishe(contents)