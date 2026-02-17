import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="automaty",
    database="baza1"
)

cursor = conn.cursor()

sql = """
SELECT 
    p.numerpolisy,
    p.kwota,
    p.terminplatnosci,
    r.rodzaj
FROM polisy p
JOIN rodzajeubezp r
    ON p.rodzajubezpieczenia = r.rodzajid
"""

cursor.execute(sql)
wyniki = cursor.fetchall()

for w in wyniki:
    print(w)

conn.close()


