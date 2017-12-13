
myfile = open("input.txt","r")
contents = myfile.read()
myfile.close()
 
contents = contents.strip().split("\n")
contents = [x.split(": ") for x in contents]
 
layers = {}
for x in contents:
    layers[int(x[0])] = int(x[1])
 
last = list(layers.keys())[-1]
severity = 1

ok = False
val = 0
while not ok:
    ok = True
    for i in layers.keys():
        k = layers[i]
        if (i + val) % (2*k-2) == 0:
            ok = False
            val += 1
            break
    
    
     
 
print(val)

