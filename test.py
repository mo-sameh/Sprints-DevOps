from sprints import MyFunc

tests = [ 
[1,2,3,4,5,0.8],
[1,8,9,11,0.3,0.9],
[1,3,7,-0.2,0.0],
[2,-100.0,-0.94],
[]
]
results = [
(0.8,3),
(0.9,8),
(0.0,0),
(-0.94,2),
0
]

for i,test_case in enumerate(tests):
	assert MyFunc(test_case) == results[i] , "Failed in test case number {} with the following input {}".format(i+1,test_case)

print("Function has sucessfully passed {} test cases".format(len(tests))) 
