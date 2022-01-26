import mysql.connector  # pip install mysql-connector-python


# db connectionnn
def open_connection(user, password, database):
    print("opening connection to " + database )
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



def insert_auto():
    marca= input("marca :")
    modello=input("modello : ")
    colore=input("colore : ")
    targa=input("targa : " )
    data_acquisto=input("data_acquisto : ")
    id_categoria=input("id_categoria : ")
    query = f"""insert into auto(marca,modello,colore,targa,data_acquisto,id_categoria)
    VALUES ("{marca}","{modello}","{colore}","{targa}","{data_acquisto}",{id_categoria}) """
    print(query)
    return query

# main
try:
    connection = open_connection("root", "root", "autonoleggio")
    #INSERIMENTO AUTO
    # query = insert_auto()
    # print("QUERY: "+ query)

    # result = do_query(connection, query)

    #PIE CHART
    query = """select marca, count(*) 
                        from auto
                        group by marca"""
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
