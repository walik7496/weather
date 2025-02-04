# Weather Forecast Application

This is a simple weather forecast application built using Python and Tkinter. The application retrieves weather forecast data from the OpenWeatherMap API and displays it in a user-friendly interface. It also checks for severe weather warnings (thunderstorms, tornadoes, hurricanes) and displays them alongside the forecast.

## Features

- **Weather Forecast**: Displays the temperature and weather description for the next few days.
- **Weather Warnings**: Identifies and shows warnings for thunderstorms, tornadoes, and hurricanes if present in the forecast.
- **User-Friendly GUI**: Built with Tkinter to provide an intuitive graphical user interface for easy interaction.
- **OpenWeatherMap API**: Retrieves weather data from the OpenWeatherMap API using your unique API key.

## Requirements

Before running the application, you need to install the required libraries:

- `tkinter` (for the graphical user interface)
- `requests` (for making HTTP requests to the OpenWeatherMap API)

You can install the `requests` library using pip if you don't have it already:

```bash
pip install requests
```

## Usage

1. Enter the City Name: Type the name of the city you want the forecast for in the text box.
2. Get the Weather: Press the "Enter" key or click the "Get Weather" button.
3. View the Forecast: The weather forecast for the next few days will appear in the scrollable text box, along with any severe weather warnings.

## Example Output

If the weather forecast includes a thunderstorm or a tornado warning, the output will look something like this:

```yaml
Weather forecast for London:
2025-02-05: Thunderstorm, 18°C
2025-02-06: Clear sky, 22°C
Warnings:
2025-02-05: Thunderstorm warning!
```

## License

This project is open-source and licensed under the MIT License.
