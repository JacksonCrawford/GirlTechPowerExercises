# Import pyowm (Python OpenWeatherMap) package to access API
import pyowm

# Define variables to store the weather stuff
owm = pyowm.OWM("c01234d923a2b4e0c5937810fa29090d")
wman = owm.weather_manager()

def getWeather(city, country):
    location = city + "," + country
    observation = wman.weather_at_place(location).weather
    return observation.temperature("fahrenheit")



# Get input from user here (usa is valid for country)
city = 
country = 

# Call the function and store it here
temp_data = 

# The data gathered from OWM is stored in a dictionary, which we can see the full contents of with this line:
print(temp_data)

#print("The high is:", temp_data["temp_max"])
#print("The current temperature is:", temp_data["temp"])
#print("The low is:", temp_data["temp_min"])

# Add a print statement to get the "feels_like" value


