import web
from collections import namedtuple
import csv
import os.path
from copy import deepcopy

urls = (
	'/(.*)', 'pb'
)
app = web.application(urls, globals())

class pb:

	def GET(self, name):
		debug = 0		
		pb_file = 'pb.csv'		
		user_input = web.input(arg1='',arg2='',arg3='',arg4='',arg5='')	
		s = ''
		arg1 = str(user_input.arg1)
		arg2 = str(user_input.arg2)
		arg3 = str(user_input.arg3)
		arg4 = str(user_input.arg4)
		arg5 = str(user_input.arg5)

		phonebook = []
		log = ''
		if os.path.exists(pb_file):
			with open(pb_file, 'rb') as csvfile:
				reader = csv.reader(csvfile, delimiter=',')
				log += 'Reading phonebook\n'				
				for row in reader:
					log += str(row[:])+'\n'									
					phonebook.append(row)
			os.remove(pb_file)
		function = ''	
		if arg1 == 'add':
			function = 'add'
			if arg2 == '':
				s = 'need surname '
			if arg3 == '':
				s += 'need name '
			if arg4 == '':
				s += 'need number' 
			if s == '':				
				
				for row in phonebook:					
					surname = row[0]
					name = row[1]
					if surname == arg2 and name == arg3:
						s = arg2 + ', ' + arg3 + ' already exists in phonebook'
				tup = (arg2,arg3,arg4,arg5)
				if s == '':				
					phonebook.append(tup)
					s = 'added entry to phonebook: ' + str(tup) + '\n'
		elif arg1 == 'list':
			function = 'list'
			for row in phonebook:
				s += 'Name: ' + row[0] + ', ' + row[1] + '\tNumber: ' + row[2] + '\tAddress: ' + row[3] + '\n'
		elif arg1 == 'find':
			function = 'find'
			for row in phonebook:
				surname = row[0]
				log += 'surname: ' + surname + '\n'
				if surname == arg2:
					s += 'Name: ' + row[0] + ', ' + row[1] + '\tNumber: ' + row[2] + '\tAddress: ' + row[3] + '\n'			
			if s == '':
				s = 'Could not find any entries for ' + arg2 	
		elif arg1 == 'update':
			for row in phonebook:
				surname = row[0]
				name = row[1]
				if surname == arg2 and name == arg3:
					phonebook.remove(row)
					phonebook.append([arg2,arg3,arg4,arg5])
					s = 'updated ' + surname + ', ' + name
			if s = '':
				s = arg2 + ', ' + arg3 + ' does not exist in phonebook'
		elif arg1 == 'delete':
			function = 'delete'			
			for row in phonebook:
				surname = row[0]
				name = row[1]
				if surname == arg2 and name == arg3:
					phonebook.remove(row)
					s = surname + ', ' + name + ' has been removed from the phonebook'					
					break
			if s == '':
				s = arg2 + ', ' + arg3 + ' does not exist in phonebook'				
		else:		
			s = 'list of cmds:\narg1=list&arg2=name&arg3=surname&arg4=number&arg5=[address] \narg1=list\narg1=delete&arg2=surname&arg3=firstname\narg1=find&arg2=surname\narg1=update&arg2=name&arg3=surname&arg4=number&arg5=address\narg1=help'		
		with open (pb_file, 'wb') as csvfile:
			log += 'Rewritting phonebook\n'
			writer = csv.writer(csvfile, delimiter=',')		
			for row in phonebook:	
				log += str(row) + '\n'
				writer.writerow(row)				



		log += 'actual results\n-------------------\n'		
		if debug:
			return 'function: ' + function + '\n' + 'log: ' + log + '\n' + s
		else:
			return s

	#def POST(self):
	#	i = web.input()	
	#	return 'hello world'
	#	raise web.seeother('/')


if __name__ == "__main__":	
	app.run()

