import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# ---------- Starter tests ----------
def test_calm_wind():
    assert wind_alert(10) == "none"

def test_no_alerts():
    assert overall_alert([]) == "none"


# ---------- wind_alert ----------
def test_wind_warning():
    assert wind_alert(100) == "warning"

def test_wind_watch():
    assert wind_alert(70) == "watch"

def test_wind_advisory():
    assert wind_alert(45) == "advisory"


# ---------- rain_alert ----------
def test_rain_heavy_saturated():
    assert rain_alert(60, True) == "warning"

def test_rain_heavy_not_saturated():
    assert rain_alert(60, False) == "watch"

def test_rain_moderate_saturated():
    assert rain_alert(20, True) == "watch"

def test_rain_moderate_not_saturated():
    assert rain_alert(20, False) == "advisory"

def test_rain_light():
    assert rain_alert(2, False) == "none"


# ---------- heat_alert ----------
def test_heat_warning():
    assert heat_alert(46, 30) == "warning"

def test_heat_watch():
    assert heat_alert(41, 30) == "watch"

def test_heat_advisory():
    assert heat_alert(36, 30) == "advisory"

def test_heat_none():
    assert heat_alert(25, 30) == "none"

def test_heat_humidity_raises_index():
    # 38 + (80-40)*0.1 = 42 -> watch
    assert heat_alert(38, 80) == "watch"


# ---------- overall_alert ----------
def test_overall_picks_worst():
    assert overall_alert(["advisory", "warning", "watch"]) == "warning"

def test_overall_unknown_alert():
    with pytest.raises(ValueError):
        overall_alert(["advisory", "storm"])
