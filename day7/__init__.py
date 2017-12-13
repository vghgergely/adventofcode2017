myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
allprograms = [x[0:x.find(" ")] for x in contents]
complete = list(contents)

topprograms = []
weights = {}
tops = {}
bottoms = []


        

for x in complete:
    progweights = []
    bottom, top = x[0:x.find(" ")] , x[x.find(">") + 1:]
    weights[bottom] = int(x[x.find("(")+1:x.find(")")])
    
    if x.find(">") != -1:
        progs = top.split(",")
        progs = [top.strip() for top in progs]
        
        tops[bottom] = progs
        for y in progs:
            progweights.append(weights[y])
        bottoms.append(bottom)
        if progweights[1:] != progweights[:-1]:
            
            
        topprograms += progs
        

for x in allprograms:
    
    if x not in topprograms:
        print(x)


        