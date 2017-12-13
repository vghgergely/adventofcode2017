


from collections import *
from functools import reduce
import itertools
import sys
import random

myfile = open("input.txt","r")
contents = myfile.read()
myfile.close()

contents = contents.strip().split('\n')

def main(contents):
    
    graph = defaultdict(list)
    for line in contents:
        
        words = line.strip().split()
        a = int(words[0])
        bs = map(lambda x: int(x.strip(',')), words[2:])
        
        for b in bs:
            graph[a].append(b)
            graph[b].append(a)
    
    vis = set()
    res = 0
    for i in range(2000):
        if i in vis:
            continue
        q = [i]
        while q:
            a = q.pop()
            for b in graph[a]:
                if b not in vis:
                    vis.add(b)
                    q.append(b)
        res += 1
    print(res)
    

main(contents)