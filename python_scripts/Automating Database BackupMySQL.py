import os
from datetime import datetime 

def backup_mysql_db(db_name, user, password, output_dir):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = os.path.join(output_dir, f"{db_name}_{timestamp}.sql")
    os.system(f"mysqldump -u {user} -p{password} {db_name} > {backup_file}")
    print(f"Database backup completed: {backup_file}")

if __name__ == "__main__":
    backup_mysql_db("my_database", "db_user", "db_pass", "/path/to/backup/")
