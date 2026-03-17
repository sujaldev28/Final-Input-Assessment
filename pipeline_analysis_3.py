def robust_pipeline_engine(stream_1, stream_2):
    cleaned_set = set()
    error_log = []
    raw_data = stream_1 + stream_2
    for item in raw_data:
        try:
            clean_id = int(item)
            cleaned_set.add(clean_id)      
        except (ValueError, TypeError) as e:
            error_log.append(f"Invalid Data: {item}, Error: {e}")
    return cleaned_set, error_log

stream_a = [101, "102", None, "Alpha", 103]
stream_b = [103, "104", "102", "Error_99", 105]
cleaned_data, failures = robust_pipeline_engine(stream_a, stream_b)
print("Cleaned Data:", cleaned_data)
print("Error logs:")
for entry in failures:
    print(entry)