import requests

def get_weather_data():
    response = requests.request("GET", "https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=25&lat=53.23&lon=10.98", headers = {"Accept": "application/json", "User-Agent": "JSHSJ/Weather jshsj@hey.com"})
    return response.json()

# def lookupWindDirection(dir):
#     if (dir >= 0 and dir < 45):
#         return "🡻"
#     elif (dir >= 45 and dir < 90):
#         return "🡿"
#     elif (dir >= 90 and dir < 135):
#         return "🡸"
#     elif (dir >= 135 and dir < 180):
#         return "🡼"
#     elif (dir >= 180 and dir < 225):
#         return "🡹"
#     elif (dir >= 225 and dir < 270):
#         return "🡽"
#     elif (dir >= 270 and dir < 315):
#         return "🡺"
#     elif (dir >= 315 and dir < 360):
#         return "🢆"
#     else:
#         return "Failed to lookup wind direction"

def format_weather_data(weather_data):
    time_series = weather_data["properties"]["timeseries"]
    first = time_series[0]["data"];
    instant = first["instant"];
    temp = instant["details"]["air_temperature"];
    wind_speed = instant["details"]["wind_speed"] * 3.6;
    wind_from_direction = instant["details"]["wind_from_direction"];
    next_hour_rain = first["next_1_hours"]["details"]["precipitation_amount"];
    rain_next_16_hours = [t["data"]["next_1_hours"]["details"]["precipitation_amount"] for t in time_series[0 : 16]];
    total_rain_next_16_hours = 0;
    for i in range(len(rain_next_16_hours)):
      total_rain_next_16_hours=total_rain_next_16_hours+rain_next_16_hours[i]

    return {
        "temp": temp,
        "wind_speed": wind_speed,
        "wind_from_direction": wind_from_direction,
        "next_hour_rain": next_hour_rain,
        "total_rain_next_16_hours": total_rain_next_16_hours
    }


weather = get_weather_data();
formatted_weather = format_weather_data(weather);
print('weather:', formatted_weather);
