def insertion_sort_other(l):
	for i in range(1, len(l)): 
		key = l[i] 
  
		j = i-1
		print(l) 

		while j >= 0 and key < l[j] :
			print("---------------------")
			print(l) 
			l[j + 1] = l[j] 
			j -= 1
			l[j + 1] = key 


	return l


def bubble_sort_other(l):

	n = len(l) -1

	while n>1:
			for j in range(n):
				
				if l[j] > l[j+1]:
						
					l[j], l[j+1]  = l[j+1], l[j] 
				