menu = """
        Pick a menu option!
---------------------------------------------------------
	1 Reverse a string
	3 Find minimum value inside a list
	4 Find the Maximum value inside a list
	5 Calculate a remainder
	6 Return distinct values of a list
	8 Add a string of variables
	9 Exit
	"""
while(True):

	print(menu)
	choice = input()

	if choice == "1":
		print ("enter your words")
		string = input()

		string_reversed = string[-1::-1]
		print(string_reversed)
	elif choice == "3":
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

	elif choice == "4":
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
					print("The one to rule them all is: " + str(high))
					break
				else:
					print("Tell me your number, puny human. Whenever you are finished simly press eter without typing a number!")
					break
	elif choice == "5":
			def question5():
				num = int(input("Input a numerator:"))
				div = int(input("Now input a divisor:"))

				result = num % div
				print("Your result is:", result)

			question5()
	elif choice == "6":
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

	elif choice == "8":
			print ("enter a")
			a = input()
			print ("enter b")
			b = input()
			print ("enter c")
			c = input()
			print ("enter d")
			d = input()
			sum = float(a) + float(b) + float(c) - float(d)
			print ("A+B+C-D equals",sum)

	elif choice == "9":
			break
