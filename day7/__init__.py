myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
allprograms = [x[0:x.find(" ")] for x in contents]
complete = list(contents)

topprograms = []
for x in complete:
    
    if x.find(">") != -1:
        x = x[x.find(">") + 1:]
        
        progs = x.split(",")
        progs = [x.strip() for x in progs]
        topprograms += progs
    
for x in allprograms:
    if x not in topprograms:
        print(x)
        