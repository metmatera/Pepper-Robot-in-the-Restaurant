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

	
	while (0 in tables.values()):
		
		im.ask('welcome')
		
		# get free tables
		free_tables = [t for t in tables if tables[t] == 0]
		free_tables.sort()
		filename_free_tables = 'tables/'
		for t in free_tables:
			filename_free_tables += t 	#filename -> T1T2T3T4T5

		# table selection (from T1 to T5)
		selected_table = im.ask(filename_free_tables)
		
		# number of people selection (from 1 to 5)
		n_people = int(im.ask('people'))

		# update tables
		tables[selected_table] = n_people	

		im.execute('confirmation')
		
	# when all the tables are occupied
	im.execute('occupied')
	

if __name__ == "__main__":

	mws = ModimWSClient()

	# local execution
	mws.setDemoPathAuto(__file__)
	# remote execution
	# mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')
	
	mws.run_interaction(i1)

