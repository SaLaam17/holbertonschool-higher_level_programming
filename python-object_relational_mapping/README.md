# Python - Object-Relational Mapping (ORM)

In this project, we will bridge two fascinating worlds: **Databases** and **Python**!  
Throughout this project, you will learn to use **MySQLdb** to interact with a MySQL database and execute SQL queries, and **SQLAlchemy** to apply the **Object-Relational Mapping (ORM)** paradigm in Python.

## Objective

1. **Part 1:** Using **MySQLdb** to connect Python to a MySQL database and execute SQL queries.
2. **Part 2:** Using **SQLAlchemy**, an ORM, to interact with the database without writing SQL queries manually.

The main idea is to demonstrate data storage abstraction. With an ORM, you no longer write complex SQL queries; instead, you work directly with Python objects. This makes your code independent of the storage type (relational database, NoSQL, etc.) and easier to maintain.

## Technologies Used

- **Python**: Programming language used to develop the project.
- **MySQLdb**: Module to connect to a MySQL database and execute SQL queries.
- **SQLAlchemy**: ORM used to manipulate data as Python objects, without writing SQL.
- **MySQL**: Relational database used to store data.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/SaLaam17/holbertonschool-higher_level_programming.git cd python-orm
   ```

2. Create a virtual environment (recommended):
```python -m venv venv```
3. Activate the virtual environment:

    . On Windows:

    ```venv\Scripts\activate```<br>
    . On macOS/Linux:

    ```source venv/bin/activate```
4. Install the necessary dependencies:

    ```pip install -r requirements.txt```

Part 1: Using MySQLdb
In this part, you will connect to a MySQL database using MySQLdb and execute SQL queries.

Example of connecting to the database and retrieving data:

```
import MySQLdb

# Connect to the MySQL database
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()

# Execute the SQL query
cur.execute("SELECT * FROM states ORDER BY id ASC")  # Here, you need to know SQL to fetch the states

# Retrieve the results
query_rows = cur.fetchall()

# Print the results
for row in query_rows:
    print(row)

# Close the connection
cur.close()
conn.close()
```

In this example, you need to know how to write SQL queries to interact with the database. This approach is flexible, but it can become difficult to manage as the number of queries and operations grows.

Part 2: Using SQLAlchemy (ORM)
With SQLAlchemy, the goal is to eliminate the need to write SQL queries and interact only with Python objects. An ORM allows you to work with objects instead of dealing with raw SQL query results.

Example with SQLAlchemy:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, State  # Ensure your models are defined in models.py

# Connect to the MySQL database using SQLAlchemy
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

# Create tables in the database (if they don't already exist)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve the states and print them
for state in session.query(State).order_by(State.id).all():  # No SQL query here, just objects!
    print("{}: {}".format(state.id, state.name))

# Close the session
session.close()
```

<b>Advantages of ORM</b><br>
<b>Storage abstraction:</b> You no longer need to worry about how data is stored (MySQL, PostgreSQL, etc.). The code remains the same regardless of the database type.
Reduced complexity: You don't need to write raw SQL queries for CRUD (Create, Read, Update, Delete) operations.
Security: ORM protects against SQL injection by properly handling parameters in queries.
Project Structure

```
python-orm/
│
├── create_tables.py        # Script to create tables in the database
├── models.py               # ORM model definitions
├── config.py               # Database configuration
├── requirements.txt        # Project dependencies
└── README.md               # This file

Models
Models are defined in the models.py file. Here is an example of a State model:

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
```
<b>Contribution</b><br>
Contributions are welcome! If you'd like to contribute to this project, follow these steps:

Fork the repository
Create a branch for your feature or bug fix
Make your changes
Submit a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for more details.


### Additional Explanation:

- **Part 1 (MySQLdb)**: The connection and execution of SQL queries are done explicitly. You need to write SQL queries to interact with the database. This approach is flexible but can become difficult to maintain as your project grows.
  
- **Part 2 (SQLAlchemy ORM)**: SQLAlchemy allows you to work with Python objects instead of worrying about SQL syntax. You define Python models that represent your tables, and you can interact with the database in a more intuitive way.

This updated `README.md` reflects the two approaches and highlights the benefits of using an ORM over traditional SQL queries.


#!/Users/laamrisaid/holberton/holbertonschool-higher_level_programming/python-object_relational_mapping/venv/bin/python3
