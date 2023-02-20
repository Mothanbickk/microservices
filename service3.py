import time
from sql_queries import create_table, complete_repairing

create_table()

if __name__ == '__main__':
    while True:
        complete_repairing()
        print("completed")
        time.sleep(20)
