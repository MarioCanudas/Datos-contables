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
        
#leer todos los archivos de una lista con las variables donde estan las rutas de los archivos
def leer_archivos(archivo_cmcy,archivo_mem,archivo_rmyb,archivo_vmyb,archivo_rmid,archivo_rpro,archivo_vcrb):
    dts_cmcy = pds.read_csv(archivo_cmcy,encoding='latin1') 
    dts_mem = pds.read_csv(archivo_mem,encoding='latin1') 
    dts_rmyb = pds.read_csv(archivo_rmyb,encoding='latin1') 
    dts_vmyb = pds.read_csv(archivo_vmyb,encoding='latin1') 
    dts_rmid = pds.read_csv(archivo_rmid,encoding='latin1') 
    dts_rpro = pds.read_csv(archivo_rpro,encoding='latin1') 
    dts_vcrb = pds.read_csv(archivo_vcrb,encoding='latin1') 
    dts_gen = [dts_cmcy,dts_mem,dts_rmyb,dts_vmyb,dts_rmid,dts_rpro,dts_vcrb]
    return dts_gen

#convertir archivo xlsx a csv:
def xlsx_a_csv(archivo,carpeta,etiqueta):
    #abrir archivo excel
    xlsx = pds.read_excel(archivo)
    #crear el archico csv con la etiqueta
    csv_archivo = os.path.join(carpeta,f'{etiqueta}.csv')
    #convertir y sobreescrivir el archivo xlsx a csv en la carpeta
    xlsx.to_csv(csv_archivo,index=False)