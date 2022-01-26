import mysql.connector  # pip install mysql-connector-python


# db connectionnn
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


# def show_bar_chart(result):
#     import numpy as np
#     labels, ys = zip(*result)
#     xs = np.arange(len(labels))
#     width = 1
#
#     plt.bar(xs, ys, width, align='center')
#
#     plt.xticks(xs, labels)  # Replace default x-ticks with xs, then replace xs with labels
#     plt.yticks(ys)
#     plt.show()

def show_pie_chart(result):
    import matplotlib.pyplot as plt
    values_ar = []
    labels_ar = []
    for row in result:
        labels_ar.append(row[0])
        values_ar.append(row[1])
    plt.pie(values_ar, labels=labels_ar)
    plt.show()

    # main


try:
    # aprire la connessione
    connection = open_connection("root", "root", "autonoleggio")
    # comporre la query
    query = """select marca, count(*) 
                from auto
                group by marca""";
    # eseguire la query
    result = do_query(connection, query)
    # visualizzare il resultset
    for row in result:
        print(row)

    # show_bar_chart(result)
    show_pie_chart(result)
    # chiudere la connessione
except mysql.connector.Error as e:
    print(e)

finally:
    close_connection(connection)
