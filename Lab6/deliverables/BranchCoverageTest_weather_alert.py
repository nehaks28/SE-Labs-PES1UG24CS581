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


# ---------- Extra boundary / branch tests ----------
@pytest.mark.parametrize("speed,expected", [
    (38, "none"), (39, "advisory"), (61, "advisory"),
    (62, "watch"), (88, "watch"), (89, "warning"),
])
def test_wind_boundaries(speed, expected):
    assert wind_alert(speed) == expected

@pytest.mark.parametrize("mm,sat,expected", [
    (9, True, "none"), (10, False, "advisory"), (10, True, "watch"),
    (49, False, "advisory"), (49, True, "watch"),
    (50, False, "watch"), (50, True, "warning"),
])
def test_rain_boundaries(mm, sat, expected):
    assert rain_alert(mm, sat) == expected

def test_heat_humidity_exactly_40_not_added():
    assert heat_alert(34, 40) == "none"      # branch: humidity > 40 False

def test_heat_humidity_just_above_40():
    assert heat_alert(34.95, 41) == "advisory"  # 34.95 + 0.1 = 35.05

@pytest.mark.parametrize("temp,expected", [
    (34, "none"), (35, "advisory"), (39, "advisory"),
    (40, "watch"), (44, "watch"), (45, "warning"),
])
def test_heat_boundaries(temp, expected):
    assert heat_alert(temp, 20) == expected

def test_overall_single_alert():
    assert overall_alert(["watch"]) == "watch"

def test_overall_not_worse_branch():
    # later alert is not worse than current worst -> 'if' False
    assert overall_alert(["warning", "advisory", "none"]) == "warning"

def test_overall_all_none():
    assert overall_alert(["none", "none"]) == "none"

def test_overall_unknown_first():
    with pytest.raises(ValueError):
        overall_alert(["storm"])
