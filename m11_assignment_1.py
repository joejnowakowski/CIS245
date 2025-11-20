# Institution: Bellevue University
# Course: CIS 245 Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 11/19/2025

"""
INSTRUCTIONS:
Create a Python applicaiton that asks the user for their zip code. Validate the format of the 
the zip code entered with regular expressions. Use the zip code to obtain weather forecast 
data from opweathermap.org's api. Use the given api key to access the open weather map web
service. Print the unformatted JSON response received. 
"""



import json, requests, re



def main():
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "906b6939735602a519447e37a839d229" #  api key
    flag = True

    while flag:
        zip_code = input("Enter the zip code for the weather look up: ")

        x = validate_zip_code(zip_code)   

        if x == None: 
            print ("Invalid zip code:", zip_code)
        
        else:
            unformatted_data = get_weather_data(base_url, zip_code, appid)
            print(unformatted_data) # json-formatted nested dictionary
            print(json.dumps(unformatted_data, indent=4))


        continue_lookup = input("Would you like to continue looking up the weather? [Y/N]").lower()

        if continue_lookup not in ["yes", "y"]:
            flag = False

def validate_zip_code(zip):
    """Validates given argument to match a specific pattern; a number 5 times."""
    zip_code = re.fullmatch("[0-9]{5}", zip) # full match specifies Only 5 numbers
    return zip_code

def get_weather_data(base_url, zip_code, appid):
    """Construct a url based on required format using given data. Request a JSON resonse from url and return the unformatted data"""
    # needed to use this format; one in video, I think, is outdated. I found this format in the website's JSON section
    url = f"{base_url}?zip={zip_code},us&units=imperial&appid={appid}" 
    response = requests.get(url)
    unformatted_data = response.json()
    return unformatted_data

if __name__ == "__main__":
    main()