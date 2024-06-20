import pandas as pds
import os

def df_de_xlsx(etiqueta):
    #definir un dataframe con un archivo csv que este en la misma carpeta solo poporcionando la etiqueta
    df = pds.read_excel((os.path.join(os.path.dirname(__file__),f'NOM-{etiqueta}.xlsx')))
    #definir las columnas con las que nos queremos quedar
    columnas = ['Fecha','Empleado','Total']
    #elimnar todas las columnas exepcto con las que nos queremos quedar
    df_L = df[columnas]
    #agregar columna etiqueta para diferenciar de donde provienen los datos en el cruce
    df_L.loc[:,'Etiqueta'] = etiqueta
    return df_L

def gen_NOM_GEN():
    #definir la carpeta de destino
    carpeta = r"G:\Mi unidad\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\ana_03a\NOM"
    #definir lista con etiquetas para posteriormente definir los dataframes de cada una
    etiquetas = ['CMCY','MEM','RMYB','VMYB','RMID','RPRO','VCRB']
    #definir un dataframe vació para concatenarlo posteriormente, en un bucle for-in y obtener un dataframe general de los datos 
    df_gen_desordenado = pds.DataFrame()
    for i in etiquetas:
        #definir cada dataframe con la lista iterada por el for-in
        df_relativo = df_de_xlsx(i)
        #al final del bucle deberia de tener todos los datos de cada uno de los archivos
        df_gen_desordenado = pds.concat([df_gen_desordenado,df_relativo],ignore_index=True)
    #ordenar el df por fecha (opcional)
    df_gen_desordenado['Fecha'] = pds.to_datetime(df_gen_desordenado['Fecha'],format="%d/%m/%Y")
    df_gen_ordenado = df_gen_desordenado.sort_values(by='Fecha')
    #crear un archivo vacio para despues sobreescribirlo con la info del df general (el que contiene todos los datos)
    archivo_vacio = os.path.join(carpeta,f'NOM-GEN.xlsx')
    #sobreescribir la info del df general al archivo csv
    df_gen_ordenado.to_excel(archivo_vacio,index=False)
    #imprimir que el proceso esta listo
    print('Archivo NOM-GEN.xlsx generado en carpeta de cobros a clientes.')

gen_NOM_GEN()
