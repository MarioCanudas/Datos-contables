import pandas as pds
import os
#generar información de los archivos:
def info_dts_gen(archivos):
    etiquetas = ['cmyc','mem','rmyb','vmyb','rmid','rpro','vcrb']
    for i,j in zip(archivos,etiquetas):
        #imprimir separador de información por su etiqueta
        print('-----------------------------------\n-----------------------------------')
        print(f'Información de datos {j}:\n')
        #obtener info de cada archivo
        i.info()

#convertir archivo xlsx a csv:
def xlsx_a_csv(archivo,carpeta,etiqueta):
    #abrir archivo excel
    xlsx = pds.read_excel(archivo)
    #crear el archico csv con la etiqueta
    csv_archivo = os.path.join(carpeta,f'{etiqueta}.csv')
    #convertir y sobreescrivir el archivo xlsx a csv en la carpeta
    xlsx.to_csv(csv_archivo,index=False)
    