import pytest
from src.weather import get_weather
from src.display import format_weather_line, print_weather_report, print_single_city


def test_format_weather_line_contains_city():
    weather = get_weather("London", 18, "rainy")
    line = format_weather_line(weather)
    assert "London" in line


def test_format_weather_line_contains_icon():
    weather = get_weather("Oslo", -2, "snowy")
    line = format_weather_line(weather)
    assert "❄️" in line


def test_format_weather_line_contains_temperature_label():
    weather = get_weather("Dubai", 38, "sunny")
    line = format_weather_line(weather)
    assert "Very Hot" in line


def test_print_weather_report_prints_header(capsys):
    weather_list = [get_weather("Berlin", 15, "cloudy")]
    print_weather_report(weather_list)
    captured = capsys.readouterr()
    assert "WEATHER REPORT" in captured.out
    assert "Berlin" in captured.out


def test_print_single_city_prints_all_fields(capsys):
    weather = get_weather("Sydney", 26, "windy")
    print_single_city(weather)
    captured = capsys.readouterr()
    assert "Sydney" in captured.out
    assert "26" in captured.out
    assert "Warm" in captured.out