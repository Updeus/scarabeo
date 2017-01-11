from itertools import combinations
from bisect import bisect_left

def loadanadict():
	f = open("anadict.txt")
	anadict = f.read().split('\n')
	f.close()
	return anadict

def findwords(rack, anadict):
  rack = ''.join(sorted(rack))
  foundwords = []
  for i in range(3,len(rack)+1):
    for comb in combinations(rack,i):
      ana = ''.join(comb)
      j = bisect_left(anadict, ana)
      if j == len(anadict):
        continue
      words = anadict[j].split()
      if words[0] == ana:
        foundwords.extend(words[1:])
  return foundwords

import sys
if len(sys.argv)==2:
	rack = sys.argv[1].strip()
else:
	print("Inserisci lettere")
	exit()
anadict = loadanadict()
print (findwords(rack, anadict))
