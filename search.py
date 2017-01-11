from itertools import combinations
from bisect import bisect_left

def loadanadict():
	#f = open("anadict.txt")
	#anadict = f.read().split('\n')
	#f.close()

	anadict = {}
	with open('anadict.txt','r') as txt:
		for line in txt:
			items = line.split()
			key,values = items[0], items[1:]
			anadict.setdefault(key,[]).extend(values)
	return anadict

def findwords(rack, anadict):
	rack = ''.join(sorted(rack))
	foundwords = set()
	for i in range(3,len(rack)+1):
		for comb in combinations(rack,i):
			anagram = ''.join(comb)
			if anagram in anadict:
				for word in anadict[anagram]:
					foundwords.add(word)
#	  		if (anagram in anadict):
#				foundwords.append(anadict[anagram])
	return foundwords

import sys
if len(sys.argv)==2:
	rack = sys.argv[1].strip()
else:
	print("Inserisci lettere")
	exit()
anadict = loadanadict()
#print (anadict)
result = (findwords(rack, anadict))
result = list(result)
result.sort( key = len)
for word in result:
	print (word)
