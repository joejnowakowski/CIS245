# Institution: Bellevue University
# Course: CIS 245 Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 11/19/2025


"""
INSTRUCTIONS:
Using the program developed in Module 11: Part I (m11_assignment_1.py), parse the JSON response.
Display two of the weather related attributes from the main object in the JSON response.
"""


import json, requests, re



def main():
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "906b6939735602a519447e37a839d229" # api key
    flag = True

    while flag:
        zip_code = input("Enter the zip code for the weather look up: ")

        validated_response = validate_zip_code(zip_code)   

        if validated_response == None: 
            print ("Invalid zip code:", zip_code)
        
        else:
            unformatted_data = get_weather_data(base_url, zip_code, appid)
            # print(unformatted_data)
            temp = unformatted_data["main"]["temp"]
            city = unformatted_data["name"]
            humidity = unformatted_data["main"]["humidity"]
            
            print(f"\nThe current temperature in {city}, with a zip code of {zip_code}, is {temp}° F\n"
                  f"with {humidity}% humidity.\n")
        
        continue_lookup = input("Would you like to continue looking up the weather? [Y/N]").lower()

        if continue_lookup not in ["yes", "y"]:
            flag = False

def validate_zip_code(zip):
    """Validates given argument to match a specific pattern; a number 5 times."""
    zip_code = re.fullmatch("[0-9]{5}", zip)
    return zip_code

def get_weather_data(base_url, zip_code, appid):
    """Construct a url based on required format using given data. Request a JSON resonse from url and return the unformatted data."""
     # needed to use this format; the one in the video, I think, is outdated. 
     # It wouldn't work for me. I got a 404 error in the response output
     # I found this format in the website's JSON section
    url = f"{base_url}?zip={zip_code},us&units=imperial&appid={appid}"
    response = requests.get(url)
    unformatted_data = response.json()
    return unformatted_data

if __name__ == "__main__":
    main()