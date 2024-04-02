from faker import Faker
import psycopg2
import random

# З'єднання з базою даних
conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="1111", host="localhost", port="5432"
)
cur = conn.cursor()

fake = Faker()

# Додавання користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Додавання статусів
statuses = ["new", "in progress", "completed"]
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Додавання завдань
for _ in range(20):
    title = fake.text(max_nb_chars=50)
    description = fake.text(max_nb_chars=200)
    status_id = random.randint(1, len(statuses))
    user_id = random.randint(1, 10)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id),
    )

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
cur.close()
conn.close()
