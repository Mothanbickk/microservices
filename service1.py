import time
import random
from sql_queries import create_table, insert_repairing
from repairing import Repairing

create_table()

if __name__ == '__main__':
    while True:
        insert_repairing(
            Repairing(
                description=random.choice(["window", "door", "bell", "bed", "wash basin", "TV" ]),
                city =random.randint(1, 20),
                price=random.randint(500, 10000),
                loss_estimate=random.randint(1, 10),
                amount=0,
            )
        )
        print("Inserted")
        time.sleep(10)
