def MyFunc(inp:list) -> tuple:
	if len(inp) == 0:
		return 0  
	total_int = 0
	count_int = 0
	'''
	 Intializing the variable with the smallest negative int of 64 bits
	 However this approach doesnot hold in python 3 as int is ubnound
	 An alternative approach would be useing numpy's -np.inf
	'''
	max_float = 2^(63) - 1  
	for element in inp:
		if isinstance(element,int) and element%2 == 0:
			total_int += element 
			count_int += 1
		elif isinstance(element,float):
			max_float = element if element > max_float else max_float
	mean_even_int = 0 if count_int == 0 else total_int/count_int
	return max_float,mean_even_int
q

