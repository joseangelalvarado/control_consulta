from tkinter import *
from tkinter import ttk
import queries
import psycopg2
from datetime import datetime
import validaciones
import viz


def run():

    # Ventana Principal

    root = Tk()
    root.title('Admisión Consulta Tococirugía')
    root.geometry('1000x600')
    frame = Frame(root)
    frame.pack()
    root.config(background="gray90")

    frame_1 = Frame(root)
    frame_1.pack(anchor=NW)
    frame_1.config(bg='gray90')

    # Consultas a la base de datos

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

    def clean_table():

        registros = tabla.get_children()

        for registro in registros:
            tabla.delete(registro)

    def borracampos():

        nombres.set("")
        ap_paterno.set("")
        ap_materno.set("")
        edad.set("")
        semanas.set("")
        motivo.set("")
        seleccion.set("Codigo Triage")

    def inserta_datos():

        conexion = psycopg2.connect(
            host='localhost', database='Consulta', user='postgres', password='181208')
        mifecha = datetime.now()
        actual = mifecha.strftime('%Y-%m-%d %H:%M:%S')
        cursor1 = conexion.cursor()
        cursor1.execute(
            "INSERT INTO paciente (nombres, ap_paterno, ap_materno, edad, sdg, motivo_consulta, fecha, id_triage) VALUES('" + nombres.get() + "','" + ap_paterno.get() + "','" + ap_materno.get() + "'," + edad.get() + "," + semanas.get() + ",'" + motivo.get() + "','" + str(actual) + "'," + seleccion.get() + ")")
        conexion.commit()
        conexion.close()

    # Etiqueta datos generales

    label_datos = Label(frame_1, text='Datos de Paciente',
                        fg='MediumPurple3', font=('sans serif', 18, 'bold'), bg='gray90')
    label_datos.grid(row=0, column=0, padx=30, pady=20)

    # Frame donde se ingresaran los datos

    frame_2 = Frame(root)
    frame_2.pack()
    frame_2.config(bg='gray90')

    nombres = StringVar()
    ap_paterno = StringVar()
    ap_materno = StringVar()
    edad = StringVar()
    semanas = StringVar()
    motivo = StringVar()
    # Nombres

    label_nombre = Label(frame_2, text='Nombres',
                         fg='MediumPurple3', font=('sans serif', 11, 'bold'), bg='gray90')
    label_nombre.grid(row=0, column=0, padx=20, sticky='w')
    entry_nombre = Entry(frame_2, width=25, textvariable=nombres, validate='key',
                         validatecommand=(root.register(validaciones.validar_nombre), '%S'))
    entry_nombre.grid(row=1, column=0, padx=20, pady=5)

    # Apellido paterno

    label_apaterno = Label(frame_2, text='Apellido Paterno',
                           fg='MediumPurple3', font=('sans serif', 11, 'bold'), bg='gray90')
    label_apaterno.grid(row=0, column=1, padx=20, sticky='w')
    entry_apaterno = Entry(frame_2, width=25, textvariable=ap_paterno, validate='key',
                           validatecommand=(root.register(validaciones.validar_nombre), '%S'))
    entry_apaterno.grid(row=1, column=1, padx=20, pady=5)

    # Apellido materno

    label_materno = Label(frame_2, text='Apellido Materno',
                          fg='MediumPurple3', font=('sans serif', 11, 'bold'), bg='gray90')
    label_materno.grid(row=0, column=2, padx=20, sticky='w')
    entry_materno = Entry(frame_2, width=25, textvariable=ap_materno, validate='key',
                          validatecommand=(root.register(validaciones.validar_nombre), '%S'))
    entry_materno.grid(row=1, column=2, padx=20, pady=5)

    # Edad

    label_edad = Label(frame_2, text='Edad', fg='MediumPurple3',
                       font=('sans serif', 11, 'bold'), bg='gray90')
    label_edad.grid(row=0, column=3, padx=20, sticky='w')
    entry_edad = Entry(frame_2, width=10, textvariable=edad, validate='key', validatecommand=(
        root.register(validaciones.validar_num), '%S', '%P'))
    entry_edad.grid(row=1, column=3, padx=20, pady=5)

    # Semanas de gestación

    label_semanas = Label(frame_2, text='Semanas de gestacíon',
                          fg='MediumPurple3', font=('sans serif', 11, 'bold'), bg='gray90')
    label_semanas.grid(row=0, column=4, padx=20, sticky='w')
    entry_semanas = Entry(frame_2, width=10, textvariable=semanas, validate='key', validatecommand=(
        root.register(validaciones.validar_sdg), '%S', '%P'))
    entry_semanas.grid(row=1, column=4, padx=20, pady=5, sticky='w')

    # Motivo consulta

    label_motivo = Label(frame_2, text='Motivo de consulta',
                         fg='MediumPurple3', font=('sans serif', 11, 'bold'), bg='gray90')
    label_motivo.grid(row=2, column=0, padx=20, pady=10, sticky='w')
    entry_motivo = Entry(frame_2, width=25, textvariable=motivo, validate='key',
                         validatecommand=(root.register(validaciones.validar_nombre), '%S'))
    entry_motivo.grid(row=3, column=0, padx=10, pady=10)

    # Triage

    colores = {1: 'Verde', 2: 'Amarillo', 3: 'Rojo'}
    seleccion = StringVar(frame_2)
    seleccion.set('Codigo Triage')
    menumotivo = OptionMenu(frame_2, seleccion, *colores.keys())
    menumotivo.grid(row=3, column=1)
    menumotivo.config(fg='MediumPurple4', font=('sans serif', 11, 'bold'))
    # Botones

    guardar = Button(frame_2, text="Guardar", width=10,
                     fg='MediumPurple4', font=('sans serif', 11, 'bold'), command=inserta_datos)
    guardar.grid(row=3, column=2)

    boton_ver = Button(frame_2, text="Registros", width=10,
                       fg='MediumPurple4', font=('sans serif', 11, 'bold'), command=load_data)
    boton_ver.grid(row=3, column=3)

    # Tabla de registros

    frame_3 = Frame(root)
    frame_3.pack()
    frame_3.config(background='gray90')

    tabla = ttk.Treeview(frame_3, heigh=10,  columns=(
        '#0', '#1', '#2', '#3', '#4', '#5', '#6'))
    tabla.grid(row=5, column=0, padx=10, pady=30)
    tabla.column('#0', width=150)
    tabla.heading('#0', text="Nombres", anchor=CENTER)
    tabla.column('#1', width=150)
    tabla.heading('#1', text="Apellido Paterno", anchor=CENTER)
    tabla.column('#2', width=150)
    tabla.heading('#2', text="Apellido Materno", anchor=CENTER)
    tabla.column('#3', width=80)
    tabla.heading('#3', text="Edad", anchor=CENTER)
    tabla.column('#4', width=80)
    tabla.heading('#4', text="SDG", anchor=CENTER)
    tabla.column('#5', width=130)
    tabla.heading('#5', text="Motivo", anchor=CENTER)
    tabla.column('#6', width=120)
    tabla.heading('#6', text="Fecha", anchor=CENTER)
    tabla.column('#7', width=100)
    tabla.heading('#7', text="Triage", anchor=CENTER)

    # Comandos
    # Menu de opciones

    menu_opciones = Menu(root)
    root.config(menu=menu_opciones)

    menu_buscar = Menu(menu_opciones, tearoff=0)
    menu_buscar.add_command(label='Buscar registro')

    menu_limpiar = Menu(menu_opciones, tearoff=0)
    menu_limpiar.add_command(label='Campos', command=borracampos)
    menu_limpiar.add_command(label='Tabla', command=clean_table)
    menu_limpiar.add_command(label='Registro', command=viz.grafica_triage)

    menu_est = Menu(menu_opciones, tearoff=0)
    menu_est.add_command(label='Triage')
    menu_est.add_command(label='Semanas de gestación')
    menu_est.add_command(label='Edad')
    menu_est.add_command(label='Fecha')

    menu_opciones.add_cascade(label='Buscar', menu=menu_buscar)
    menu_opciones.add_cascade(label='Limpiar', menu=menu_limpiar)
    menu_opciones.add_cascade(label='Estadisticas', menu=menu_est)

    root.mainloop()


if __name__ == '__main__':
    run()
