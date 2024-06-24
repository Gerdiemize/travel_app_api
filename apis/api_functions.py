import requests
import json

def get_events_near(latitude, longitude, keyword, start_date_time=None, end_date_time=None):
    url = f'https://app.ticketmaster.com/discovery/v2/events?apikey=fgl3sn6jWwuYstYGZ48xRfGNTN43vUr6&keyword={keyword}&latlong={latitude},{longitude}&radius=10&unit=km&source=ticketmaster&locale=*'
    
    if start_date_time:
        url += f'&startDateTime={start_date_time}'
    
    if end_date_time:
        url += f'&endDateTime={end_date_time}'
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request failed with status: {response.status_code}.')
            raise Exception('Failed to send question to the API')
    except Exception as e:
        print(f'Error making GET request: {e}')
        raise Exception('Failed to send question to the API')

# Example usage
#latitude = 40.7128
#longitude = -74.0060
#keyword = 'music'
#start_date_time = '2024-05-01T00:00:00Z'
#end_date_time = '2024-05-31T23:59:59Z'

#events = get_events_near(latitude, longitude, keyword, start_date_time, end_date_time)
#print(events)

def get_current_weather_conditions(latitude, longitude):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=80954fd7c9c131813443ad2e0e8d6aa4'
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request failed with status: {response.status_code}.')
            raise Exception('Failed to get weather conditions from the API')
    except Exception as e:
        print(f'Error making GET request: {e}')
        raise Exception('Failed to get weather conditions from the API')

# Example usage
#latitude = 40.7128
#longitude = -74.0060

#weather_conditions = get_current_weather_conditions(latitude, longitude)
#print(weather_conditions)

def fetch_airbnb_data(location, checkin_date, checkout_date, number_of_adults, number_of_children, number_of_infants):
    url = f'https://airbnb13.p.rapidapi.com/search-location?location={location}&checkin={checkin_date}&checkout={checkout_date}&adults={number_of_adults}&children={number_of_children}&infants={number_of_infants}&pets=0&page=1&currency=USD'
    
    headers = {
        'X-RapidAPI-Key': '23341a914fmsh5f85f224b3b1e19p14a2f5jsn5fd592c49b8c',
        'X-RapidAPI-Host': 'airbnb13.p.rapidapi.com'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request failed with status: {response.status_code}.')
            raise Exception('Failed to fetch data from Airbnb API')
    except Exception as e:
        print(f'Error making GET request: {e}')
        raise Exception('Failed to fetch data from Airbnb API')

# Example usage
location = "Paris"
checkin_date = "2024-07-16"
checkout_date = "2024-07-19"
number_of_adults = "1"
number_of_children = "0"
number_of_infants = "0"

airbnb_data = fetch_airbnb_data(location, checkin_date, checkout_date, number_of_adults, number_of_children, number_of_infants)
print(airbnb_data)