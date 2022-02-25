from hogre_dimensioner_catalantal_multitdimensional_list	import N_Dim_list
from hogre_dimensioner_catalantal_utilities	import *

# === ARGUMENTS ===
GLOBAL_D  			= 6			# SUPPORT MAX 27 (the amount of letters in variable ABC)
GLOBAL_N  			= 6			# AS HIGH AS YOU HAVE TIME FOR
USE_DP 				= True		# Use DP to speed up the algoritm (disables the output of all posible paths)
STORE_PATHS_DEBUG 	= False		# Store every possible path to same file (overwrites itself) (only useful if debug mode is on and USE_DP is False)
COMP_TO_FORMULA 	= True		# Whether or not the result of the DFS should be compared to the formula in the function C_vd() defined in the utilities file 
TEST_ONLY_ONE_D 	= False		# Whether or not only test one univers of GLOBAl_D (instead of <= GLOBAL_D)

# === CONSTANTS ===
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# === DFS-SPECIFIC GLOBAL CONSTANTS ===
AMOUNT_OF_DIMENSIONS 	= GLOBAL_D									# Stores the amount of dimensions for the specific universe (incase TEST_ONLY_ONE_D is False)
DIMENSIONS 				= [0 for _ in range(AMOUNT_OF_DIMENSIONS)]	# Stores the size of the grid in the diffrent dimensions (all values are the same for now)
PATH_BUFFER 			= []										# Stores paths in a list (only used if STORE_PATHS_DEBUG is True)
PATH_SET 				= set()										# Stores paths in a set so it can be compared with PATH_BUFFER (only used if STORE_PATHS_DEBUG is True)

DP = N_Dim_list()		# The DP list (a n-dimensions list object)

# === DFS ===
def cata_vd_DFS(position:list, path:str = ""):
	
	# return if arrived in the other corner
	if position == DIMENSIONS: 
		if not USE_DP:
			PATH_BUFFER.append(path)
			PATH_SET.add(path)
		return 1
	
	# return if already visited this point
	if USE_DP:
		if DP.getValue(position) != -1:
			return DP.getValue(position)

	# variable to store total amount of paths from this point
	out = 0

	# move one step in the first dimension and add the amount of paths found
	if position[0] < DIMENSIONS[0]:
		out += cata_vd_DFS(
			moveOneStepInDimension(0, position),
			path + ABC[0]
			)

	# move one step in the other dimension and add the amount of paths found
	for i in range(1, AMOUNT_OF_DIMENSIONS):
		if position[i] < DIMENSIONS[i]:
			if position[i] != position[i-1]:
				out += cata_vd_DFS(
					moveOneStepInDimension(i, position),
					path + ABC[i]
					)
	
	# store total amount of paths from this point
	if USE_DP: 
		DP.setValue(position, out)

	# return total amount of paths from this point
	return out

# === DRIVER CODE FOR DFS ===
def runForDimensions():
	# declare global variables just to be safe
	global DIMENSIONS, PATH_BUFFER, PATH_SET, DP
	# loop for every element n < GLOBAL_N
	for size in range(0, GLOBAL_N):
		# specify dimensions
		DIMENSIONS  = [size for _ in range(AMOUNT_OF_DIMENSIONS)]
		# clear global variables for next DFS
		PATH_BUFFER = []
		PATH_SET	= set()
		DP.create([dimension + 1 for dimension in DIMENSIONS])

		# run DFS
		amount = cata_vd_DFS([0 for _ in range(AMOUNT_OF_DIMENSIONS)])

		# result from formula
		f_amount = C_vD(AMOUNT_OF_DIMENSIONS, size)

		# print result
		print(
			str(size) if size >= 10 else " " + str(size), 					 # The number describing n (with a space added if n < 10)
			"" if USE_DP else "p:" + str(len(PATH_BUFFER) == len(PATH_SET)), # If the code stores all of the paths, T/F depending on if there are no duplicate 
			"vd:" + str(amount == f_amount) if COMP_TO_FORMULA else "",		 # If the COMP_TO_FORMULA flag is True, T/F depending on if the DFS return the same as the formula
			" - ",
			amount
			)
		# export result to file (for debug)
		if STORE_PATHS_DEBUG: exportToTxt(PATH_BUFFER, "VD_DEBUG_DATA")


def runForUniverse(amountOfDimensions:int):
	# print header
	print(f"=== Amount of Dimensions = {amountOfDimensions} ===")
	# assign amountOfDimensions to the global variable
	global AMOUNT_OF_DIMENSIONS
	AMOUNT_OF_DIMENSIONS = amountOfDimensions
	# run for every n
	runForDimensions()

# because forloops only run for 0, 1, 2, ... i-1 and not i 
GLOBAL_N += 1
# if only one 'universe' should be tested
if TEST_ONLY_ONE_D:
	# LES' GO
	runForUniverse(GLOBAL_D)
else:
	# because forloops only run for 0, 1, 2, ... i-1 and not i 
	GLOBAL_D += 1
	# runs for every dimension from 2 (because a 0 and 1-dimension case is trivial) up to (and including) GLOBAL_D
	for dimSize in range(2, GLOBAL_D):
		# LES' GOOOO
		runForUniverse(dimSize)
