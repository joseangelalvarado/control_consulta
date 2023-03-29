import psycopg2
import matplotlib.pyplot as plt


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
