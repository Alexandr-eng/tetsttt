import psycopg2
import json



DB_HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'test'
DB_PASSWORD = 'test'



conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()


cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()


data = []
for row in rows:
    data.append({
        'id': row[0],
        'name': row[1],
        'created_at': row[2].isoformat(),  # конвертация timestamp в формат ISO
        'price': round(row[3], 2),  # округление float до 2 знаков после запятой
        'description': row[4]
    })


with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


# Закрытие подключения к базе данных PostgreSQL
cur.close()
conn.close()