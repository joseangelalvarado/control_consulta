import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns


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

    plt.hist(seleccion)
    plt.show()


def grafica_fecha():

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

    sns.lineplot(x=fechas, y=cantidades, data=paciente)
    xticks = plt.xticks()[0]
    plt.xticks(xticks[::1])
    plt.show()


def grafica_edad():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    cursor1.execute(
        'SELECT edad FROM paciente')
    paciente = cursor1.fetchall()

    edad = []

    for row in paciente:
        edad.append(row[0])

    plt.hist(edad)
    plt.show()
