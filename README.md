# Weather Log Analyzer

A beginner-friendly Python project that reads real-world style weather data from a CSV file, analyzes it, and produces formatted reports and a JSON summary.

---

## Project Description

This project loads monthly weather records for two Indian cities — **Mumbai** and **Delhi** — covering the full year of 2024. It uses core Python concepts (no external libraries) to filter data, calculate statistics, find extreme days, and save results to a JSON file.

---

## Concepts Used

| Concept | Where it appears |
|---|---|
| Functions with docstrings | Every function in `weather_analyzer.py` |
| CSV reading | `load_weather_data()` using `csv.DictReader` |
| JSON writing | `save_summary()` using `json.dump()` |
| List comprehensions | Month extraction, temperature lists |
| Dictionary comprehensions | `monthly_summary()`, combined summary in `main()` |
| `filter()` with lambda | `filter_by_city()` |
| `map()` with lambda | `get_temperatures()` |
| `datetime` / `strptime` | Parsing `DD-MM-YYYY` date strings in `load_weather_data()` |
| `pathlib` | `setup_folders()` creates the `outputs/` directory |
| Error handling (`try/except`) | `load_weather_data()` catches `FileNotFoundError`, `save_summary()` catches write errors |
| Loops | Iterating records in `print_report()` |
| Conditionals | Guard clause in `print_report()`, early return in `main()` |
| f-strings | All formatted print statements |

---

## How to Run

1. Make sure Python 3.8 or higher is installed.
2. Place `weather_data.csv` and `weather_analyzer.py` in the same folder.
3. Open a terminal in that folder and run:

```
python weather_analyzer.py
```

4. The script will:
   - Create an `outputs/` folder automatically
   - Print weather reports for Mumbai and Delhi in the terminal
   - Save `outputs/monthly_summary.json`

No external packages are required. Only the Python standard library is used.

---

## Project Folder Structure

```
weather_log_analyser/
│
├── weather_data.csv          # Raw weather data (24 rows, 2 cities, 12 months each)
├── weather_analyzer.py       # Main Python script
├── README.md                 # This file
│
└── outputs/                  # Created automatically when the script runs
    └── monthly_summary.json  # JSON file with monthly stats for both cities
```

---

## Functions Overview

| Function | Purpose |
|---|---|
| `setup_folders()` | Creates the `outputs/` folder using `pathlib` |
| `load_weather_data(filename)` | Reads CSV, parses dates, returns list of dicts |
| `filter_by_city(data, city)` | Uses `filter()` + lambda to get one city's records |
| `get_temperatures(data)` | Uses `map()` + lambda to extract temperature values |
| `monthly_summary(data)` | Dictionary comprehension: avg temp, humidity, total rain per month |
| `find_extremes(data)` | Finds hottest, coldest, and rainiest days |
| `save_summary(summary, filename)` | Writes the summary dict to a JSON file |
| `print_report(data)` | Prints a formatted terminal report for one city |
| `main()` | Calls all functions in order |

---

## Sample Output

```
Folder ready: C:\...\weather_log_analyser\outputs

============================================================
  Weather Report: Mumbai
============================================================
Date           Temp (°C)   Humidity   Rainfall  Condition
------------------------------------------------------------
01 Jan 2024        31.2°      72.0%      2.1mm  Partly Cloudy
01 Feb 2024        32.5°      68.0%      0.5mm  Sunny
01 Mar 2024        34.8°      65.0%      1.2mm  Sunny
...

============================================================
  Monthly Summary: Mumbai
============================================================
Month          Avg Temp   Avg Humidity   Total Rain
------------------------------------------------------------
January           31.2°         72.0%        2.1mm
February          32.5°         68.0%        0.5mm
...

============================================================
  Extreme Days: Mumbai
============================================================
  Hottest day : 01 Apr 2024 — 36.1°C (Hot and Humid)
  Coldest day : 01 Aug 2024 — 28.5°C (Heavy Rain)
  Rainiest day: 01 Jul 2024 — 621.3mm (Very Heavy Rain)
============================================================

  Year average temperature for Mumbai: 31.7°C
```

And the saved `outputs/monthly_summary.json` looks like:

```json
{
    "Mumbai": {
        "January": {
            "avg_temperature_c": 31.2,
            "avg_humidity_pct": 72.0,
            "total_rainfall_mm": 2.1
        },
        ...
    },
    "Delhi": {
        "January": {
            "avg_temperature_c": 14.3,
            "avg_humidity_pct": 78.0,
            "total_rainfall_mm": 5.2
        },
        ...
    }
}
```
