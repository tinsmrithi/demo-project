from src.weather import get_temperature_label

CONDITION_ICONS = {
    "sunny": "☀️",
    "cloudy": "☁️",
    "rainy": "🌧️",
    "snowy": "❄️",
    "windy": "💨",
}


def format_weather_line(weather):
    """Return a single formatted weather summary string."""
    icon = CONDITION_ICONS.get(weather["condition"], "🌡️")
    label = get_temperature_label(weather["temperature"])
    return (
        f"{icon}  {weather['city']} | "
        f"{weather['temperature']}°C | "
        f"{weather['condition'].capitalize()} | "
        f"{label}"
    )


def print_weather_report(weather_list):
    """Print a formatted weather report for a list of cities."""
    print("=" * 50)
    print("       🌍  WEATHER REPORT")
    print("=" * 50)
    for weather in weather_list:
        print(format_weather_line(weather))
    print("=" * 50)


def print_single_city(weather):
    """Print weather for a single city."""
    print(f"\n📍 Weather for {weather['city']}:")
    print(f"   Temperature : {weather['temperature']}°C")
    print(f"   Condition   : {weather['condition'].capitalize()}")
    print(f"   Feels like  : {get_temperature_label(weather['temperature'])}")