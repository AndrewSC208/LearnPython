val = [False, False, False, False, False, True, True]

def getCEOStatus(x):
	ceoStatus = False
	i = 0
	while (i < 6):
		print i
		if x[i] == True:
			ceoStatus = True
		
		i = i + 1 #end while loop

	print ceoStatus
	return ceoStatus

getCEOStatus(val)