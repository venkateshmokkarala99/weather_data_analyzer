# Weather Log Analyzer
# ============================================================
# Reads a full year of daily weather data for two cities from a CSV file
# Parses date strings into proper date objects for accurate processing
# Filters records by city to analyse each city separately
# Extracts temperature values from filtered records for calculations
# Calculates monthly averages for temperature and humidity and total rainfall per city
# Identifies the hottest day, coldest day, and rainiest day from the records
# Saves a structured monthly summary report as a JSON file in the outputs folder
# Prints a clean formatted report in the terminal showing all records and key findings

# Step 1: Create the outputs folder if it does not already exist

# Step 2: Read all weather records from the CSV file
#         and parse the date string into a date object

# Step 3: Filter records for a specific city

# Step 5: Calculate monthly averages for temperature,
#         humidity, and total rainfall for a given city

# Step 6: Find the hottest day, coldest day, and
#         rainiest day from the records

# Step 7: Save the monthly summary to a JSON file
#         inside the outputs folder

# Step 8: Print a clean formatted report in the terminal
#         showing all records and key findings

# Step 9: Run the full pipeline — load data, analyse
#         both cities, save the report, print results
# ============================================================
import csv 
import json
from pathlib import Path
from datetime import datetime 

# Step 1: Create the outputs folder if it does not already exist
def set_up_folder():
    outputs_folder = Path("outputs")
    outputs_folder.mkdir(exist_ok=True)
    print(f"folder created: {outputs_folder} successfully")

#Step 2: Read all weather records from the CSV file
#        and parse the date string into a date object
def load_weather_data(filename):
    records = []
    try:
        with open(filename, newline= "",encoding = "utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["date"] = datetime.strptime(row["date"], "%d-%m-%Y")
                row['temperature_c'] = float(row['temperature_c'])
                row['humidity_pct'] = float(row['humidity_pct'])
                row['rainfall_mm'] = float(row['rainfall_mm'])
                records.append(row)

    except FileNotFoundError:
        print(f"file is not found:{filename}")
    
    return records

# Step 3: Filter records for a specific city
def filter_by_city(data,city):
    filter_data = list(filter(lambda record:record['city'] == city ,data))
    return filter_data

 # step 4: getting tempertaures 
def get_temperatures(data):
    temperatures = list(map(lambda record : record['temperature_c'] , data))
    return temperatures

# Step 5: monthly summary 
def monthly_summary(data):
    month_names = [record["date"].strftime("%B") for record in data]
    unique_months = [
        month for index, month in enumerate(month_names)
        if month not in month_names[:index]
    ]
    summary = {
        month: {
            "avg_temperature_c": round(
                sum(r["temperature_c"] for r in data if r["date"].strftime("%B") == month)
                / len([r for r in data if r["date"].strftime("%B") == month]),
                1
            ),
            "avg_humidity_pct": round(
                sum(r["humidity_pct"] for r in data if r["date"].strftime("%B") == month)
                / len([r for r in data if r["date"].strftime("%B") == month]),
                1
            ),
            "total_rainfall_mm": round(
                sum(r["rainfall_mm"] for r in data if r["date"].strftime("%B") == month),
                1
            )
        }
        for month in unique_months
    }

    return summary


# 6. FIND EXTREMES

def find_extremes(data):


    hottest_day = max(data, key=lambda record: record["temperature_c"])
    coldest_day = min(data, key=lambda record: record["temperature_c"])
    rainiest_day = max(data, key=lambda record: record["rainfall_mm"])

    extremes = {
        "hottest": hottest_day,
        "coldest": coldest_day,
        "rainiest": rainiest_day
    }

    return extremes


# 7. SAVE SUMMARY

def save_summary(summary, filename):

    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(summary, json_file, indent=4)
        print(f"\nMonthly summary saved to: {filename}")

    except Exception as error:
        print(f"Error saving summary: {error}")


# 8. PRINT REPORT

def print_report(data):
      if not data:
        print("No data to display.")
        return
      city_name = data[0]["city"]
      print(f"\n{'=' * 60}")
      print(f"  Weather Report: {city_name}")
      print(f"{'=' * 60}")
      print(f"{'Date':<14} {'Temp (°C)':>10} {'Humidity':>10} {'Rainfall':>10}  Condition")
      print(f"{'-' * 60}")

      for record in data:
        date_str = record["date"].strftime("%d %b %Y")
        print(
            f"{date_str:<14}"
            f"{record['temperature_c']:>9.1f}°"
            f"{record['humidity_pct']:>9.1f}%"
            f"{record['rainfall_mm']:>9.1f}mm"
            f"  {record['condition']}"
        )



      summary = monthly_summary(data)

      print(f"\n{'=' * 60}")
      print(f"  Monthly Summary: {city_name}")
      print(f"{'=' * 60}")
      print(f"{'Month':<12} {'Avg Temp':>10} {'Avg Humidity':>14} {'Total Rain':>12}")
      print(f"{'-' * 60}")

      for month, stats in summary.items():
        print(
            f"{month:<12}"
            f"{stats['avg_temperature_c']:>9.1f}°"
            f"{stats['avg_humidity_pct']:>13.1f}%"
            f"{stats['total_rainfall_mm']:>11.1f}mm"
        )

      extremes = find_extremes(data)

      print(f"\n{'=' * 60}")
      print(f"  Extreme Days: {city_name}")
      print(f"{'=' * 60}")

      hottest = extremes["hottest"]
      coldest = extremes["coldest"]
      rainiest = extremes["rainiest"]

      print(
        f"  Hottest day : {hottest['date'].strftime('%d %b %Y')} — "
        f"{hottest['temperature_c']}°C ({hottest['condition']})"
    )
      print(
        f"  Coldest day : {coldest['date'].strftime('%d %b %Y')} — "
        f"{coldest['temperature_c']}°C ({coldest['condition']})"
    )
      print(
        f"  Rainiest day: {rainiest['date'].strftime('%d %b %Y')} — "
        f"{rainiest['rainfall_mm']}mm ({rainiest['condition']})"
    )
      print(f"{'=' * 60}")

      temperatures = get_temperatures(data)
      avg_temp = round(sum(temperatures) / len(temperatures), 1)
      print(f"\n  Year average temperature for {city_name}: {avg_temp}°C")


def main():
    set_up_folder()

    all_data = load_weather_data("weather_data.csv")

    if not all_data:
        print("No data loaded. Exiting.")
        return

    # Step 3: Filter data by city and print the Mumbai report
    mumbai_data = filter_by_city(all_data, "Mumbai")
    print_report(mumbai_data)

    # Step 4: Filter data by city and print the Delhi report
    delhi_data = filter_by_city(all_data, "Delhi")
    print_report(delhi_data)

    # Step 5: Build a combined monthly summary and save it to JSON
    # We use a dictionary comprehension to merge both city summaries
    combined_summary = {
        city: monthly_summary(filter_by_city(all_data, city))
        for city in ["Mumbai", "Delhi"]
    }
    save_summary(combined_summary, "outputs/monthly_summary.json")


# Run main() only when this script is executed directly
if __name__ == "__main__":
    main()


    

