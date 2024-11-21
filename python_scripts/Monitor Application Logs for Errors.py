import re

def monitor_log(logfile, error_keyword):
    with open(logfile, 'r') as file:
        for line in file:
            if re.search(error_keyword, line):
                print(f"Error found: {line.strip()}")

if __name__ == "__main__":
    monitor_log("/path/to/application.log", "ERROR")