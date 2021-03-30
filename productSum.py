# algoexprert product Sum
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
	level = 1
	
	
	def helper(array, level, sum):
		# if array
		sum = 0
		for n in array:
			if type(n) is int:
				sum += n
				print(sum)
				
			else:
				print(n, level, sum)
				sum += helper(n, level+1, sum)
				
		# sum += sum * level
		print(sum)
		return sum * level
		
	return helper(array, level, sum)
		
		
