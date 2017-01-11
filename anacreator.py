words = open ('words.txt')
dict={}
for word in words:
	word=word.strip()
	if (len(word)>2 and len(word)<8):
		key = ''.join(sorted(word))
		if key in dict:
			dict[key].append(word)
		else :
			dict[key]= [word]
words.close()
anadict = [' '.join([key]+value) for key, value in dict.items()]
anadict.sort()
f = open('anadict.txt','w')
f.write('\n'.join(anadict))
f.close()
