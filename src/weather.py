VALID_CONDITIONS = ["sunny", "cloudy", "rainy", "snowy", "windy"]


def get_weather(city, temperature, condition):
    """Return a weather data dict for a city."""
    if not city or not isinstance(city, str):
        raise ValueError("City must be a non-empty string")
    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number")
    if condition.lower() not in VALID_CONDITIONS:
        raise ValueError(f"Condition must be one of: {VALID_CONDITIONS}")

    return {
        "city": city.strip().title(),
        "temperature": temperature,
        "condition": condition.lower(),
    }


def get_temperature_label(temperature):
    """Return a human-readable label for a temperature value."""
    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number")
    if temperature >= 35:
        return "Very Hot"
    elif temperature >= 25:
        return "Warm"
    elif temperature >= 15:
        return "Mild"
    elif temperature >= 5:
        return "Cold"
    else:
        return "Freezing"


def get_humidity_label(humidity):
    """Return a label based on humidity percentage."""
    if not isinstance(humidity, (int, float)):
        raise ValueError("Humidity must be a number")
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity must be between 0 and 100")

    if humidity >= 80:
        return "Very Humid"
    elif humidity >= 60:
        return "Humid"
    elif humidity >= 40:
        return "Comfortable"
    else:
        return "Dry"