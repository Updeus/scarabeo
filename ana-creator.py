words = open ('words.txt')
dict={}
i=0
for word in words:
	word=word.strip()
	if (len(word)>2 and len(word)<7):
		key = ''.join(sorted(word))

		i+=1
		if i > 10: break

		if key in dict:
			#print(key)
			dict[key].append(word)
		else :
			dict[key]= [word]

words.close()
anadict = [' '.join([key]+value) for key, value in dict.items()]
anadict.sort()
f = open('anadict.txt','w')
f.write('\n'.join(anadict))
f.close()
