import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime, timedelta

def get_weather_forecast(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def parse_weather_forecast(data):
    forecasts = []
    for item in data['list']:
        forecast_date = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
        forecast_weather = {
            'date': forecast_date,
            'temperature': item['main']['temp'],
            'description': item['weather'][0]['description']
        }
        forecasts.append(forecast_weather)
    return forecasts

def check_weather_warnings(forecasts):
    warnings = []
    for forecast in forecasts:
        if 'thunderstorm' in forecast['description'].lower():
            warnings.append(f"{forecast['date']}: Thunderstorm warning!")
        if 'tornado' in forecast['description'].lower():
            warnings.append(f"{forecast['date']}: Tornado warning!")
        if 'hurricane' in forecast['description'].lower():
            warnings.append(f"{forecast['date']}: Hurricane warning!")
    return warnings

def display_weather_forecast(city, forecasts, warnings):
    root = tk.Tk()
    root.title(f"Weather forecast for {city}")
    
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    label_city = ttk.Label(frame, text=f"Weather forecast for {city}", font=('Helvetica', 16))
    label_city.pack()

    text_weather = tk.Text(frame, wrap="word", height=20, width=50)
    text_weather.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_weather.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    text_weather.config(yscrollcommand=scrollbar.set)

    for forecast in forecasts:
        text_weather.insert(tk.END, f"{forecast['date']}: {forecast['description']}, {forecast['temperature']}°C\n")

    if warnings:
        text_weather.insert(tk.END, "\nWarnings:\n")
        for warning in warnings:
            text_weather.insert(tk.END, f"{warning}\n")
    
    text_weather.configure(state='disabled')
    
    root.mainloop()

def get_weather_and_display(event=None):
    city = entry_city.get()
    api_key = "YOUR_API_KEY"
    data = get_weather_forecast(city, api_key)
    if 'cod' in data and data['cod'] == '200':
        forecasts = parse_weather_forecast(data)
        warnings = check_weather_warnings(forecasts)
        display_weather_forecast(city, forecasts, warnings)
    else:
        print("Failed to retrieve weather data. Please check your city name or API key.")

# GUI
root = tk.Tk()
root.title("Weather Forecast")

label_city = ttk.Label(root, text="Enter city:")
label_city.pack()

entry_city = ttk.Entry(root)
entry_city.pack()
entry_city.focus()

entry_city.bind("<Return>", get_weather_and_display)

button_submit = ttk.Button(root, text="Get Weather", command=get_weather_and_display)
button_submit.pack()

root.mainloop()
