import os

class get_browsers:
	'''
	********* THIS SCRIPT RETURNS A LIST CONTAINING BROWSERS INSTALLED ON USER'S LINUX SYSTEM *********
	CLASS get_browsers DOCINFO:
	get_browsers HAVE TWO FUNCTIONS I.E.,
	1) __init__
	2) work()

		__init__ DOCFILE:
			__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.

		WORK() DOCFILE:
			THE FUNCTION WORKS IN FOLLOWING WAY:
			1) COLLECTING DATA FROM COMMANDLINE, AND SAVING IT INTO A STRING.
			2) SPLITTING DATA ACCORDING TO A NEW LINE AND SAVING ALL LINES 'BROWSER' NAMED LIST.
			3) REMOVING LAST REDUNDANT ELEMENT.
			4) REFINING NAME FROM THE LIST WE GET.
			5) RETURNING THE LIST.
	'''

	def __init__(self):
		'''
__init__ DOCFILE:
__init__ BLOCK SERVES THE INITIALIZATION FUNCTION, CONTAINING INITIALIZED VARIABLES WHICH IS GOING TO BE USED LATER BY OTHER MEMBER FUNCTION.
		'''
		self.command_output = ""																	# TO SAVE DATA RECIEVED FROM COMMAND INTO A STRING
		self.browsers = []																			# FOR SAVING BROWSER DATA COLLECTED INTO A SINGLE VARIABLE


	def work(self):
		'''
WORK() DOCFILE:
	THE FUNCTION WORKS IN FOLLOWING WAY:
	1) COLLECTING DATA FROM COMMANDLINE, AND SAVING IT INTO A STRING.
	2) SPLITTING DATA ACCORDING TO A NEW LINE AND SAVING ALL LINES 'BROWSER' NAMED LIST.
	3) REMOVING LAST REDUNDANT ELEMENT.
	4) REFINING NAME FROM THE LIST WE GET.
	5) RETURNING THE LIST.
		'''
		self.command_output = os.popen("apropos 'web browser'").read()									# COLLECTING DATA FROM COMMANDLINE, AND SAVING IT INTO A STRING.
		self.browsers = self.command_output.split('\n')														# SPLITTING DATA ACCORDING TO A NEW LINE AND SAVING ALL LINES 'BROWSER' NAMED LIST
		self.browsers.pop()																				# REMOVING LAST REDUNDANT ELEMENT
		self.browsers = [i[:i.find('(')-1] for i in self.browsers]											# REFINING NAME FROM THE LIST WE GET
		return self.browsers																				# RETURNING THE LIST