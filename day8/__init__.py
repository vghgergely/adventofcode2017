myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
contents = contents.split('\n')

from collections import defaultdict

dict = defaultdict(int)
maxval = 0

for phrase in contents:
    var1, instruction, val1, _, var2, operator, val2 = phrase.replace("\n","").split()
    if eval(str(dict[var2]) + operator + val2):
        if instruction == "inc":
            dict[var1] += int(val1)
            
            if dict[var1] > maxval:
                maxval = dict[var1]
        else:
            dict[var1] -= int(val1)
            if dict[var1] > maxval:
                maxval = dict[var1]
print( max(dict.values()))
print(maxval)
