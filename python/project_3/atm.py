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
# the time module has been include in order to cuase intentional delay in some parts of the code
# in order to improve user experience
import time

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
            print("-" * 38)
            print("Loading...")
            time.sleep(1)
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
			print("...")
			time.sleep(1)
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data') as acc_holder:
				user_data = acc_holder[acc_num]
				trial_pin = 3
				while trial_pin >= 0:
					if pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						account_settings()
					elif pin == user_data["Pin"]:
						break
					else:
						print("...")
						time.sleep(1)
						print("Invalid pin. You have", trial_pin, "trials")
						pin = input("Enter a valid pin to proceed or 0 to cancel :")
						trial_pin -= 1
					if trial_pin == 0:
						print("-" * 38)
						print("You have entered your pin unsuccessfully 3 times. You will be redirected now")
						time.sleep(3)
						account_settings()
						break
				print("-" * 38)
				print("Loading...")
				time.sleep(3)
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
						print("...")
						time.sleep(1)
						account_settings()
						break
		# asks user to confirm their pin and if the pin is correct it proceeds to changing the user pin
		elif choice == "2":
			new_pin = ''
			print("...")
			time.sleep(1)
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data', writeback=True) as acc_holder:
				user_data = acc_holder[acc_num]
				trial_pin = 3
				while trial_pin >= 0:
					if pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						account_settings()
					elif pin == user_data["Pin"]:
						break
					else:
						print("...")
						time.sleep(1)
						print("Invalid pin. You have", trial_pin, "trials")
						pin = input("Enter a valid pin to proceed or 0 to cancel :")
						trial_pin -= 1
					if trial_pin == 0:
						print("-" * 38)
						print("You have entered your pin unsuccessfully 3 times. You will be redirected now")
						time.sleep(3)
						account_settings()
						break
				print("-" * 38)

				def Pin():
					nonlocal new_pin
					new_pin =  input("Input a new 5 digit pin or 0 to cancel: ")
					if new_pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						account_settings()
					elif pin.isdigit():
						if len(pin) == 5:
							exit
						else:
							print("...")
							time.sleep(1)
							print("Invalid input")
							Pin()
					else:
						print("...")
						time.sleep(1)
						print("Invalid input")
						Pin()

				Pin()
				print("-" * 38)
				print("Loading...")
				time.sleep(3)
				user_data["Pin"] = new_pin
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Pin changed succesfully")
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return: ")
					if go_back == "0":
						print("...")
						time.sleep(1)
						account_settings()
						break
		# asks user to confirm their pin and if correct proceeds to changing the user phone number
		elif choice == "3":
			phone_num = ''
			print("...")
			time.sleep(1)
			print("-" * 38)
			pin = input("Enter your pin to continue or 0 to return: ")
			with shelve.open('user_data', writeback=True) as acc_holder:
				user_data = acc_holder[acc_num]
				trial_pin = 3
				while trial_pin >= 0:
					if pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						account_settings()
					elif pin == user_data["Pin"]:
						break
					else:
						print("...")
						time.sleep(1)
						print("Invalid pin. You have", trial_pin, "trials")
						pin = input("Enter a valid pin to proceed or 0 to cancel :")
						trial_pin -= 1
					if trial_pin == 0:
						print("-" * 38)
						print("You have entered your pin unsuccessfully 3 times. You will be redirected now")
						time.sleep(3)
						account_settings()
						break
				print("-" * 38)
				
				def phone_number():
					nonlocal phone_num
					phone_num =  input("Input your new Phone Number: ")
					if phone_num == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						main()
					elif phone_num.isdigit():
						if len(phone_num) == 11:
							print("...")
							time.sleep(1)
							exit
						else:
							print("...")
							time.sleep(1)
							print("Invalid phone number")
							phone_number()
					else:
						print("...")
						time.sleep(1)
						print("Invalid phone number")
						phone_number()

				phone_number()
				print("-" * 38)
				print("Loading...")
				time.sleep(3)
				user_data["Phone number"] = phone_num
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Phone nmuber changed successfully")
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return: ")
					if go_back == "0":
						print("...")
						time.sleep(1)
						account_settings()
						break
		# customer service menu
		elif choice == "4":
			print("...")
			time.sleep(1)
			print("-" * 38)
			print("\tContact us trough the following numbers if you have any issues: 09052423929, 08080017464")
			print("\tOr Email us at ABCnaija@gmail.ng or at ogunsanyalouis@gmail.com")
			print("-" * 38)
			time.sleep(2)
			while True:
				go_back = input("Enter 0 to return: ")
				if go_back == "0":
					print("...")
					time.sleep(1)
					account_settings()
					break
		# exits the account settings menu
		elif choice == "5":
			print("-" * 38)
			print("Exiting...")
			time.sleep(3)
			transaction_menu()

# balance_menu function containing code to print the user account balance
# Time spent: 5 mins
def balance_menu():
	print("-" * 38)
	with shelve.open('user_data') as acc_holder:
		user_data = acc_holder[acc_num]
		pin = input("Enter your pin to proceed :")
		trial_pin = 3
		while trial_pin >= 0:
			if pin == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				transaction_menu()
			elif pin == user_data["Pin"]:
				break
			else:
				print("...")
				time.sleep(1)
				print("Invalid pin. You have", trial_pin, "trials")
				pin = input("Enter a valid pin to proceed or 0 to cancel :")
				trial_pin -= 1
			if trial_pin == 0:
				print("-" * 38)
				print("You have entered your pin unsuccessfully 3 times. You will be redirected now")
				time.sleep(3)
				transaction_menu()
				break
		print("-" * 38)
		print("Loading...")
		time.sleep(3)
		print("-" * 38)
		print("Your Account Balance is: N",user_data["Balance"])
		print("-" * 38)
		while True:
			go_back = input("Enter 0 to return: ")
			if go_back == "0":
				print("-" * 38)
				print("Loading...")
				time.sleep(1)
				transaction_menu()
				break

# transfer_menu function contains code for transferring amount to other account holders
# since the code cannot interact with other codes it is assumed that users can only transfer
# between users with accounts at the bank
# Time spent: 10hrs
def transfer_menu():
	print("-" * 38)

	def transfer():
		# this function checks if the amount entered is less than the user balance
		# if the amount is less it asks the user to confirm their pin to transfer the amount
		nonlocal amount, reciever_account
		with shelve.open('user_data', writeback=True)as acc_holders:
			user_data = acc_holders[acc_num]
			if int(amount) > user_data["Balance"] :
				print("-" * 38)
				print("The amount you have entered is more than your balance")
				print("Your account balance is N",user_data["Balance"])
				print("-" * 38)
				amount = input("Please enter another amount or 0 to cancel: ")
				trial_accbal = True
				while trial_accbal:
					if amount == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						transaction_menu()
					if amount.isdigit():
						if int(amount) > 100:
							transfer()
							break
						else:
							print("...")
							time.sleep(1)
							amount = input("The amount must be greater than N100. Enter a valid amount or 0 to cancel :")
							trial_accbal = True
					else:
						print("...")
						time.sleep(1)
						amount = input("Enter a valid amount to proceed or 0 to cancel :")
						trial_accbal = True
			elif int(amount) <= user_data["Balance"]:
				print("-" * 38)
				print("You are about to transfer N",amount, "to", reciever_data["First Name"], reciever_data["Last Name"])
				pin = input("Enter your pin to proceed or 0 to cancel: ")
				trial_pin = 3
				while trial_pin >= 0:
					if pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						transaction_menu()
					elif pin == user_data["Pin"]:
						break
					else:
						print("...")
						time.sleep(1)
						print("Invalid pin. You have", trial_pin, "trials")
						pin = input("Enter a valid pin to proceed or 0 to cancel :")
						trial_pin -= 1
					if trial_pin == 0:
						print("-" * 38)
						print("You have entered your pin unsuccessfully 4 times. You will be redirected now")
						time.sleep(3)
						transaction_menu()
						break
				# deposits the amount into the recipient account
				balance = reciever_data["Balance"] + int(amount)
				reciever_data["Balance"] = balance
				reciever[reciever_account] = reciever_data
				# deducts the amount from the user account balance
				user_bal = user_data["Balance"] - int(amount)
				user_data["Balance"] = user_bal
				acc_holders[acc_num] = user_data
				print("-" * 38)
				print("Loading...")
				time.sleep(3)
				# prints a success message to indicate that the transfer has been made
				print("-" * 38)
				print("Transfer Successful")
				print("Your account balance is N",user_data["Balance"])
				while True:
					print("-" * 38)
					go_back = input("Enter 1 to transfer again or 0 to return: ")
					if go_back == "0":
						print("-" * 38)
						print("Loading...")
						time.sleep(1)
						transaction_menu()
					elif go_back == "1":
						print("...")
						time.sleep(1)
						transfer_menu()

	# asks user for the account number they want to transfer to
	print("You can only transfer to other account holdres at the bank")
	reciever_account = input("Enter the account number that you want to transfer to or 0 to cancel: ")
	# opens the shelve to check if inputed account number is an account holder
	with shelve.open('user_data', writeback=True)as reciever:
		trial_acc = True
		while trial_acc:
			if reciever_account == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				transaction_menu()
				break
			if reciever_account in reciever:
				break
			else:
				print("...")
				time.sleep(1)
				print("Invalid account number")
				reciever_account = input("Enter a valid account number or 0 to cancel: ")
				trial_acc = True
		# prints the name of the user with the inputed account number and
		# asks user for amount to transfer 
		reciever_data = reciever[reciever_account]
		print("-" * 38)
		print("Checking...")
		time.sleep(2)
		print("-" * 38)
		print(reciever_data["First Name"], reciever_data["Last Name"])
		print("-" * 38)
		amount = input("Enter the amount you want to transfer or 0 to cancel. The least transfer amount is N100: ")
		trial_amount = True
		while trial_amount:
			if amount == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				transaction_menu()
			if amount.isdigit():
				if int(amount) > 100:
					transfer()
					break
				else:
					print("...")
					time.sleep(1)
					amount = input("The amount must be greater than N100. Enter a valid amount or 0 to cancel :")
					trial_amount = True
			else:
				print("...")
				time.sleep(1)
				amount = input("Enter a valid amount to proceed or 0 to cancel :")
				trial_amount = True

# withdrawal_menu function containing code for withdrawing from user account
# Time spent: 12hrs
def withdrawal_menu():
	print("-" * 38)
	# this function checks if the amount entered by user is a digit
	def is_digit():
		nonlocal deduct
		amount = input("Enter an amount to withdraw or 0 to cancel: ")
		if amount == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			withdrawal_menu()
		elif amount.isdigit():
			if int(amount) in range(1000, 30001):
				deduct = int(amount)
				print("...")
				time.sleep(1)
				withdraw_amount()
			else:
				print("...")
				time.sleep(1)
				print("The amount must be in the range of N1,000 and N30,000")
				is_digit()
		else:
			print("...")
			time.sleep(1)
			print("Enter a valid amount to proceed")
			is_digit()

	# this function takes the amount inputed by user, checks if the input is lesser than the user account balance and
	# carries out the transaction of withdrawing the amount from the user's account balance after confirming their pin
	def withdraw_amount():
		amount = deduct
		with shelve.open('user_data', writeback=True)as acc_holder:
			user_data = acc_holder[acc_num]
			if amount > user_data["Balance"]:
				print("-" * 38)
				print("The amount you have entered is greater than your account balance")
				print("Your account balance is: N", user_data["Balance"])
				is_digit()
			else:
				print("-" * 38)
				print("Your are about to withdraw the sum of N", amount)
				pin = input("Enter your pin to proceed or 0 to cancel: ")
				trial_pin = 3
				while trial_pin >= 0:
					if pin == "0":
						print("-" * 38)
						print("Cancelling...")
						time.sleep(1)
						withdrawal_menu()
					elif pin == user_data["Pin"]:
						break
					else:
						print("...")
						time.sleep(1)
						print("Invalid pin. You have", trial_pin, "trials")
						pin = input("Enter a valid pin to proceed or 0 to cancel :")
						trial_pin -= 1
					if trial_pin == 0:
						print("-" * 38)
						print("You have entered your pin unsuccessfully 4 times. You will be redirected now")
						time.sleep(3)
						withdrawal_menu()
						break
				balance = user_data["Balance"] - amount
				user_data["Balance"] = balance
				acc_holder[acc_num] = user_data
				print("-" * 38)
				print("Loading...")
				time.sleep(4)
				print("-" * 38)
				print("Withdrawal successful")
				print("Your account balance is N", user_data["Balance"])
				print("-" * 38)
				while True:
					go_back = input("Enter 0 to return to transaction menu or 1 to withdraw again :")
					if go_back == "0":
						print("-" * 38)
						print("Loading...")
						time.sleep(1)
						transaction_menu()
						break
					elif go_back == "1":
						print("...")
						time.sleep(1)
						withdrawal_menu()
						break

	print("Withdrawal menu")
	print("\t1 - N1,000", "\t5 - N20,000")
	print("\t2 - N2,000", "\t6 - N30,000")
	print("\t3 - N5,000", "\t7 - Enter amount")
	print("\t4 - N10,000", "\t8 - Exit")
	print("-" * 38)

	choice = input("Choose an option to withdraw: ")

	options = ["1", "2", "3", "4", "5", "6", "7", "8"]
	# while loop to keep asking user for input if input is not between 1 to 8
	trial_choice = True
	while trial_choice:
		if choice in options:
			break
		else:
			choice = input("Choose an option between 1 and 8 to withdraw: ")
			trial_choice = True
	if choice == "8":
		print("-" * 38)
		print("Exiting...")
		time.sleep(1)
		transaction_menu()
	elif choice == "1":
		deduct = 1000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "2":
		deduct = 2000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "3":
		deduct = 5000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "4":
		deduct = 10000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "5":
		deduct = 20000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "6":
		deduct = 30000
		print("...")
		time.sleep(1)
		withdraw_amount()
	elif choice == "7":
		# if user chooses to enter amount
		print("-" * 38)
		print("The minumum withdrawal amount is N1000 and the maximum is N30,000")
		is_digit()

# deposit_menu function containing code for depositing into user account
# Time spent: 7hrs
def deposit_menu():
	print("-" * 38)
	# asks user to input deposit amount printing an error if input is invalid and cancelling if 0 is entered
	add_to_balance = input("The minimum deposit amount is N1000. Enter an amount to deposit or 0 to return: ")
	trial_add = True
	while trial_add:
		if add_to_balance == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			transaction_menu()
		elif add_to_balance.isdigit():
			if int(add_to_balance) > 999:
				break
			else:
				print("...")
				time.sleep(1)
				add_to_balance = input("Please enter an amount greater than N1000 :")
				trial_add = True
		else:
			print("...")
			time.sleep(1)
			add_to_balance = input("Invalid input. Enter a valid amount :")
			trial_add = True

    # after a valid amount is inputed, the shelve is openend in order to deposit into the user balance
	with shelve.open('user_data', writeback=True)as acc_holders:
		user_data = acc_holders[acc_num]
		balance = user_data["Balance"] + int(add_to_balance)
		user_data["Balance"] = balance
		acc_holders[acc_num] = user_data
		print("-" * 38)
		print("Loading...")
		time.sleep(4)
		print("-" * 38)
		print("Deposit succesful")
		print("Your account balance is: N",user_data["Balance"])
		print("-" * 38)
		go_back = input("Enter 0 to return or 1 to deposit again: ")
		while True:
			if go_back == "0":
				print("-" * 38)
				print("Returning...")
				time.sleep(1)
				transaction_menu()
				break
			if go_back == "1":
				print("...")
				time.sleep(1)
				deposit_menu()
				break
			go_back = input("Enter 0 to return or 1 to deposit again: ")

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
			print("-" * 38)
			print("Loading...")
			time.sleep(1)
			deposit_menu()
		elif choice == "2":
			# calls the withdrawal_menu function
			print("-" * 38)
			print("Loading...")
			time.sleep(1)
			withdrawal_menu()
		elif choice == "3":
			# calls the transfer_menu function
			print("-" * 38)
			print("Loading...")
			time.sleep(1)
			transfer_menu()
		elif choice == "4":
			# calls the balance_menu function
			print("-" * 38)
			print("Loading...")
			time.sleep(1)
			balance_menu()
		elif choice == "5":
			# calls the account setting function
			print("-" * 38)
			print("Loading...")
			time.sleep(1)
			account_settings()
		elif choice == "6":
			# at this point the current user exits and thank you message and then a welcome message is pritnted for the new user with the main menu
			print("-" * 38)
			print("Thank you for Banking with us")
			print("-" * 38)
			print("Exiting...")
			time.sleep(2)
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
	# declaring variables
	first_name = ''
	last_name = ''
	phone_num = ''
	pin = ''
	
	print("-" * 38)
	# makes acc_num accesible at other functions
	global acc_num
	# picks a random quote from the 'qoute' list and prints it in italics
	print("\x1B[3m" + random.choice(quotes) + "\x1B[0m")
	print("-" * 38)
	print("...")
	time.sleep(3)
	# 0 is added as an option at every point asking for input giving user freedom to quit at any point
	print("Welcome! Enter 0 at anytime to cancel")

	# functions are nested in order to ask user for their details and handle error input
	# Frst name function
	def First_name():
		nonlocal first_name
		first_name = input("Input your First Name: ")
		if first_name == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			main()
		elif first_name.isalpha():
			print("...")
			time.sleep(1)
			Last_name()
		else:
			print("...")
			time.sleep(1)
			print("Invalid input")
			First_name()
	# Last name function
	def Last_name():
		nonlocal last_name
		last_name = input("Input your Last Name: ")
		if last_name == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			main()
		elif last_name.isalpha():
			print("...")
			time.sleep(1)
			phone_number()
		else:
			print("...")
			time.sleep(1)
			print("Invalid input")
			Last_name()
	# Phone number function
	def phone_number():
		nonlocal phone_num
		phone_num =  input("Input your Phone Number: ")
		if phone_num == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			main()
		elif phone_num.isdigit():
			if len(phone_num) == 11:
				print("...")
				time.sleep(1)
				Birth_date()
			else:
				print("...")
				time.sleep(1)
				print("Invalid phone number")
				phone_number()
		else:
			print("...")
			time.sleep(1)
			print("Invalid phone number")
			phone_number()
	# Date of birth function additional error handling functions are added to ensure correct input of birth date and
	# to check if user is underage
	def Birth_date():
		def dob(day,month,year):
			global date_of_birth
			date_of_birth = day,month,year
		
		print("Enter your Date of birth")
		day = input("Enter the day: ")
		trial_day = True
		while trial_day:
			if day == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				main()
			elif day.isdigit():
				if int(day) in range(1, 32):
					break
				else:
					print("...")
					time.sleep(1)
					day = input("Invalid input. Enter a valid day :")
					trial_day = True
			else:
				print("...")
				time.sleep(1)
				day = input("Invalid input. Enter a valid day :")
				trial_day = True
		print("...")
		time.sleep(1)
		month = input("Enter the month in digits: ")
		trial_month = True
		while trial_month:
			if month == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				main()
			if month.isdigit():
				if int(month) in range(1, 13):
					break
				else:
					print("...")
					time.sleep(1)
					month = input("Invalid input. Enter a valid month :")
					trial_month = True
			else:
				print("...")
				time.sleep(1)
				month = input("The month must be in digits. Enter a valid month :")
				trial_month = True
		print("...")
		time.sleep(1)
		year = input("Enter the year: ")
		trial_year = True
		while trial_year:
			if year == "0":
				print("-" * 38)
				print("Cancelling...")
				time.sleep(1)
				main()
			if year.isdigit():
				if int(year) in range(1935, 2006):
					break
				elif int(year) > 2005:
					print("...")
					time.sleep(1)
					print("Sorry you cannot open an account with us.")
					print("You must have been 18 at the start of the year to be eligible.")
					year = input("Enter 0 to cancel or enter another birth year: ")
					trial_year = True
				else:
					print("...")
					time.sleep(1)
					year = input("Invalid input. Enter a valid year :")
					trial_year = True
			else:
				print("...")
				time.sleep(1)
				year = input("Invalid input. Enter a valid year :")
				trial_year = True
		dob(int(day),int(month),int(year))
		print("...")
		time.sleep(1)
		Pin()
	# Pin function
	def Pin():
		nonlocal pin
		pin =  input("Input a 5 digit pin: ")
		if pin == "0":
			print("-" * 38)
			print("Cancelling...")
			time.sleep(1)
			main()
		elif pin.isdigit():
			if len(pin) == 5:
				exit
			else:
				print("...")
				time.sleep(1)
				print("Invalid input")
				Pin()
		else:
			print("...")
			time.sleep(1)
			print("Invalid input")
			Pin()

	# calls the First name function to begin to ask user for their details
	First_name()

	# creates an account number starting with 100 and ending with the last 7 digits of the phone number
	last7_digit_phonenum = int(phone_num) % 10000000
	acc_num = "100" + str(last7_digit_phonenum)
	# creates variable for storing user account balance and stores N1000
	acc_balance = 1000
	# puts all user details in a list 
	user_data = {
		"First Name": first_name,
		"Last Name": last_name,
		"Balance": acc_balance,
		"Phone number": phone_num,
		"Account number": acc_num,
		"Birth date": date_of_birth,
		"Pin": pin
	}
	# puts the list containing user details on a shelve thereby making it accessible between sessions and easy to access
	with shelve.open('user_data') as acc_holders:
		# saves the item on the shelve with the account number
		acc_holders[acc_num] = user_data
	# prints a welcome message and proceeds to the transaction menu
	print("-" * 38)
	print("Creating acoount...")
	time.sleep(4)
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
    acc_num = input("Enter your acount number to login or enter 0 to cancel: ")
    # cancels
    if acc_num == "0":
        print("-" * 38)
        print("Cancelling...")
        time.sleep(1)
        main()
    else:
        # asks user for their pin
        print("...")
        time.sleep(1)
        pin = input("Input your pin or enter 0 to cancel: ")
        if pin == "0":
            print("-" * 38)
            print("Cancelling...")
            time.sleep(1)
            main()
        else:
            # while loop giving 3 chances
            while trial <= 3:
                print("...")
                time.sleep(1)
                if trial == 3:
                    print("-" * 38)
                    print("You have inputed the wrong account number and pin 4 times, you will now be redirected to the main menu.")
                    print("-" * 38)
                    # waits 4 seconds before printing welcome message and going to main menu
                    time.sleep(4)
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
                # opens the shelf 'user data' containing the details of users
                with shelve.open('user_data')as acc_holders:
                    # checks if inputed acc_num and pin are correct
                    if acc_num not in acc_holders and pin not in acc_holders:
                        # prints invalid if incorrect and asks for input again
                        print("Invalid Login Details")
                        acc_num = input("Enter your acount number to login or 0 to cancel: ")
                        if acc_num == "0":
                            print("-" * 38)
                            print("Cancelling...")
                            time.sleep(1)
                            main()
                        else:
                            print("...")
                            time.sleep(1)
                            pin = input("Input your pin or 0 to cancel: ")
                            trial += 1
                            if pin == "0":
                                print("-" * 38)
                                print("Cancelling...")
                                time.sleep(1)
                                main()
                    # if inputed acc_num is correct 
                    elif acc_num in acc_holders:
                        user_data = acc_holders[acc_num]
                        # checks if inputed pin is correct for the inputed acc_num
                        if pin == user_data["Pin"]:
                            # if inputed acc_num and pin is correct prints a welcome message and procceeds to the transactions menu
                            print("-" * 38)
                            print("Loading...")
                            time.sleep(2)
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
                            acc_num = input("Enter your acount number to login or 0 to cancel: ")
                            if acc_num == "0":
                                print("-" * 38)
                                print("Cancelling...")
                                time.sleep(1)
                                main()
                            else:
                                print("...")
                                time.sleep(1)
                                pin = input("Input your pin or 0 to cancel: ")
                                trial += 1
                            if pin == "0":
                                print("-" * 38)
                                print("Cancelling...")
                                time.sleep(1)
                                main()

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
            print("-" * 38)
            print("Loading...")
            time.sleep(1)
            create_account()
        elif response == "2":
            # calls login function
            print("-" * 38)
            print("Loading...")
            time.sleep(1)
            login()
        elif response == "3":
            # calls customer service function
            print("-" * 38)
            print("Loading...")
            time.sleep(1)
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
            time.sleep(2)
            # returns to main menu
            while True:
                go_back = input("Enter 0 to return to main menu: ")
                if go_back == "0":
                    print("-" * 38)
                    print("Returning...")
                    time.sleep(1)
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