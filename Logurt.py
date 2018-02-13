def numbersix():
	result = set(input("Give a list of numbers, please! ")) 
	dup_items = set()
	uniq_items = []
	for x in result:
	if x not in dup_items:
	uniq_items.append(x)
	dup_items.add(x)

	print(dup_items)	

numbersix()

