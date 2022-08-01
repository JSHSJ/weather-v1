import urequests
# from machine import Pin, SPI

# # SPIV on ESP32
# sck = Pin(18)
# miso = Pin(19)
# mosi = Pin(23)
# dc = Pin(32)
# cs = Pin(33)
# rst = Pin(19)
# busy = Pin(35)
# spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=sck, miso=miso, mosi=mosi)

# e = epaper4in2.EPD(spi, cs, dc, rst, busy)
# e.init()

w = 400
h = 300
x = 0
y = 0

# --------------------

# use a frame buffer
# 400 * 300 / 8 = 15000 - thats a lot of pixels
# import framebuf
# buf = bytearray(w * h // 8)
# fb = framebuf.FrameBuffer(buf, w, h, framebuf.MONO_HLSB)
# black = 0
# white = 1
# fb.fill(white)


def get_weather_data():
    response = urequests.request("GET", "https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=25&lat=53.23&lon=10.98", headers = {"Accept": "application/json", "User-Agent": "JSHSJ/Weather jshsj@hey.com"})
    return response.json()

def format_weather_data(weather_data):
    time_series = weather_data["properties"]["timeseries"]
    first = time_series[0]["data"];
    instant = first["instant"];
    temp = instant["details"]["air_temperature"];
    wind_speed = instant["details"]["wind_speed"];
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
