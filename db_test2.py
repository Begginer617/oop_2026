import mysql.connector

### Tworzenie połączenia
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to DB successful")
    except OSError as e:
        print(f"ERROR occured: '{e}' ")
    return connection

connection = create_connection("localhost", "root", "automaty")

## Wysyłanie skryptu SQL do bazy
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OSError as e:
        print(f"ERROR occured: '{e}' ")

select_polisy = "SELECT * FROM baza1.polisy"
polisy = execute_read_query(connection, select_polisy)

## Obsługa returna ze zwroconej tabeli wedlug wysłanego skryptu SQL
for numerpolisy in polisy:
    print(numerpolisy)