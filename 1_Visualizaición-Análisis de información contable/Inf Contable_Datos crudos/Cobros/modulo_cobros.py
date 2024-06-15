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
    
#crear archivos con etiqueta codigo para guardar los datos limpios
def arch_nvos_limpios(clave_tipo,carpeta):
    etiquetas = ['cmyc','mem','rmyb','vmyb','rmid','rpro','vcrb']
    for i in etiquetas:
        #con cada etiqueta se creara un archivo clave_tipo-ETIQUETA.csv
        os.path.join(carpeta,f'{clave_tipo}-{i.capitalize()}.csv')
    print('Archivos creados en la carpeta')

#exportar archivos de cobro a clientes desde carpeta local
archivo_cmcy = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobro clientes centro de medios y comercio de yucatan.csv"
archivo_mem = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobro clientes medios electronicos de mérida.csv"
archivo_rmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobro clientes radio mayab.csv"
archivo_vmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobros clientes voz del mayab.csv"
archivo_rmid = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobro de clientes radio merida.csv"
archivo_rpro = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobros cliente radio progreso.csv"
archivo_vcrb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Cobros\cobros de cliente voz del caribe.csv"
#leer los archivos .csv 
dts_gen = leer_archivos(archivo_cmcy,archivo_mem,archivo_rmyb,archivo_vmyb,archivo_rmid,archivo_rpro,archivo_vcrb)
