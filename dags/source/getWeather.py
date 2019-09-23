import requests
import json
from datetime import datetime 
import os

# defining variables
# json_data = ''

def get_weather():
	"""
	Query openweathermap.com's API and to get the weather for
	Brooklyn, NY and then dump the json to the //data/ directory 
	with the file name "<today's date>.json"
	"""

	# My API key is defined in my config.py file.
	paramaters = {'q': 'Brooklyn, USA', 'appid':'25237a5210330ad588a2a33c388da468'}

	result     = requests.get("http://api.openweathermap.org/data/2.5/weather?", paramaters)

	# If the API call was sucessful, get the json and dump it to a file with 
	# today's date as the title.
	if result.status_code == 200 :
		# Get the json data 
		json_data = result.json()
		# print(json_data)
		
		# create directory
		createDirectory()

		# make file 
		filename = "data/" + str(datetime.now().date()) + '.json'    	
		
		with open(filename, 'w') as file:
			print(filename)
			json.dump(json_data, file)
			print(json_data)
			print("closing file . . . ")            
        	
	else :
		print ("Error In API call.")

# function to create directory 
def createDirectory():
    # creating directory 
    dirName = "data"
    
    # create target directory if don't exists    
    if not os.path.exists(dirName):
    # exception handeling for file not found
        try:
            os.makedirs(dirName)
            print("Directory ", dirName, "Created")

        except FileExistsError as fe:
            print("Error : ", fe)
            print("Directory ", dirName, "already exists")


if __name__ == "__main__":
	get_weather()