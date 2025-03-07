def get_book_text(file_path):
	with open(file_path) as f:
		# f is a file object
		file_contents = f.read()
	return file_contents


def word_count(text):
	n_words=len(text.split())
	return n_words

def char_distribution(text):
	charCounts={}

	for c in text:
		lc = c.lower()
		if lc in charCounts:
			charCounts[lc] += 1
		else:
			charCounts[lc]=1
	return charCounts

def sort_on(dict):
    return dict["count"]

def dict_to_list(d):
	l=[]
	for c in d:
		i={"character": "", "count":0}
		n = d[c]

		i["character"]=c
		i["count"]=n

		l.append(i)
		#print(f"'{c}': {n}")

	l.sort(reverse=True, key=sort_on)
	return l

def report(fp):

	contents=get_book_text(fp)
	num_words=word_count(contents)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {fp}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	print ("--------- Character Count -------")

	
	chars=char_distribution(contents)
	l=dict_to_list(chars)
	l.sort(reverse=True, key=sort_on)

	for d in l:

		if d["character"].isalpha():
			print(f"{d['character']}: {d['count']}")

	print("============= END ===============")