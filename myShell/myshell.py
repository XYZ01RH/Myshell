#!/usr/bin/env python

import os
import sys
import subprocess

class Shell:
	def __init__(self):
		self.currentDir = str(os.getcwd())
		self.envVar = {"shell" : self.currentDir, "PWD" : str(os.getcwd())}
		os.environ.clear()
		os.environ.update(self.envVar)

	#Changes the current directory and updates
	#the PWD environment variable
	def cd(self,newDir = ""):
		#If empty then return the current dir
		if(len(newDir) == 0):
			print os.getenv("PWD")
			return
		try:
			os.chdir(newDir)
			os.environ["PWD"] = newDir
			self.currentDir=os.getenv("PWD")
		except:
			print "The directory path " + newDir + " is invalid or does not exist. Please give the full directory path"

	#Clears the screen
	def clr(self):
		print("\033c")
		print("Welcome....to my shell...make yourself at home. Enter a command to begin: \n")
	
	#List contents of specified directory
	def dir(self,path):
		try:
			for content in os.listdir(path):
				print content
		except dirError:
			print "The directory " + path + " is invalid or does not exist"

	#Print all of the current environment variables
	def environ(self):
		environ = os.environ
		for each in environ:
			print(each + " : " + environ[each])
		
	#Print user input to the console
	def echo(self,userIn):
		print userIn + "\n"

	#Display a user help menu
	def help(self):
		print "Custom Shell Manual"
		print "-----------------"
		print "Usage:"
		print "./myshell.py [File containing commands]"
		print "-----------------"
		print "Commands:"
		print "dir [directory] - list directory contents"
		print "clr - clear the current shell screen"
		print "environ - output the current environment variables"
		print "cd [target directory] - change current working directory"
		print "pause - pause execution in the shell until the user hits 'enter'"
		print "quit - quits the shell"
		print "echo [String] - prints the specified string to the shell"
		print "Other:"
		print "All other commands entered into this shell will be treated as"
		print "executeable files/commands"
		print "-----------------"
		print ""

	#Pauses the shell
	def pause(self):
		try:
			raw_input("Paused..Press Enter to continue")
		except:
			pass

	#Exits the shell
	def quit(self):
		sys.exit()


	#Creates a new subprocess with specified environemnt variables
	def childProcess(self,programInput):
		try:
			parentDict = {"parent" : (os.getcwd() + "/myshell"), "PWD" : self.currentDir}
			subprocess.call(programInput, env=parentDict)
			return True
		except:
			print "Process creation error"

	#Reads a file full of commands
	def readFile(self,fileIn):
		with open (fileIn, 'r') as commandFile:
			try:
				for line in commandFile:
					print line.rstrip()
					self.commandCheck((line.rstrip()).split())
			except NameError as e:
				print "File input error"
		

	#Checks user input for commands
	def commandCheck(self,commandIn):
		if(commandIn[0] == "cd"):
			if(len(commandIn) > 1):
				self.cd(commandIn[1])
			else:
				self.cd()
		elif(commandIn[0] == "clr"):
			self.clr()
		elif(commandIn[0] == "dir"):
			if(len(commandIn) > 1):
				self.dir(commandIn[1])
			else:
				self.dir(".")
		elif(commandIn[0] == "environ"):
			self.environ()
		elif(commandIn[0] == "echo"):
			self.echo(" ".join(commandIn[1:]))
		elif(commandIn[0] == "help"):
			self.help()
		elif(commandIn[0] == "pause"):
			self.pause()
		elif(commandIn[0] == "quit"):
			self.quit()
		else:
			self.childProcess(commandIn[0])
		
		
#Main running function
def runner(argv):
	_environ = dict(os.environ)
	newShell = Shell()
	if(len(argv) > 1):
		filename = argv[1]
		newShell.readFile(filename)
		print("Exiting Shell. Goodbye")
	else:
		print("Welcome....to my shell...make yourself at home. Enter a command to begin: \n")
		while(True):
			entry  = raw_input(newShell.currentDir + ":> ")
			if( len(entry) != 0 ):
				newShell.commandCheck(entry.split())
			else:
				print ""
	os.environ.update(_environ)


runner(sys.argv)
		
				
	

	
