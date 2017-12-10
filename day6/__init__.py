myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split()
contents = [int(x) for x in contents]
print(contents)



def blockDistributor(blocks):
    seen = []
    result = 0
    firsts = {}
    while True:
        i = blocks.index(max(blocks))
        j = blocks[i]     
        blocks[i] = 0
        if i + 1 > len(blocks) - 1:
            i = 0
        else:
            i += 1
        while j > 0:
            
            
            blocks[i] += 1
            
            if i == len(blocks) - 1:
                i = 0
            else:
                i += 1
            j -= 1
            
        next = list(blocks)
        if next in seen:
            partone = result + 1
            return result + 1 - firsts[tuple(next)]
        seen.append(next)
        
        result += 1
        firsts[tuple(next)] = result
        
            
test = [0,2,7,0]

print(blockDistributor(contents))

