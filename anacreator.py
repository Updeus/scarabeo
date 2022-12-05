with open ('words.txt') as words:
	dict={}
	for word in words:
		word=word.strip()
		if (len(word)>2 and len(word)<8):
			key = ''.join(sorted(word))
			if key in dict:
				dict[key].append(word)
			else :
				dict[key]= [word]
anadict = [' '.join([key]+value) for key, value in dict.items()]
anadict.sort()
with open('anadict.txt','w') as f:
	f.write('\n'.join(anadict))
