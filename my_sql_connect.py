import mysql.connector
#db connectionnn
def open_connection(user, password, database):
    connection = mysql.connector.connect(user=user, password=password, host='localhost', database=database)
    return connection

def close_connection(connection):
    connection.close()
    print("connection closed")

def do_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result

# main
try:
    # aprire la connessione
    connection = open_connection("root", "root", "sneakers")
    # eseguire la query
    query = """select brand,model,buyer_region from orders limit 1000"""
    result = do_query(connection, query)
    # visualizzare il resultset
    for row in result:
        print(row[1])

# chiudere la connessione

except mysql.connector.Error as e:
    print(e)

finally:
    close_connection(connection)
