import os
import tarfile
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    backup_filename = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"
    backup_filepath = os.path.join(backup_dir, backup_filename)

    with tarfile.open(backup_filepath, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    
    print(f"Backup completed: {backup_filepath}")

if __name__ == "__main__":
    source = "/path/to/important/data"
    destination = "/path/to/backup/location"
    backup_directory(source, destination)