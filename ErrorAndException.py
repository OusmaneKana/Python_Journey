def provide_int():
	while True:
		try:
			number = int(input("Please put an integer: "))
		except:
			print("I asked for an integer you moron!!")
		else:
			print("Thank you for the input")
			break
		# finally:
		# 	print("End of operation")

provide_int()