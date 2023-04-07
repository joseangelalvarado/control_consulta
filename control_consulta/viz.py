import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def grafica_triage():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    cursor1.execute(
        'SELECT codigo FROM paciente INNER JOIN triage ON triage.id_triage = paciente.id_triage')
    paciente = cursor1.fetchall()

    seleccion = []

    for row in paciente:
        seleccion.append(row[0])

    cursor1.close()
    conexion.close()

    ve = seleccion.count('verde')
    am = seleccion.count('amarillo')
    ro = seleccion.count('rojo')

    colores = ['green', 'yellow', 'red']

    triage_list = ve, am, ro
    triage_labels = ['Urgencia menor', 'Urgencia', 'Urgencia vital']
    plt.pie(triage_list,
            colors=colores, autopct="%.1f%%", pctdistance=1.2)
    plt.title('Consultas por Triage')
    plt.legend(triage_labels, bbox_to_anchor=(0, 1))
    plt.show()


'''def grafica_fecha():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    cursor1.execute(
        'SELECT fecha, COUNT(*) as cantidad FROM paciente GROUP BY fecha;')
    paciente = cursor1.fetchall()

    fechas = []
    cantidades = []

    for fecha, cantidad in paciente:
        fechas.append(fecha)
        cantidades.append(cantidad)

    cursor1.close()
    conexion.close()

    sns.lineplot(x=fechas, y=cantidades, data=paciente, color='darkslateblue')
    xticks = plt.xticks()[0]
    plt.title('Consultas por Fechas')
    plt.xticks(xticks[::1])
    plt.show()'''


def grafica_edad():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    cursor1.execute(
        'SELECT edad, COUNT(*) as total_edad FROM paciente GROUP BY edad')
    paciente = cursor1.fetchall()

    edades = []
    totales = []

    for edad, total_edad in paciente:
        edades.append(edad)
        totales.append(total_edad)

    cursor1.close()
    conexion.close()
    etiquetas = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    fig, ax = plt.subplots()
    ax.bar(edades, totales)
    plt.title('Consulta por Edad')
    plt.show()


def grafica_semanas():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    cursor1.execute(
        'SELECT COUNT(*) sdg FROM paciente WHERE sdg > 0 AND sdg < 13')
    trimestre1 = cursor1.fetchall()

    cursor1.execute(
        'SELECT count(*) sdg FROM paciente WHERE sdg > 12 AND sdg < 25 ')
    trimestre2 = cursor1.fetchall()

    cursor1.execute(
        'SELECT COUNT(*) sdg FROM paciente WHERE sdg > 24 AND sdg < 42')
    trimestre3 = cursor1.fetchall()

    cursor1.execute('SELECT COUNT(*) sdg FROM paciente')
    total = cursor1.fetchall()

    primero = []
    segundo = []
    tercero = []
    totales = []

    for trim1 in trimestre1:
        primero.append(trim1)

    for trim2 in trimestre2:
        segundo.append(trim2)

    for trim3 in trimestre3:
        tercero.append(trim3)

    for numero in total:
        totales.append(numero)

    x = primero[0]
    y = segundo[0]
    z = tercero[0]

    newlist = x, y, z
    resultado = [a[0] for a in newlist]
    etiquetas = ["Primer trimestre", "Segundo trimestre", "Tercer trimestre"]

    plt.pie(resultado, labels=etiquetas, autopct="%.1f%%",
            pctdistance=1.2, labeldistance=1.4)
    plt.title('Consulta por trimestre')
    plt.show()


def grafica_fecha():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()

    query = """ SELECT fecha FROM paciente"""

    df = pd.read_sql(query, conexion)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y/%b/%d')
    df = df.groupby(pd.Grouper(key='fecha', freq='M')
                    ).size().reset_index(name='count')
    df['month'] = df['fecha'].dt.year
    df = df.sort_values(by='month')

    plt.plot(df['fecha'].dt.strftime('%Y/%b'), df['count'])
    plt.show()


def queries():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    df = pd.read_sql(
        'SELECT * FROM paciente', conexion)

    df.to_csv('C:\\Users\\angel\\Desktop\\Proyectos\\Platzi\\base_consulta.csv')
