import pytest
from src.weather import get_weather, get_humidity_label, get_temperature_label


def test_get_weather_returns_valid_dict():
    result = get_weather("Mumbai", 32, "sunny")
    assert result == {"city": "Mumbai", "temperature": 32, "condition": "sunny"}


def test_get_weather_title_cases_city_and_strips_whitespace():
    result = get_weather("  new delhi  ", 28, "cloudy")
    assert result["city"] == "New Delhi"


def test_get_weather_raises_for_empty_city():
    with pytest.raises(ValueError, match="City must be a non-empty string"):
        get_weather("", 25, "sunny")


def test_get_weather_raises_for_invalid_condition():
    with pytest.raises(ValueError, match="Condition must be one of"):
        get_weather("Paris", 20, "hailing")


def test_get_weather_raises_for_invalid_temperature():
    with pytest.raises(ValueError, match="Temperature must be a number"):
        get_weather("Tokyo", "hot", "sunny")


def test_get_temperature_label_returns_very_hot_when_above_35():
    assert get_temperature_label(40) == "Very Hot"


def test_get_temperature_label_returns_freezing_when_below_5():
    assert get_temperature_label(-10) == "Freezing"


def test_get_temperature_label_raises_when_not_a_number():
    with pytest.raises(ValueError, match="Temperature must be a number"):
        get_temperature_label("warm")


def test_get_humidity_label_returns_very_humid_when_high():
    assert get_humidity_label(85) == "Very Humid"


def test_get_humidity_label_returns_dry_when_low():
    assert get_humidity_label(30) == "Dry"


def test_get_humidity_label_raises_when_out_of_range():
    with pytest.raises(ValueError, match="Humidity must be between 0 and 100"):
        get_humidity_label(101)


def test_get_humidity_label_raises_when_not_a_number():
    with pytest.raises(ValueError, match="Humidity must be a number"):
        get_humidity_label("high")