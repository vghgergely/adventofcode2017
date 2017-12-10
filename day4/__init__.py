myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
contents = [x.split() for x in contents]


def isValid(contents):
    
    good = 0
    better = 0
    for phrase in contents:
        sorteds = []
        for word in phrase:
            sortedword = sorted(word)
            
            sorteds.append(''.join(sortedword))
            
        if len(sorteds) == len(set(sorteds)):
            better += 1
        
        if len(phrase) == len(set(phrase)):
            good += 1
            
    return better
    
print (isValid(contents))