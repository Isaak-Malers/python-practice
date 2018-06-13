import random

# best case
array1 = [1, 1, 2]



def arrayGenerator(length):
	#build an output
	out = []
	#fill it with subsequent values
	for i in range(1, length):
		out.append(i)
	#append a random duplicate
	duplicate = random.randint(1, length-1)
	out.append(duplicate)
	#randomize the output.
	random.shuffle(out)

	return [duplicate, out]




def dupFinder(array):
	pointer = 0
	while True:
		print array
		#do logic here:
		#print pointer
		#if we have found our "special number"
		if array[pointer]  == None:
			#print "found None"
			return pointer

		#if we haven't found our special number, set pointer to the value of anArray:
		temp = array[pointer]
		array[pointer] = None
		pointer = temp


print dupFinder(array1)


"""
for i in range(0, 50000):
	seed = arrayGenerator(5)
	array = list(seed[1])
	answer = seed[0]

	caluclated = dupFinder(array)

	if(caluclated != answer):
		print "failed for:"
		print seed
		print "returned: " + str(caluclated)
"""