import os
import shutil
from datetime import datetime

def rotate_log_file(logfile, backup_dir):
    if os.path.exists(logfile):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_log = os.path.join(backup_dir, f"log_{timestamp}.log")
        shutil.move(logfile, backup_log)
        open(logfile, 'w').close()  # Create a new empty log file
        print(f"Log rotated and saved as {backup_log}")
    else:
        print(f"{logfile} does not exist.")

if __name__ == "__main__":
    logfile = "/path/to/logfile.log"
    backup_dir = "/path/to/log/backups"
    rotate_log_file(logfile, backup_dir)
