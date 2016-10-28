

import time, math
s = time.time()

def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	
	i = 3
	range = int( math.sqrt(n) ) + 1
	while( i < range ):
		if( n % i == 0):
			return 0
		i += 1
	return 1
	
N,T = 1,3
while N < 10001:
	if IsPrime(T):
		N+=1
	T+=2

print(T)
	
##
#prime_list = [2,3,5,7,11,13]
#max_index = 6
#start_value = 14

#while max_index < 10001:
#	prime_check = 1
	
#	for i in prime_list:
#		if start_value % i == 0:
#			prime_check = 0
#			break
		
#	if prime_check == 1:
#		prime_list.append(start_value)
#		print(start_value)
#		max_index += 1

#	start_value += 1

