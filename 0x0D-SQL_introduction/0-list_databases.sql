import mysql.connector

def list_databases():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
    )

    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")

    databases = []
    for database in cursor:
        databases.append(database[0])

    return databases

if __name__ == "__main__":
    databases = list_databases()
    print("The following databases are available:")
    for database in databases:
        print(database)
