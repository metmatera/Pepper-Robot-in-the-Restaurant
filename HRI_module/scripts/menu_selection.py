import sys
import time
import os
import random

try:
	sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
	print "Please set MODIM_HOME environment variable to MODIM folder."
	sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *

def i1():
	water_count = 0
	coke_count = 0
	tables = {'T1':0, 'T2':0, 'T3':0, 'T4':0, 'T5':0}

	orders = {'T1':[], 'T2':[], 'T3':[], 'T4':[], 'T5':[]} #We assign to each table a list containing the order informations: inside the list, a tuple is assigned
															#carrying the type of choice and its quantity e.g (Water, 4)
	# welcome page with start button
	im.ask('welcome_menu')
	
	"""

	1. Ask for what do they want to drink. Let's put 2 type of drinks: a coke and a bottle of water
	2. Let them choose the quantity of the selected drink
	3. Ask again if they want to drink something else 
	4. Let them choose the quantity of the selected drink


	1. Ask for what do they want to eat. Let's put 2 type of dishes: a burger and a salad
	2. Let them choose the quantity of the selected dish
	3. Ask again if they want to eat something else 
	4. Let them choose the quantity of the selected dish

	"""
	OrderConfirmation = 'Cancel'
	
	while OrderConfirmation == 'Cancel':
		confirmation_filename = 'confirmations/'
		W_quantity = ''
		C_quantity = ''
		ToMenu = False
		while not ToMenu:
			selected_drink = im.ask('menu/drinks')   #selected_drink  = Water or Coke
			if selected_drink == 'ToMenu':
				break

			if selected_drink == 'Water':
				W_quantity = im.ask('quantity_drinks')
				#orders[selected_table].append((selected_drink, int(W_quantity)))

			if selected_drink == 'Coke':
				C_quantity = im.ask('quantity_drinks')
				#orders[selected_table].append((selected_drink, int(C_quantity)))
		
		if W_quantity == '':
			confirmation_filename += 'W0'
		else:
			confirmation_filename += 'W' + W_quantity

		if C_quantity == '':
			confirmation_filename += 'C0'
		else:
			confirmation_filename += 'C' + C_quantity
		
		


		H_quantity = ''
		F_quantity = ''
		ToConfirmation = False
		while not ToConfirmation:
			selected_dish = im.ask('menu/dishes')   #selected_dish  = Burger or Chips
			if selected_dish == 'ToConfirmation':
				break

			if selected_dish == 'Burger':
				H_quantity = im.ask('quantity_dishes')
				#orders[selected_table].append( (selected_dish, int(H_quantity)))

			if selected_dish == 'Chips':
				F_quantity = im.ask('quantity_dishes')
				#orders[selected_table].append( (selected_dish, int(F_quantity)))

		if H_quantity == '':
			confirmation_filename += 'H0'
		else:
			confirmation_filename += 'H' + H_quantity
			
		if F_quantity == '':
			confirmation_filename += 'F0'
		else:
			confirmation_filename += 'F' + F_quantity



		OrderConfirmation = im.ask(confirmation_filename)
		if OrderConfirmation == 'Confirm':
			im.execute('confirmation_menu')
		else:
			im.execute('restart')


if __name__ == "__main__":

	mws = ModimWSClient()

	# local execution
	mws.setDemoPathAuto(__file__)
	# remote execution
	# mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')
	
	mws.run_interaction(i1)

