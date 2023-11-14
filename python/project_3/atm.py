# Script name: atm.py
# Purpose: an Automated Teller Machine (atm) simulation that allows users to perform basic financial transactions
# Author: Ogunsanya Louis Similoluwa 236345

# importing modules
# random module to pick random quotes from the 'quote' list
import random
# the shelve module provides a persistent storage system for Python objects, allowing you to save and retrieve data between sessions
# the shelve module is essential to store up the details of users (account holders) and to enable easy retrieval of user data
# it is crucial for creating accounts and for easy interaction between multiple accounts as in the transfer menu
import shelve

# Start: 5:28 pm 3/11/23

# functions are used in this code to allow easy movement between menus, to make the code consice and
# to avoid repitions that could lead to an unreasonably lenghty code

# 'quotes' a list containing the qualities of the bank to be printed when new users attempt to create accounts
quotes = ["Did you know the ABC Bank of Nigeria is the First and the Best Bank in Nigeria", 
          "Did you know that ABC Bank of Nigeria offers personalized financial solutions tailored to your unique needs?", 
          "Did you know that we here ABC value our customer privacy to the utmost", 
          "Did you know that ABC Bank of Nigeria is committed to fostering financial literacy through educational programs and resources?", 
          "Did you know that ABC Bank of Nigeria employs cutting-edge technology to ensure secure and convenient banking experiences for its customers?", 
          "Did you know that ABC Bank of Nigeria provides a range of innovative digital banking services to enhance your financial convenience?"]

# customer service menu
# Time spent: 5 mins
def customer_services():
    print("-" * 38)
    print("\tContact us trough the following numbers if you have any issues: 09052423929, 08080017464")
    print("\tOr Email us at ABCnaija@gmail.ng or at ogunsanyalouis@gmail.com")
    print("-" * 38)
    while True:
        go_back = input("Enter 0 to return to main menu: ")
        if go_back == "0":
            main()
            break

# account_settings menu containing code for user to carry out basic account settings
# Time spent 5hrs
def account_settings():
	print("-" * 38)
	while True:
		print("Account Settings:")
		print("\t1 - My Account Details")
		print("\t2 - Change Pin")
		print("\t3 - Change Phone number")
		print("\t4 - Contact Us")
		print("\t5 - Exit")
		print("-" * 38)

		choice = input("Enter an option: ")

		# asks user to confirm their pin and if correct prints out the user details
		if choice == "1":
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data') as acc_holder:
				user_data = acc_holder[acc_num]
				if pin == "0":
					account_settings()
				if pin == '':
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
						if pin != '':
							break
				if pin != user_data["Pin"]:
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
							break
						if pin == '':
							while True:
								pin = input("Enter a valid pin or 0 to return: ")
								if pin == "0":
									account_settings()
									break
								if pin != '':
									break
				print("-" * 38)
				print("Name:", user_data["First Name"], user_data["Last Name"])
				print("Account Number:", user_data["Account number"])
				print("Phone Number:", user_data["Phone number"])
				print("Date of Birth:", user_data["Birth date"])
				print("Account Balane:", user_data["Balance"])
				print("Pin:", user_data["Pin"])
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return: ")
					if go_back == "0":
						account_settings()
						break
		# asks user to confirm their pin and if the pin is correct it proceeds to changing the user pin
		elif choice == "2":
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data', writeback=True) as acc_holder:
				user_data = acc_holder[acc_num]
				if pin == "0":
					account_settings()
				if pin == '':
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
						if pin != '':
							break
				if pin != user_data["Pin"]:
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
							break
						if pin == '':
							while True:
								pin = input("Enter a valid pin or 0 to return: ")
								if pin == "0":
									account_settings()
									break
								if pin != '':
									break
				print("-" * 38)
				new_pin = input("Enter your new pin or 0 to cancel: ")
				if new_pin == "0":
					account_settings()
				if new_pin == '':
					while True:
						if new_pin == "0":
							account_settings()
							break
						if new_pin != '':
							break
						new_pin = input("Enter a valid pin or 0 to cancel: ")
				if new_pin.isdigit():
					while True:
						if pin == "0":
							account_settings()
							break
						if len(new_pin) == 5:
							break
						new_pin =  input("Pin must be 5 digits: ")
				else:
					while True:
						if new_pin.isdigit():
							while True:
								if pin == "0":
									account_settings()
									break
								if len(new_pin) == 5:
									break
								new_pin = input("Pin must be 5 digits: ")
							break
							new_pin = input("Pin must be 5 digit numbers: ")
				user_data["Pin"] = new_pin
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Pin changed succesfully")
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return: ")
					if go_back == "0":
						account_settings()
						break
		# asks user to confirm their pin and if correct proceeds to changing the user phone number
		elif choice == "3":
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data', writeback=True) as acc_holder:
				user_data = acc_holder[acc_num]
				if pin == "0":
					account_settings()
				if pin == '':
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
						if pin != '':
							break
				if pin != user_data["Pin"]:
					while True:
						pin = input("Enter a valid pin or 0 to return: ")
						if pin == "0":
							account_settings()
							break
						if pin == '':
							while True:
								pin = input("Enter a valid pin or 0 to return: ")
								if pin == "0":
									account_settings()
									break
								if pin != '':
									break
				print("-" * 38)
				phone_number =  input("Input your new Phone Number or 0 to cancel: ")
				if phone_number == "0":
					account_settings()
				if phone_number == '':
					while True:
						if phone_number == "0":
							account_settings()
							break
						if phone_number != '':
							break
						phone_number = input("Enter a valid Phone number or 0 to cancel: ")
				if phone_number.isdigit():
					while True:
						if phone_number == "0":
							account_settings()
							break
						if len(phone_number) == 11:
							break
						phone_number =  input("Enter a valid Phone Number of 0 to cancel: ")
				else:
					while True:
						if phone_number.isdigit():
							while True:
								if phone_number == "0":
									account_settings()
									break
								if len(phone_number) == 11:
									break
								phone_number =  input("Enter a valid Phone Number or 0 to cancel: ")
							break
						phone_number = input("Enter a valid Phone number or 0 to cancel: ")
				user_data["Phone number"] = phone_number
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Phone nmuber changed successfully")
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return: ")
					if go_back == "0":
						account_settings()
						break
		# customer service menu
		elif choice == "4":
			print("-" * 38)
			print("\tContact us trough the following numbers if you have any issues: 09052423929, 08080017464")
			print("\tOr Email us at ABCnaija@gmail.ng or at ogunsanyalouis@gmail.com")
			print("-" * 38)
			while True:
				go_back = input("Enter 0 to return: ")
				if go_back == "0":
					account_settings()
					break
		# exits the account settings menu
		elif choice == "5":
			transaction_menu()

# balance_menu function containing code to print the user account balance
# Time spent: 5 mins
def balance_menu():
	print("-" * 38)
	with shelve.open('user_data') as acc_holder:
		user_data = acc_holder[acc_num]
		print("Your Account Balance is: N",user_data["Balance"])
		print("-" * 38)
		while True:
			go_back = input("Enter 0 to return: ")
			if go_back == "0":
				transaction_menu()
				break

# transfer_menu function contains code for transferring amount to other account holders
# since the code cannot interact with other codes it is assumed that users can only transfer
# between users with accounts at the bank
# Time spent: 10hrs
def transfer_menu():
	print("-" * 38)
	# asks user for the account number they want to transfer to
	reciever_account = input("Enter the account number that you want to transfer to or 0 to cancel: ")
	if reciever_account == "0":
		transaction_menu()
	if reciever_account == '':
		while True:
			print("-" * 38)
			reciever_account = input("Enter a valid account number to proceed or 0 to cancel: ")
			if reciever_account == "0":
				transaction_menu()
				break
			if reciever_account != '':
				break
	# opens the shelve to check if inputed account number is an account holfer
	with shelve.open('user_data', writeback=True)as reciever:
		if reciever_account not in reciever:
			while True:
				print("-" * 38)
				print("Acount number does not exist")
				reciever_account = input("Enter a valid account number to transfer to or 0 to cancel: ")
				if reciever_account == "0":
					transaction_menu()
					break
				if reciever_account == '':
					while True:
						print("-" * 38)
						reciever_account = input("Enter a valid account number to proceed or 0 to cancel: ")
						if reciever_account == "0":
							transaction_menu()
							break
						if reciever_account != '':
							break
				if reciever_account in reciever:
					break
		# prints the name of the user with the inputed account number and
		# asks user for amount to transfer 
		reciever_data = reciever[reciever_account]
		print(reciever_data["First Name"], reciever_data["Last Name"])
		print("-" * 38)
		amount = input("Enter the amount you want to transfer or 0 to cancel: ")
		if amount == "0":
			transaction_menu()
		if amount == '':
			while True:
				print("-" * 38)
				amount = input("Enter a valid amount to proceed or 0 to cancel: ")
				if amount == "0":
					transaction_menu()
					break
				if amount != '':
					break

		def transfer():
			# this function checks if the amount entered is less than the user balance
			# if the amount is less it asks the user to confirm their pin to transfer the amount
			nonlocal amount, reciever_account
			with shelve.open('user_data', writeback=True)as acc_holders:
				user_data = acc_holders[acc_num]
				if int(amount) > user_data["Balance"] :
					while True:
						print("-" * 38)
						print("The amount you have entered is more than your balance")
						print("Your account balance is N",user_data["Balance"])
						print("-" * 38)
						amount = input("Please enter another amount or 0 to cancel: ")
						if amount == "0":
							transaction_menu()
							break
						if amount == '':
							while True:
								print("-" * 38)
								reciever_account = input("Enter a valid amount to proceed or 0 to cancel: ")
								if reciever_account == "0":
									transaction_menu()
									break
								if reciever_account != '':
									break
						if int(amount) <= user_data["Balance"]:
							break
				print("-" * 38)
				print("You are about to send N",amount, "to", reciever_data["First Name"], reciever_data["Last Name"])
				pin = input("Enter your pin to proceed or 0 to cancel: ")
				if pin == "0":
					transaction_menu()
				if pin == '':
					while True:
						pin = input("Enter a valid pin to proceed or 0 to cancel: ")
						if pin == "0":
							transaction_menu()
							break
						if pin != '':
							break
				if pin != user_data["Pin"]:
					trial = 0
					while trial <= 2:
						print("Invalid pin")
						pin = input("Enter your pin to proceed or 0 to cancel: ")
						if pin == "0":
							transaction_menu()
							break
						if pin == '':
							while True:
								pin = input("Enter a valid pin to proceed or 0 to cancel: ")
								if pin == "0":
									transaction_menu()
									break
								if pin != '':
									break
						if pin == user_data["Pin"]:
							break
				# deposits the amount into the recipient account
				balance = reciever_data["Balance"] + int(amount)
				reciever_data["Balance"] = balance
				reciever[reciever_account] = reciever_data
				# deducts the amount from the user account balance
				user_bal = user_data["Balance"] - int(amount)
				user_data["Balance"] = user_bal
				acc_holders[acc_num] = user_data
				# prints a success message to indicate that the transfer has been made
				print("-" * 38)
				print("Transfer Successful")
				print("Your account balance is N",user_data["Balance"])
				while True:
					print("-" * 38)
					go_back = input("Enter 1 to transfer again or 0 to return: ")
					if go_back == "0":
						transaction_menu()
					elif go_back == "1":
						transfer_menu()
		
		# checks if the inputed amount is digit 
		if amount.isdigit():
			transfer()
		else:
			while True:
				print("-" * 38)
				amount = input("Enter a valid amount to transfer or 0 to cancel: ")
				if amount == "0":
					transaction_menu()
				if amount == '':
					while True:
						print("-" * 38)
						amount = input("Enter a valid amount to proceed or 0 to cancel: ")
						if amount == "0":
							transaction_menu()
							break
						if amount != '':
							break
				if amount.isdigit():
					transfer()
					break

# withdrawal_menu function containing code for withdrawing from user account
# Time spent: 12hrs
def withdrawal_menu():
	print("-" * 38)

	# this function checks if the amount enterd by user is a digit
	def is_digit():
		nonlocal deduct
		amount = amount_1
		if amount == "0":
			withdrawal_menu()
		if amount == '':
			while True:
				print("-" * 38)
				amount = input("Enter a valid amount to withdraw or 0 to cancel: ")
				if amount == "0":
					withdrawal_menu()
					break
				if amount != '':
					break
		if amount.isdigit():
			if int(amount) in range(100, 100001):
				deduct = int(amount)
				withdraw_amount()
			else:
				while True:
					print("-" * 38)
					print("The amount must be a number between N100 and N100,000")
					amount = input("Enter an amount again to withdraw or 0 to cancel: ")
					if amount == "0":
						withdrawal_menu()
						break
					if amount.isdigit():
						if int(amount) in range(100, 100001):
							deduct = int(amount)
							withdraw_amount()
							break
		else:
			while True:
				print("-" * 38)
				print("The amount must be a number between N100 and N100,000")
				amount = input("Enter an amount again to withdraw or 0 to cancel: ")
				if amount == "0":
					withdrawal_menu()
					break
				if amount.isdigit():
					if int(amount) in range(100, 100001): 
						deduct = int(amount)
						withdraw_amount()
						break

	# this function takes the amount inputed by user, checks if the input is lesser than the user account balance and
	# carries out the transaction of withdrawing the amount from the user's account balance
	def withdraw_amount():
		nonlocal amount_1
		amount = deduct
		with shelve.open('user_data', writeback=True)as acc_holder:
			user_data = acc_holder[acc_num]
			if amount > user_data["Balance"]:
				print("-" * 38)
				print("The amount you have entered is greater than your account balance")
				amount_1 = input("Please enter an amount within the range of your balance :")
				is_digit()
			else:
				print("-" * 38)
				print("Your are about to withdraw the sum of N", amount)
				pin = input("Enter your pin to proceed or 0 to cancel: ")
				if pin == "0":
					withdrawal_menu()
				if pin == '':
					while True:
						pin = input("Enter a valid pin to proceed or 0 to cancel: ")
						if pin == "0":
							withdrawal_menu()
							break
						if pin != '':
							break
				if pin != user_data["Pin"]:
					trial = 0
					while trial <= 2:
						print("Invalid pin")
						pin = input("Enter your pin to proceed or 0 to cancel: ")
						if pin == "0":
							withdrawal_menu()
							break
						if pin == '':
							while True:
								pin = input("Enter a valid pin to proceed or 0 to cancel: ")
								if pin == "0":
									withdrawal_menu()
									break
								if pin != '':
									break
						if pin == user_data["Pin"]:
							break
				balance = user_data["Balance"] - amount
				user_data["Balance"] = balance
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Withdrawal successful")
				print("Your account balance is N", user_data["Balance"])
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return to transaction menu or 1 to withdraw again :")
					if go_back == "0":
						transaction_menu()
						break
					elif go_back == "1":
						withdrawal_menu()
						break

	print("Withdrawal menu")
	print("\t1 - N100")
	print("\t2 - N500")
	print("\t3 - N1,000")
	print("\t4 - N5,000")
	print("\t5 - N10,000")
	print("\t6 - N50,000")
	print("\t7 - Enter amount")
	print("\t8 - Exit")
	print("-" * 38)

	choice = input("Choose an option to withdraw: ")

	options = ["1", "2", "3", "4", "5", "6", "7", "8"]
	# while loop to keep asking user for input if input is not between 1 to 8
	while True:
		if choice in options:
			break
		choice = input("Choose an option between 1 and 8 to withdraw: ")
	if choice == '':
		while True:
			if choice != '':
				break
			choice = input("Choose an option between 1 and 8 to withdraw: ")
	if choice == "8":
		transaction_menu()
	elif choice == "1":
		deduct = 100
		withdraw_amount()
	elif choice == "2":
		deduct = 500
		withdraw_amount()
	elif choice == "3":
		deduct = 1000
		withdraw_amount()
	elif choice == "4":
		deduct = 5000
		withdraw_amount()
	elif choice == "5":
		deduct = 10000
		withdraw_amount()
	elif choice == "6":
		deduct = 50000
		withdraw_amount()
	elif choice == "7":
		# if user chooses to enter amount
		print("-" * 38)
		print("The minumum withdrawal amount is N100 and the maximum is N100,000")
		amount_1 = input("Enter an amount to withdraw of 0 to cancel: ")
		is_digit()

# deposit_menu function containing code for depositing into user account
# Time spent: 7hrs
def deposit_menu():
	print("-" * 38)
	# asks user to input deposit amount printing an error if input is invalid and cancelling if 0 is entered
	add_to_balance = input("Enter an amount to deposit or 0 to return: ")
	if add_to_balance == "0":
		transaction_menu()
	if add_to_balance == '':
		while True:
			add_to_balance = input("Enter a valid amount to deposit or 0 to return: ")
			if add_to_balance == "0":
				transaction_menu()
				break
			if add_to_balance != '':
				break
	if add_to_balance.isdigit():
		# after a valid amount is inputed, the shelve is openend in order to deposit into the user balance
		with shelve.open('user_data', writeback=True)as acc_holders:
			user_data = acc_holders[acc_num]
			balance = user_data["Balance"] + int(add_to_balance)
			user_data["Balance"] = balance
			acc_holders[acc_num] = user_data
			print("Deposit succesful")
			print("Your account balance is: N",user_data["Balance"])
			print("-" * 38)
			go_back = input("Enter 0 to return or 1 to deposit again: ")
			while True:
				if go_back == "0":
					transaction_menu()
				if go_back == "1":
					deposit_menu()
	else:
		# if input is not a digit
		while True:
			add_to_balance = input("Enter a valid amount to deposit of 0 to return: ")
			if add_to_balance == "0":
				transaction_menu()
				break
			if add_to_balance.isdigit():
				# if input is a valid digit it opens the shelve to deposit into the user account balance
				with shelve.open('user_data', writeback=True)as acc_holders:
					user_data = acc_holders[acc_num]
					balance = user_data["Balance"] + int(add_to_balance)
					user_data["Balance"] = balance
					acc_holders[acc_num] = user_data
					print("Deposit succesful")
					print("Your account balance is: N",user_data["Balance"])
					go_back = input("Enter 0 to return or 1 to deposit again: ")
					print("-" * 38)
					while True:
						if go_back == "0":
							transaction_menu()
						if go_back == "1":
							deposit_menu()
							break

# transaction_menu function containing the menu after user sign in 
def transaction_menu():
	while True:
		print("-" * 38)
		print("Transactions Menu:")
		print("\t1 - Deposit Funds")
		print("\t2 - Withdraw Funds")
		print("\t3 - Transfer Funds")
		print("\t4 - View my Balance")
		print("\t5 - Account Settings")
		print("\t6 - Exit")
		print("-" * 38)

		choice = input("Enter a choice: ")

		if choice == "1":
			# calls the deposit_menu function
			deposit_menu()
		elif choice == "2":
			# calls the withdrawal_menu function
			withdrawal_menu()
		elif choice == "3":
			# calls the transfer_menu function
			transfer_menu()
		elif choice == "4":
			# calls the balance_menu function
			balance_menu()
		elif choice == "5":
			# calls the account setting function
			account_settings()
		elif choice == "6":
			# at this point the current user exits and a welcome message is pritnted for the new user with the main menu
			print('\n')
			print("-" * 38)
			# prints in bold
			print("\033[1mWelcome to the ABC Bank of Nigeria\033[0m")
			# prints in italics
			print("\x1B[3mThe First Bank of Nigeria and the Best\x1B[0m")
			print("How can we help you today: ")
			print("-" * 38)
			# calls main function containing the main menu
			main()

# create_account function containing code for creating accounts with the bank
# Time spent: 7 hrs
def create_account():
	print("-" * 38)
	# makes acc_num accesible at other functions
	global acc_num
	# picks a random quote from the 'qoute' list and prints it in italics
	print("\x1B[3m" + random.choice(quotes) + "\x1B[0m")
	print("-" * 38)
	# 0 is added as an option at every point asking for input giving user freedom to quit at any point
	print("Welcome! Enter 0 at anytime to return to main menu")
	
	# asks user to input their first nameand last name exiting the menu if 0 is entered and 
	# printing an error if whitespaces are entered or if input is input is empty
	first_name = input("Input your First Name: ")
	if first_name == "0":
		main()
	if first_name == '':
		while True:
			first_name = input("Enter a valid First name: ")
			if first_name == "0":
				main()
			if first_name != '':
				break
	if first_name.isspace():
		while True:
			first_name = input("Enter a valid First name: ")
			if first_name == "0":
				main()
			if first_name == '':
				while True:
					first_name = input("Enter a valid First name: ")
					if first_name == "0":
						main()
					if first_name != '':
						break
			if not first_name.isspace():
				break
	# asks for last name
	last_name = input("Input your Last name: ")
	if last_name == "0":
		main()
	if last_name == '':
		while True:
			if last_name == "0":
				main()
			if last_name != '':
				break
			last_name = input("Enter a valid Last Name: ")
	if last_name.isspace():
		while True:
			last_name = input("Enter a valid First name: ")
			if last_name == "0":
				main()
			if last_name == '':
				while True:
					last_name = input("Enter a valid First name: ")
					if last_name == "0":
						main()
					if last_name != '':
						break
			if not last_name.isspace():
				break
	# asks user to input their phone number exiting menu if 0 is entered and
	# printing an error if user input is not an eleven digit number
	phone_number =  input("Input your Phone Number: ")
	if phone_number == "0":
		main()
	if phone_number == '':
		while True:
			if phone_number != '':
				break
			phone_number = input("Enter a valid Phone number: ")
	if phone_number != '':
		if phone_number.isdigit():
			while True:
				if len(phone_number) == 11:
					break
				phone_number =  input("Enter a valid Phone Number: ")
		else:
			while True:
				if phone_number.isdigit():
					while True:
						if len(phone_number) == 11:
							break
					phone_number =  input("Enter a valid Phone Number: ")
					break
				phone_number = input("Enter a valid Phone number: ")
	# asks user to input their date of birth exiting menu if 0 is entered and
	# printing an error if whitespaces are entered or if input is empty
	# dob is an acronym for date of birth
	dob = input("Enter your Date of Birth (dd/mm/yy): ")
	if dob == "0":
		main()
	if dob == '':
		while True:
			if dob == "0":
				main()
			if dob != '':
				break
			dob = input("Enter a valid Date of Birth: ")
	if dob.isspace():
		while True:
			dob = input("Enter a valid First name: ")
			if dob == "0":
				main()
			if dob == '':
				while True:
					dob = input("Enter a valid First name: ")
					if dob == "0":
						main()
					if dob != '':
						break
			if not dob.isspace():
				break
	# asks user to enter a transaction pin exiting menu if 0 is entered and
	# printing an error if pin is not a 5 digit number
	pin = input("Enter a 5 digits pin: ")
	if pin == "0":
		main()
	if pin == '':
		while True:
			if pin != '':
				break
			pin = input("Enter a valid pin: ")
	if pin != '':
		if pin.isdigit():
			while True:
				if len(pin) == 5:
					break
				pin =  input("Pin must be 5 digits: ")
		else:
			while True:
				if pin.isdigit():
					while True:
						if len(pin) == 5:
							break
						pin = input("Pin must be 5 digits: ")
					break
				pin = input("Pin must be 5 digit numbers: ")
	# creates an account number starting with 100 and ending with the last 7 digits of the phone number
	last7_digit_phonenum = int(phone_number) % 10000000
	acc_num = "100" + str(last7_digit_phonenum)
	# creates variable for storing user account balance and stores N1000
	acc_balance = 1000
	# puts all user details in a list 
	user_data = {
		"First Name": first_name,
		"Last Name": last_name,
		"Balance": acc_balance,
		"Phone number": phone_number,
		"Account number": acc_num,
		"Birth date": dob,
		"Pin": pin
	}
	# puts the list containing user details on a shelve thereby making it accessible between sessions and easy to access
	with shelve.open('user_data') as acc_holders:
		# saves the item on the shelve with the account number
		acc_holders[acc_num] = user_data
	# prints a welcome message and proceeds to the transaction menu
	print("-" * 38)
	print("Welcome,", first_name, last_name)
	print("As a welcome package the Bank has offered you a sum of N1000")
	print("Your account number is", acc_num)
	print("Your Account Balance is N",acc_balance)
	print("-" * 38)
	print("What would you like to do first: ")
	transaction_menu()

# login function contains code for  account holders login 
# Time spent: 5hrs    
def login():
    # note that 0 is added to every point user is asked for input to allow for easy cancelling and exiting
    print("-" * 38)
    trial = 0
    # sets acc_num global in order to access the variable at other parts of the code
    global acc_num
    # asks user to input their account number
    acc_num = input("Enter your acount number to login or enter 0 to return to main menu: ")
    # cancels
    if acc_num == "0":
        main()
    else:
        # asks user for their pin
        pin = input("Input your pin or enter 0 to return to main menu: ")
        if pin == "0":
            main()
        else:
            # while loop giving 3 chances
            while trial <= 2:
                # opens the shelf 'user data' containing the details of users
                with shelve.open('user_data')as acc_holders:
                    # checks if inputed acc_num and pin are correct
                    if acc_num not in acc_holders and pin not in acc_holders:
                        # prints invalid if incorrect and asks for input again
                        print("Invalid Login Details")
                        acc_num = input("Enter your acount number to login 0 to go back main menu: ")
                        if acc_num == "0":
                            main()
                        else:
                            pin = input("Input your pin of 0 to go back to main menu: ")
                            if pin == "0":
                                main()
                                trial += 1
                    # if inputed acc_num is correct 
                    elif acc_num in acc_holders:
                        user_data = acc_holders[acc_num]
                        # checks if inputed pin is correct for the inputed acc_num
                        if pin == user_data["Pin"]:
                            # if inputed acc_num and pin is correct prints a welcome message and procceeds to the transactions menu
                            print("-" * 38)
                            print("Welcome,", user_data["First Name"], user_data["Last Name"])
                            print("What would you like to do today:")
                            print("Account Balance: N",user_data["Balance"])
                            print("-" * 38)
                            transaction_menu()
                            break
                        else:
                            # if inputed pin is incorrect for the inputed acc_num prints invalid and asks user for input again
                            print("Invalid Login Details")
                            acc_num = input("Enter your acount number to login 0 to go back main menu: ")
                            if acc_num == "0":
                                main()
                            else:
                                pin = input("Input your pin of 0 to go back to main menu: ")
                            if pin == "0":
                                main()
                                trial += 1

# main function containing main menu
def main():
    # while true loop to ensure the code keeps running
    # and to ensure that if user enters invalid input the main menu keeps printing until a valid input is entered
    while True:
        print("-" * 38)
        print("Main Menu:")
        print("\t1 - Create an Account with us")
        print("\t2 - Existing User")
        print("\t3 - Customer Services")
        print("\t4 - About Us")
        print("-" * 38)

        response = input("Pick an option: ")

        if response == "1":
            # calls the create account function
            create_account()
        elif response == "2":
            # calls login function
            login()
        elif response == "3":
            # calls customer service function
            customer_services()
        elif response == "4":
            print("-" * 38)
            # prints a short description of the bank
            print("\tABC Bank of Nigeria, the premier and leading financial institution in the country,\n" 
                "\tstands as the first and best bank, setting the standard for excellence in the Nigerian banking industry.\n" 
                "\tWith a rich history of financial innovation and unwavering commitment to customer satisfaction,\n" 
                "\tABC Bank invites you to experience unparalleled banking services.\n" 
                "\tJoin us and elevate your financial journey with the trusted partner, ABC Bank of Nigeria.")
            print("-" * 38)
            # returns to main menu
            while True:
                go_back = input("Enter 0 to return to main menu: ")
                if go_back == "0":
                  	main()

# driver code to start atm 
if __name__ == "__main__":
    # welcome message
    print('\n')
    print("-" * 38)
    # prints in bold
    print("\033[1mWelcome to the ABC Bank of Nigeria\033[0m")
    # prints in italics
    print("\x1B[3mThe First Bank of Nigeria and the Best\x1B[0m")
    print("How can we help you today: ")
    print("-" * 38)
    # calls main function containing the main menu
    main()

# Finished: 1:35am, 7/11/23