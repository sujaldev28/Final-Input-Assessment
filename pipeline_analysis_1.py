# Challenge 1: The Data Profiler (Easy)
# Goal: Master basic data manipulation and string formatting.
# ● Topics: Variables, Data Types, Strings, Lists.
# ● Task: Create a script that takes a list of "raw" sensor readings (strings with extra
# whitespace and mixed casing) and converts them into a clean, numerical list.
# ● Objective: 1. Create a list of strings: [" 23.5 ", "low", " 45.0", "HIGH ", "30.2"].
# 2. Use a loop to strip whitespace and convert all strings to lowercase.
# 3. Identify which values are numbers and store them in a new list as floats.

raw_readings = [" 23.5 ", "low", " 45.0", "HIGH ", "30.2"]
clean_readings = []
clean_numeric_readings = []
for data in raw_readings:
    data = data.strip().lower()
    clean_readings.append(data)
    if data.replace('.', '', 1).isdigit():
        clean_numeric_readings.append(float(data))
print("Cleaned Readings:", clean_readings)
print("Numeric Readings:", clean_numeric_readings)