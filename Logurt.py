def numbersix():
	result = set(input("Gimme ya list of numbers homie! "))
 
	dup_items = set()
	uniq_items = []
	for x in result:
		if x not in dup_items:
			uniq_items.append(x)
			dup_items.add(x)

	print(dup_items)	

numbersix()

