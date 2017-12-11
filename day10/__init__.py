myfile = open('input.txt', 'r')
contents = myfile.read()
myfile.close()

contents = contents.strip()
ascii = [ord(x) for x in contents]
ascii += [17, 31, 73, 47, 23]

    

contents = contents.split(",")
contents = [int(x) for x in contents]

seq = list(range(256))
testseq = list(range(5))
testinput = [3,4,1,5]



def hash_one(input):
    seq = list(range(256))
    skip = 0
    start = 0
    for x in input:
        
        z = x - 1
        if x % 2 == 0:
            iterating = list(range(start,start + int(x/2)))
        else:
            iterating = list(range(start,start + int(x/2) + 1))
        for y in iterating:
            seq[y % len(seq)],  seq[(y + z) % len(seq)] = seq[(y + z) % len(seq)] , seq[y % len(seq)]
            z -= 2
        start = (start + x + skip) % len(seq)
        skip += 1    
        
    return seq

def hash_zwei(input):
    seq = list(range(256))
    skip = 0
    start = 0
    for i in range(64):
        for x in input:
            z = x - 1
            if x % 2 == 0:
                iterating = list(range(start,start + int(x/2)))
            else:
                iterating = list(range(start,start + int(x/2) + 1))
            for y in iterating:
                seq[y % len(seq)],  seq[(y + z) % len(seq)] = seq[(y + z) % len(seq)] , seq[y % len(seq)]
                z -= 2
            start = (start + x + skip) % len(seq)
            skip += 1    
    
    resstring = ""
    for i in range(16):
        res = 0
        for j in range(16):
            res = res ^ seq[16*i + j]
        resstring += "%0.2x" % res
    
    return resstring

def hash_two(lengths):
    rope = list(range(256))
    pos = 0
    skip = 0
    for i in range(64):
        for length in lengths:
            if pos + length <= len(rope):
                begin = rope[:pos]
                middle = rope[pos:pos + length]
                end = rope[pos + length:]
                rope = begin + middle[::-1] + end
            else:
                begin = rope[:(pos + length) % len(rope)]
                middle = rope[(pos + length) % len(rope):pos]
                end = rope[pos:]
                count = len(end)
                sel = end + begin
                sel = sel[::-1]
                rope = sel[count:] + middle + sel[:count]

            pos = (pos + length + skip) % len(rope)
            skip += 1
    
    dense = ''
    for i in range(0,256,16):
        nums = rope[i:i + 16]
        result = int(eval(' ^ '.join([str(x) for x  in nums])))
        dense += "{:02x}".format(result)

    return dense
    
print("mine: ",hash_zwei(ascii))
print("his:",hash_two(ascii))


reslist = []
resstring = ""


