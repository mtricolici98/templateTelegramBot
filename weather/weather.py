def find_coord_for_city(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'appid': 'b27b49d9e275f365ef91907882000ab2',
    }
    import requests
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return dict(lat=response.json()[0]['lat'], lon=response.json()[0]['lon'])
    raise Exception('City data not found')


def get_weather(position_info: dict):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        **position_info,
        'appid': 'b27b49d9e275f365ef91907882000ab2',
        'units': 'metric'
    }

    import requests

    response = requests.get(url, params=params)

    print(response.request.url)

    if response.status_code == 200:
        print(response.json())
        data = response.json()
        return dict(
            weather=data['weather'][0]['main'],
            temp=data['main']['temp'],
        )
    raise Exception('Weather data not found.')


def get_weather_for_city(city_name):
    coord = find_coord_for_city(city_name)
    return get_weather(coord)
