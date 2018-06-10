
#generator function to return permutations of some strings:
#to do this in a generator must be recursive?
def stringPermutations(strings):
	#recursive base case, if the string list is empty, yield nothing:
	if(len(strings) is 0):
		yield ""

	def copyWithout(aList, aIndex):
		out = list(aList)
		del out[aIndex]
		return out

	#now we can start iterating:
	for index in range(len(strings)):
		for subPermutation in stringPermutations(copyWithout(strings, index)):
			yield strings[index] + subPermutation


array = ["one", "two", "three"]
array2 = ["one"]
array3 = []
array4 = ["how", "far", "will", "this", "scale?"]
#this one takes a LOOOONG time, but it does execute in constant ram.
array5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


for permutation in stringPermutations(array5):
	print permutation