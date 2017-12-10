myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')
contents = [int(x) for x in contents]

#print(contents)
def jumpyMaze(list):
    pos = 0
    steps = 0
    temp = 0
    incr = True
    while True:
        
        if list[pos] >= 3:
            incr = False
        temp = pos
        pos = pos + list[pos]
        if pos > (len(list) -1) or pos < 0:
            return steps + 1
        if incr:    
            list[temp] = list[temp] + 1
        else:
            list[temp] = list[temp] - 1
        steps += 1
        
        incr = True
        
list = [0, 3, 0, 1, -3]
#print(jumpyMaze(list))
print(jumpyMaze(contents))