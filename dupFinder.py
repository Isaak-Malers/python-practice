#import random for building randomized test cases:
import random
import time



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
def huntAndPeck(array):
	pointer = 0
	while True:
		#print array
		if array[pointer]  == None:
			return pointer

		temp = array[pointer]
		array[pointer] = None
		pointer = temp

#addition method:
def numericAddition(array):
	total = sum(array)
	expected = (len(array)/2) * (1 + len(array)-2)
	return total-expected

#hashmap method:
def makeHashmap(array):
	#interestingly, pre-alocating the hasmap worsens performance in python...
	#checking if a key is IN a hashmap and growing it dynamically is the fastests solution.
	intermediate = {i: 1 for i in range(len(array))}
	for value in array:
		if intermediate[value] == 2:
			return value
		else:
			intermediate[value] = 2

def orderHunt(array):
	sort = sorted(array)
	for i in range(0, len(sort)):
		if(sort[i] == sort[i+1]):
			return sort[i]



def runSample(tests, size, function):
	print ""
	print "running " + str(tests) + " random tests with length " + str(size) + ":"
	print "using:  " + function.__name__

	timeTracker = 0

	for i in range(0, tests):
		seed = arrayGenerator(size)
		array = list(seed[1])
		answer = seed[0]

		start = time.time()
		caluclated = function(array)
		end = time.time()

		timeTracker = timeTracker + (end-start)

		if(caluclated != answer):
			print "failed for:"
			print seed
			print "returned: " + str(caluclated)

	print "total computation time: " + str(timeTracker)


array1 = [1, 2, 2]
array2 = [2, 1, 2]
array3 = [2, 2, 1]
# array[1] pointing to itself isn't a problem.
# because in order to GET to looking at array[1], we would have to go to a location with a value that is already one
# Just before the whole algorithm falls apart, it finds to solution.
badCase = [3, 1, 4, 2, 2]
veryGoodCase = [1, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]





#Some performance metrics, in seconds, my virtual machine has 6GB ram, and 6 cores of a corei7:
#Interestingly, even though all the algorithms have similar complexity in theory,
#numeric-addition outperformes the others by a MASSIVE margin.


#other cool stuff:
#hunt-and-peck = CPU bound
#numeric-addition = CPU bound
#hash-map = Memory bound
#sorting = CPU bound

#I'm not really sure why the hash-map method is memory bound.



#500000 samples, 20 long each:
#hunt-and-peck:     2.94
#numeric-addition:   .75
#hash-map:          2.42
#orderHunt:         3.68

#50000 samples, 200 long each:
#hunt-and-peck:     2.63
#numeric-addition:   .24
#hash-map:          2.17        
#orderHunt:         4.52

#5000 samples, 2000 long each:
#hunt-and-peck:     2.67
#numeric-addition:   .18
#hash-map:          2.01
#orderHunt:         7.16

#500 samples, 20000 long each:
#hunt-and-peck:     2.59
#numeric-addition:   .18
#hash-map:          3.15

#50 samples, 200000 long each:
#hunt-and-peck:     2.80
#numeric-addition:   .19
#hash-map:          3.20

#5 samples, 2000000 long each:
#hunt-and-peck:     4.09
#numeric-addition:   .30
#hash-map:          3.23    


#Uncomment to run a big sample:
runSample(50000, 200, huntAndPeck)
runSample(50000, 200, numericAddition)
runSample(50000, 200, makeHashmap)
runSample(50000, 200, orderHunt)