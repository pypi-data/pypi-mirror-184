#!/usr/bin/env python3
import hashlib
import json

# HashedDB!
# By Pigeon Nation!

'''
Secure Password Databases!
For more docs, see the PyPi page!

-- -- -- -- -- -- -- -- +++ == --- - ---- 

Examples, Walkthrough and Usage

-- -- -- -- -- -- -- -- +++ == --- - ---- 

Basic Usage:
=======================================

# Import Module
import HashedDB

# Create Database
db = HashedDB.HashedDB()

# Add Users
db.add_user('bobsmith', 'password1234')
db.add_user('shellythames', 'neonchickenABCD1234')

# Simple CLI - Ask for username and password
print('Login: ')
un = input('Username > ')
pw = input('Password > ')

# Check Details Against Database
result = db.check_user(un, pw)

# Report Results
if result:
	print('Login Succesful!')
else:
	print('Login Failed!')

File Saving:
=======================================

Directory:
Example 2
 ├ add_people.py
 ├ login.py
 ⎩ database.json

ADD_PEOPLE.PY

# Import Module
import HashedDB

# Create New Database
db = HashedDB.HashedDB()

# Add Users
db.add_user('bobsmith', 'password1234')
db.add_user('shellythames', 'neonchickenABCD1234')

# Save To A JSON File
db.to_json('database.json')

LOGIN.PY

# Import Modules
import HashedDB

# Create Database
db = HashedDB.HashedDB()

# Fill Database With Usernames From JSON File
db.from_json('database.json')

# Simple CLI - Ask for username and password
print('Login: ')
un = input('Username > ')
pw = input('Password > ')

# Check Details Against Database
result = db.check_user(un, pw)

# Report Results
if result:
	print('Login Succesful!')
else:
	print('Login Failed!')

'''

version = '0.0.3'
author = 'Pigeon Nation'


class HashedDB():
	'''A Simple Secure Password Database!'''
	def __init__(self, alg=hashlib.sha256):
		'''
		Initiates the Database.
		
		ARGs and KWARGs:
		(* = arg and ** = kwarg)
		
		**alg - The algorithm used to hash the passwords in the database.
		'''
		self.db = {}
		self.alg = alg
	
	def to_json(self, filepath):
		'''Save data to a json file.'''
		assert (type(filepath) == str), 'Invalid Type For Filepath - Only Strings Accepted.'
		json.dump(self.db, filepath)
	
	def from_json(self, filepath):
		'''Load data from a json file - WARNING! All usernames stored in the database will be lost and replaced with new ones.
		To load data from a json file WITHOUT loosing data use HashedDB.append_json(...) instead.'''
		assert (type(filepath) == str), 'Invalid Type For Filepath - Only Strings Accepted.'
		self.db = json.load(filepath)
	
	def filesave_format(self, filepath, format_):
		'''
		Saves data using the specified format. Eg:
		# Using json format
		>>> import json
		>>> db.filesave_format('mydb.json', json)
		
		<module_or_class>.dump(...) is called, with the file name and data being passed to that.
		A module or class must be passed with the method ".dump". Do not pass strings containing the name of a file format to format_! An error will be raised.
		'''
		format_.dump(filepath, self.db)
	
	def fileload_format(self, filepath, format_):
		'''
		Loads data using the specified format. Eg:
		# Using json format
		>>> import json
		>>> db.fileload_format('mydb.json', json)
		
		<module_or_class>.load(...) is called, with the file name being passed to that. Method must return a dictionary.
		A module or class must be passed with the method ".load". Do not pass strings containing the name of a file format to format_! An error will be raised.
		Warning! All data contained in the database before the load will be lost. To only append data, use fileapnd_format(...)!
		'''
		data = format_.load(filepath)
		self.db = data
	
	def fileapnd_format(self, filepath, format):
		'''
		Appends data using the specified format. Eg:
		# Using json format
		>>> import json
		>>> db.fileapnd_format('mydb.json', json)
		
		<module_or_class>.load(...) is called, with the file name being passed to that. Method must return a dictionary.
		A module or class must be passed with the method ".load". Do not pass strings containing the name of a file format to format_! An error will be raised.
		Warning! All data with the same name will be overwritten!
		'''
		
		data = format_.load(filepath)
		for i in data:
			self.db[i] = data[i]
	
	def append_json(self, filepath):
		'''Load data from a json file without losing data already stored. Duplicate entries will be overwritten.'''
		assert (type(filepath) == str), 'Invalid Type For Filepath - Only Strings Accepted.'
		jdb = json.load(filepath)
		for i in jdb:
			self.db[i] = jdb[i]
	
	def check_user(self, eun, epw):
		'''Determines if login details are valid or not. Returns True or False.'''
		assert (type(eun) == str), 'Invalid Type For EUN - Only Strings Accepted.'
		assert (type(epw) == str), 'Invalid Type For EPW - Only Strings Accepted.'
		return True if eun in self.db and self.db[eun] == self.compute(epw.encode()) else False
	
	def import_dict(self, dict_):
		'''Imports a dictionary to the database. WARNING! All usernames stored in the database will be lost and replaced with new ones.
		To load data from a dictionary file WITHOUT loosing data use HashedDB.add_by_dict(...) instead.'''
		assert (type(dict_) == dict), 'Invalid Type For Dict - Only Dictionaries Accepted.'
		self.db = dict_
	
	def add_by_dict(self, dict_):
		'''Imports data from a dictionary into the database without deleting all the other data. Duplicates will be overwritten.'''
		assert (type(dict_) == dict), 'Invalid Type For Dict - Only Dictionaries Accepted.'
		for i in dict_:
			try:
				self.add_user(i, dict_[i])
			except TypeError:
				raise IndexError('Invalid Username Type "' + str(type(i)) + '" - Expecting Strings Only.')
	
	def rem_by_list(self, list_, shout_errors=True):
		'''Mass-removes data from the database. Invalid usernames will raise an error unless shout_errors is False.'''
		assert (type(list_) == list), 'Invalid Type For List - Only Lists Accepted.'
		for i in list_:
			try:
				self.rem_user(i)
			except IndexError:
				if shout_errors:
					raise IndexError('Invalid Username "' + str(i) + '"')
			except TypeError:
				raise IndexError('Invalid Type "' + str(type(i)) + '" - Expecting Strings Only.')
	
	def compute(self, inp):
		'''Converts a password into a hash.'''
		assert (type(un) == bytes), 'Invalid Type For Input - Only Bytes Accepted.'
		return self.alg(inp).hexdigest()
	
	def add_user(self, un, pw):
		'''Adds a user to the database.'''
		assert (type(un) == str), 'Invalid Type For Username - Only Strings Accepted.'
		assert (type(pw) == str), 'Invalid Type For Password - Only Strings Accepted.'
		self.db[un] = self.compute(pw.encode())
	
	def rem_user(self, un):
		'''Removes a user from the database.'''
		assert (type(un) == str), 'Invalid Type For Username - Only Strings Accepted.'
		del self.db[un]
	
	def get_dict(self):
		'''Returns a dictionary object containing all the usernames and passwords in the database.'''
		return self.db
	