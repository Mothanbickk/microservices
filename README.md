Task:
Create a new table: repair, with the following columns:
- id (int, primary key)
- description (varchar)
- city (varchar)
- price (integer)
- loss_estimate (integer)
- amount (integer)
- created (date) default now
- status (varchar) default "new"

Services: 
1. Create a new repairing every minute.
1. Read all repairing from the database and multiplies price by loss_estimate and stores it in amount and change status to "paid". 
1. Update all repairing with status "paid" and change status to "done".

Instructions:

Inserting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (type, description, amount) VALUES (%s, %s, %s)", (expense.type, 
expense.description, expense.amount))
conn.commit()
```
    
Selecting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return [{
        "id": expense[0],
        "type": expense[1],
        "description": expense[2],
        "amount": expense[3],
        "created": expense[4]
    } for expense in expenses
    ]
```