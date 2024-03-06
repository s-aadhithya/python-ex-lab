def read_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    print(f"Ignoring non-numeric data: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data

def perform_numerical_calculations(data):
    try:
        if not data:
            raise ValueError("No numerical data found.")
        total = sum(data)
        average = total / len(data)
        return total, average
    except ZeroDivisionError:
        print("Cannot calculate average: Division by zero.")
    except Exception as e:
        print(f"An error occurred during numerical calculations: {e}")

if __name__ == "__main__":
    file_path = 'data.txt'  # Update with your file path
    data = read_data_from_file(file_path)
    total, average = perform_numerical_calculations(data)
    if total is not None and average is not None:
        print(f"Total: {total}")
        print(f"Average: {average}")
