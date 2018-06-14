#import random for building randomized test cases:
import random
import time
#this is an array with the first million primes.  Not an ideal thing to have laying around.
#from rainbow import primes
#here is a shorter list of primes, for running small tests:
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149]


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
		if array[pointer] < 0:
			return pointer

		temp = array[pointer]
		array[pointer] = -array[pointer]
		pointer = temp


#using a rainbow table of primes, we can hopefully get it even faster:
def primeHack(array):
	product = 1
	for value in array:
		if(product % primes[value] == 0):
			return value
		product = product * primes[value]


#addition method:
def numericAddition(array):
	#curious if not using the sum method impacts performance greatly:
	total = 0
	for value in array:
		total = total+value
	total = sum(array)
	expected = (len(array)/2) * (1 + len(array)-2)
	return total-expected

#hashmap method:
def makeHashmap(array):
	#interestingly, pre-alocating the hasmap worsens performance in python...
	#checking if a key is IN a hashmap and growing it dynamically is the fastest solution.
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


#given a number of sets to run, the length of those sets, and a function:
#records performance metrics about how a function handles the problem.
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

runSample(100, 100000, huntAndPeck)
runSample(100, 100000, numericAddition)
runSample(100, 100000, makeHashmap)
runSample(100, 100000, orderHunt)


#Some performance metrics, in seconds, my virtual machine has 6GB ram, and 6 cores of a corei7:
#Interestingly, even though all the algorithms have similar complexity in theory,
#numeric-addition outperformes the others by a MASSIVE margin.


#other cool stuff:
#hunt-and-peck = CPU bound
#numeric-addition = CPU bound
#hash-map = Memory bound
#sorting = CPU bound
#primeHack = Memory bound

#I'm not really sure why the hash-map method is memory bound.
#The primehack method appears to be memory bound, 
#I suspect this is due to the large number handling in python being memory hard.


#500000 samples, 20 long each:
#hunt-and-peck:     2.94
#numeric-addition:   .75
#hash-map:          2.42
#orderHunt:         3.68
#primeHack:         3.14

#50000 samples, 200 long each:
#hunt-and-peck:     2.63
#numeric-addition:   .24
#hash-map:          2.17        
#orderHunt:         4.52
#primeHack:         7.11

#5000 samples, 2000 long each:
#hunt-and-peck:     2.67
#numeric-addition:   .18
#hash-map:          2.01
#orderHunt:         7.16
#primeHack:        39.85

#500 samples, 20000 long each:
#hunt-and-peck:     2.59
#numeric-addition:   .18
#hash-map:          3.15
#primeHack:       Longer than I care to wait.

#50 samples, 200000 long each:
#hunt-and-peck:     2.80
#numeric-addition:   .19
#hash-map:          3.20

#5 samples, 2000000 long each:
#hunt-and-peck:     4.09
#numeric-addition:   .30
#hash-map:          3.23    