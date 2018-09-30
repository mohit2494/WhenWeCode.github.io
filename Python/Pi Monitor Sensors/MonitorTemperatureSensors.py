import os 
import os.path
import re								# regular expressions
import time
from datetime import datetime
import json								# for handling JSON objects
import sys
from crontab import CronTab
import subprocess
from threading import Thread
import smtplib								# Library for sending emails
## Pending Library Import 
#Import sensor library here

# Adding Dummy Sensors for Now
sensors = {
    "DummySensor1":{
        "MaxTrigger": 20,
        "MinTrigger": 10
    },
    "DummySensor2":{
        "MaxTrigger":20,
        "MinTrigger":10
    }
}				
coldStorageName = "Cold Storage Default"
emailTo = "deepikakalra09@gmail.com"
emailFromUsername = "mohit2494@gmail.com"
emailFromPassword = ""							# Shouldn't be shown publicly though
notificationTime = 10
settingsDelim = '\n' 							# The Default Delimiter we are setting is next line
cronJob = type('system_cron',(object,),{})() 				# Creating an object of system level cron job

def clear(message):
	os.system('cls')
	print(message)

# Main Menu of the program
def setupEmail(message):
	# clear the console
	clear(message)
	# import global variables
	global emailTo
	global emailFrom
	global emailFromUsername
	global emailFromPassword
	global notificationTime
	print("---------------------------------------------------------------------------\n\t")
	print("Welcome to the email setup menu! You can choose from the following options: \n\t")
	print("---------------------------------------------------------------------------\n\t")
	print("1. Change receiver's email: \n\t"+emailTo)
	print("2. Change senders's email: \n\t"+emailFromUsername)
	print("3. change sender's password: \n\t"+emailFromPassword)
	print("4. Change time to wait between consecutive notifications: \n\t"+str(notificationTime))
	print("5. Main Menu")
	try:
		navigateTo = input(">") 		# Prompt for user to input the menu choice
	except:
		setupEmail("I didn't understand.Please enter a valid choice or navigate to Main Menu.") # Default Case Run
	actualNavigateTo = 0; 				# Default Navigation Step
	
	try : 
		actualNavigateTo = int(navigateTo)
	except: 
		actualNavigateTo = -1			# input entered is not a proper integer
	if(actualNavigateTo < 1 or actualNavigateTo >5 ): 
		setupEmail("I didn't understand.Please enter a valid choice or navigate to Main Menu.") # Default Case Run
	if(actualNavigateTo == 1 ): changeReceiversEmail()
	if(actualNavigateTo == 2 ): changeSendersEmail()
	if(actualNavigateTo == 3 ): changeSendersPassword()
	if(actualNavigateTo == 4 ): changeNotificationTime()
	if(actualNavigateTo == 5): mainMenu("")
	setupEmail("I didn't understand.Please enter a valid choice or navigate to Main Menu.") # Default Case Run

# Change Cold Storage Name
def changeColdStorageName():
	global coldStorageName
	clear("Loading Cold Storage Change Program.....\n\n\t")
	print("Current Cold Storage Name : " + coldStorageName + '\n\n Please Enter New Cold Storage Name : \n')
	newName = input (">")
	if(len(newName)<1) : 
		return
	coldStorageName = newName
	return
	#saveSettings()

# This function flushes the old sensor list and gets in the new one
def detectSensors():
	global sensors
	clear("We are currently running a dummy set of sensors! We'll soon be working with the real ones!\n")
	print("Here is the sensor configuration we have right now..\n")
	for key in sensors:
		print("Sensor Name: \t" + key)
		print("Maximum Trigger Temperature: " + str(sensors[key]['MaxTrigger']) + " Degrees in Celcius\n\t")
		print("Minimum Trigger Temperature: " + str(sensors[key]['MinTrigger']) + " Degrees in Celcius\n")
	input("Press Any Key to return! ..")
	mainMenu("")

# Print temperature from sensors
def printTemperatureSettings():
	global sensors
	clear("We are currently running a dummy set of sensors! We'll soon be working with the real ones!\n")
	print("Here is the sensor configuration we have right now..\n")
	for key in sensors:
		print("Sensor Name: \t" + key)
		print("Maximum Trigger Temperature: " + str(sensors[key]['MaxTrigger']) + " Degrees in Celcius\n\t")
		print("Minimum Trigger Temperature: " + str(sensors[key]['MinTrigger']) + " Degrees in Celcius\n")
	input("Press Any Key to return! ..")
	mainMenu("")

# Main Menu Function for running the program
def mainMenu(message):
	clear(message)
	print('------------------------------------------------------------ \n\t')
	print('Welcome to the Main Menu! Choose from the folloing choices : \n\t')
	print('------------------------------------------------------------ \n\t')
	print('1. Change Cold Storage Name: \n\t Current Cold Storage Name: '+coldStorageName)
	print('2. Setup Sensors:\n\t '+str(len(sensors))+' are active!')
	print('3. View temperature settings and values:\n\t')
	print('4. Setup Notifications:\n\t')
	print('5. Run temperature monitoring: Monitoring ('+("not ")+"running!)\n\t")
	print('6. Add or remove monitoring from cron jobs:\n\t')
	print('7. Save and Exit:\n\t')
	try:
		navigateTo = input(">")
	except:
		MainMenu("I did not understand. Please try again!.")
	actualNavigateTo = 0 
	try : 
		actualNavigateTo = int(navigateTo)
	except:
		actualNavigateTo = -1
	if(actualNavigateTo < 1 or actualNavigateTo > 7):
		mainMenu("I did not understand. Please try again!.")
	if(actualNavigateTo == 1):
		changeColdStorageName()
	if(actualNavigateTo == 2):
		detectSensors()
	if(actualNavigateTo == 3):
		printTemperatureSettings()
	if(actualNavigateTo == 4):
		setupEmail("")
	if(actualNavigateTo == 5):
		monitorForever()
	if(actualNavigateTo == 6):
		addRemoveCron()
	if(actualNavigateTo == 7):
		saveSettings()
		if(thre.isAlive()): thre._Thread_stop()
		exit(0)
	mainMenu("I did not understand. Please try again!.")

mainMenu("")