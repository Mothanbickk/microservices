import time
from sql_queries import create_table, update_repairing

create_table()

if __name__ == '__main__':
    while True:
        update_repairing()
        print("updated")
        time.sleep(20)
