count = 0
x = []
while(True):
	num = input('Tell me your number, puny human. Whenever you are finished simply press enter without typing a number!: ')
	if(num.isdigit()):
		x.append(int(num))
		count += 1
	elif(x):
		high = max(x)
		low = min(x)
		print("The weakest among you seems to be: " + str(low))
		break
	else:
		print("Tell me your number, puny human. Whenever you are finished simly press eter without typing a number!")
		break
