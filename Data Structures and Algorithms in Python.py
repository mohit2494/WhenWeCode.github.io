# DATA STRUCTURES AND ALGORITHMS IN PYTHON

# 1. INTRODUCTION AND EFFICIENCY
#===============================

# This is a one-line comment in Python. - Code blocks are so useful
""" This type of comment is used to document the purpose of functions and classes """

# Declaration/Initialization
#===========================
# Values, not variables have data types 
# A variable can be reassigned to contain a different data type
answer = 42 			# simple variable declaration
answer = "The answer is 42"	# simple string declaration in python

# Data types in python
#=====================

boolean = True 		#boolean
number	= 1.1 		#float
string  = "Strings can be declared with single or double quotes"  	# string
pylist	= ["Lists can have",1,2,3,4,"or more types together!"]    	# list
pytuple = ("Tuples","can have","more than",2,"elements!")		# tuple
dictionary = {'one':1,'two':2,'three':3}				# hash/dictionary
variable_with_zero_data = None						# simple variable

# Simple logging in python
#=========================
print "Printed"

# Conditionals
#=============
if cake == "delicious":
	return "Yes,please!"
elif cake == "okay":
	return "I'll have a small piece."
else :
	return "No, thank you."

# Loops
#======
for item in list:
	print item
while(total < max_val):
	total += values[i]
	i +=2
# Functions
#==========
def divide(dividend,divisor):
	quotient = dividend/divisor
	remainder= dividend%divisor
	return quotient,remainder
def calculate_stuff(x,y):
	(q,r) = divide(x,y) # 	!NOTE : how the return values are being stored in tuples
	print q,r

# Classes
#========
class Person(object):
	def _init_(self,name,age): # This defines the constructor for the class
		self.name = name
		self.age  = age
	def birthday(self)
		self.age += 1

# Efficiency/Complexity
#======================
"""
	Here we talk about the BIG-O Notation and understanding 
	how it helps in making better algorithms
"""
# 2. LIST BASED COLLECTIONS

#  LINKED LISTS IN PYTHON
#========================

#  A NORMAL NODE
class Element(object):
	def _init_(self,value):
		self.value = value
		self.next = None # Remember that None is just like null in python

# INITIALIZING HEAD OF THE LINKED LIST 
class LinkedList(object):
	def _init_(self,head=None)
		self.head = head

# APPENDING AN ELEMENT IN THE LINKED LIST 
def append(self,new_element){
	current = self.head
	if self.head:
		while current.next:
			current = current.next
		current.next = new_element
	else:
		self.head = new_element
}

# PROGRAM FOR IMPLEMENTING LINKED LISTS IN PYTHON
#================================================

# DEFINES AN ELEMENT IN THE LINKED LIST
class Element(object):
	def _init_(self,value)
	self.value = value
	self.next = None
# LINKED LIST CLASS	
class LinkedList(object):
	
	# INITIALIZE HEAD OF THE LINKED LIST
	def _init_(self,head=None):
	self.head = head
	
	# APPENDING AN ELEMENT IN THE LINKED LIST
	def append(self,new_element):
	current = self.head
	if self.head:
		while current.next:
			current = current.next
		current.next = new_element
	else:
		self.head = new_element

	# GET POSITION OF AN ELEMENT IN THE LINKED LIST
	def get_position(self,position):
		counter = 1			# COUNTER FOR KEEPING TRACK OF POSITION WHILE ITERATION
		current = self.head 		# INITIALIZE CURRENT TO HEAD
		if position < 1:		# IF POSITION IS LESS THAN 1, GO BACK YOU!
			return None
		while current and counter <= position:	# GO-ON WHILE CURRENT IS ALIVE AND COUNTER IS YET NOT POSITION
			if counter == position
				return current
			current = current.next
			counter +=1
		return None

	# INSERTION INTO THE LINKED LIST
	def insert(self,new_element,position):
		counter = 1
		current = self.head
		if position == 1: 	# INSERTION HAS TO HAPPEN AT HEAD
			new_element.next = self.head
			self.head = new_element
		elif
			while current and counter < position: # SEE THAT IT IS GOING FOR < POSITION CAUSE IF IT SAYS POSITION=3, THEN IT HAS TO BE B/W 2 AND 3
				if counter == position - 1:
					new_element.next = current.next
					current.next = new_element
				current = current.next
				counter += 1
			elif position == 1:
				new_element.next = self.head
				self.head = new_element

	# DELETE A NODE IN THE LINKED LIST
	def delete(self,value):
		current = self.head
		previous = None
		while current.value != value and current.next:			# CASE WHEN IT'S NOT THE HEAD
			previous = current
			current = current.next
		if current.value == value: 					# CASE WHEN YOU HAVE TO DELETE FROM THE HEAD
			if previous:
				previous.next = current.next
			else 
				self.head = current.next
# 3. SEARCHING AND SORTING

# 4. MAPS AND HASHING

# 5. TREES

# 6. GRAPHS 

# 7. CASE STUDIES IN ALGORITHMS

# 8 . TECHNICAL INTERVIEW TIPS 

