import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if not weather_data:
        print("No weather data available.")
        return
    
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        
        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {description.capitalize()}")
    except KeyError:
        print("Unexpected weather data format.")
        print(json.dumps(weather_data, indent=2))

def main():
    print("Welcome to the Python Weather App!")
    print("----------------------------------")
    
    # Get your free API key from https://openweathermap.org/api
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    
    while True:
        location = input("\nEnter city name (or 'quit' to exit): ").strip()
        if location.lower() == 'quit':
            break
            
        weather_data = get_weather(api_key, location)
        display_weather(weather_data)

if __name__ == "__main__":
    main()