from datetime import datetime

def read_log_file(file_path):
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) >= 3:
                timestamp_str = parts[0].strip()
                message = parts[1].strip()
                severity = parts[2].strip()
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    log_entries.append((timestamp, message, severity))
                except ValueError:
                    print(f"Ignoring invalid timestamp format: {timestamp_str}")
    return log_entries

def total_entries(log_entries):
    return len(log_entries)

def count_entries_by_severity(log_entries, severity):
    return sum(1 for entry in log_entries if entry[2] == severity)

def average_time_gap(log_entries):
    if len(log_entries) < 2:
        return None
    total_gap = sum((log_entries[i][0] - log_entries[i-1][0]).total_seconds()
                    for i in range(1, len(log_entries)))
    return total_gap / (len(log_entries) - 1)

if __name__ == "__main__":
    file_path = 'log_file.txt'  # Update with your log file path
    log_entries = read_log_file(file_path)

    print(f"Total number of entries: {total_entries(log_entries)}")
    severity = 'ERROR'  # Update with the severity level you want to count
    print(f"Number of entries with severity '{severity}': {count_entries_by_severity(log_entries, severity)}")

    avg_gap = average_time_gap(log_entries)
    if avg_gap is not None:
        print(f"Average time gap between entries: {avg_gap} seconds")
    else:
        print("Insufficient entries to calculate average time gap.")
