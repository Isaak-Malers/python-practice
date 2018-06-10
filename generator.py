
#generator function to return permutations/combinations of some strings:
def stringPermutations(strings, outputLength=None, combine=False):
	#sanatize and handle inputs
	if(outputLength is None):
		outputLength = len(strings)

	#First define some helper fuctions:
	#copyWithout returns a copy of a list, sans the value at whatever aIndex is.
	def copyWithout(aList, aIndex):
		assert aIndex > -1, "copyWithout was called with a negative value for index"
		out = list(aList)
		del out[aIndex]
		return out


	#now on to the meat of the function:


	#recursive base case, if the string list is empty, yield nothing:
	if(len(strings) is 0):
		yield ""

	#ensure that we don't exceed the output length, this case is non recursive but still must iterate.
	if(outputLength is 1):
		for string in strings:
			yield string

	#if we don't have to worry about the outputLength:
	#iterate through all the strings, but ALSO append the value of the recursive function call:
	else:
		for index in range(len(strings)):
			if(combine is False):
				for subPermutation in stringPermutations(list(strings), outputLength-1, combine):
					yield strings[index] + subPermutation

			#if combining is true, we run the same code as above but we use the copyWithout function:
			else:
				for subPermutation in stringPermutations(copyWithout(strings, index), outputLength-1, combine):
					yield strings[index] + subPermutation


#array test cases:
array = ["one", "two", "three"]#short enough to verify by hand
array2 = ["one"]#test single case
array3 = []#test empty case
array4 = ["how", "far", "will", "this", "scale?"]#test something kinda long
array5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#test something really long

#calculate how many results were returned, so that I can verify the math on this guy:
results = 0
for permutation in stringPermutations(array5, 3, combine=True):
	print permutation
	results += 1
print "calulated " + str(results) + " permutations"