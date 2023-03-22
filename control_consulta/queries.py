import psycopg2


def load_data():

    conexion = psycopg2.connect(
        host='localhost', database='Consulta', user='postgres', password='181208')
    cursor1 = conexion.cursor()
    try:
        cursor1.execute(
            "SELECT nombres, ap_paterno, ap_materno, edad, sdg, motivo_consulta, fecha, codigo FROM paciente INNER JOIN triage ON triage.id_triage = paciente.id_triage; ")
        for row in cursor1.fetchall():
            tabla.insert("", 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        conexion.close()

    except:
        pass


def clean_table(tabla):

    registros = tabla.get_children()

    for registro in registros:
        tabla.delete(registro)
