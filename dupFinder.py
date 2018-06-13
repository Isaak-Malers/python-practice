#import random for building randomized test cases:
import random

#this will generate an array and solution randomly
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


#this is the actual algorithm:
def dupFinder(array):
	pointer = 0
	while True:
		#print array
		if array[pointer]  == None:
			return pointer

		temp = array[pointer]
		array[pointer] = None
		pointer = temp

def runSample(tests, size):
	print ""
	print "running 5000 randomly generated tests on larger datasets, only failures will print:"
	for i in range(0, 5000):
		seed = arrayGenerator(5000)
		array = list(seed[1])
		answer = seed[0]

		caluclated = dupFinder(array)

		if(caluclated != answer):
			print "failed for:"
			print seed
			print "returned: " + str(caluclated)


array1 = [1, 2, 2]
array2 = [2, 1, 2]
array3 = [2, 2, 1]
# array[1] pointing to itself isn't a problem.
# because in order to GET to looking at array[1], we would have to go to a location with a value that is already one
# Just before the whole algorithm falls apart, it finds to solution.
badCase = [3, 1, 4, 2, 2]
veryGoodCase = [1, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]

print "running some explicit tests"
print array1
print dupFinder(array1)
print array2
print dupFinder(array2)
print array3
print dupFinder(array3)
print badCase
print dupFinder(badCase)
print veryGoodCase
print dupFinder(veryGoodCase)

#Uncomment to run a big sample:
#runSample(500, 500)