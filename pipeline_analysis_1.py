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