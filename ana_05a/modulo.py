import pandas as pds
import os

def df_de_xlsx(tipo,etiqueta):
    #definir un dataframe con un archivo csv que este en la misma carpeta solo poporcionando la etiqueta
    if tipo == 'GYA' or tipo == 'PP':
        df = df = pds.read_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','ana_05a',f'Archivos GYC', f'{tipo}-{etiqueta}.xlsx')))
    else:
        df = pds.read_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','ana_05a',f'Archivos {tipo}', f'{tipo}-{etiqueta}.xlsx')))
    #definir las columnas con las que nos queremos quedar
    if tipo == 'CC':
        columnas = ['Fecha','Cliente','Cobrado','ID Operación']
    elif tipo == 'NOM':
        columnas = ['Fecha','Empleado','Total']
    elif tipo == 'GYA':
        columnas = ['Fecha','Proveedor','Pagado','Saldo','Impuestos']
    elif tipo == 'PP':
        columnas  = ['Fecha','Proveedor','Total Aplicado']
    #elimnar todas las columnas exepcto con las que nos queremos quedar
    df_L = df[columnas]
    #agregar columna etiqueta para diferenciar de donde provienen los datos en el cruce
    df_L.loc[:,'Etiqueta'] = etiqueta
    return df_L

def gen_GYC_GEN():
    #definir carpeta de destino del archivo cruzado, y definir todas las etiquetas
    carpeta = r'G:\Mi unidad\Proyectos Análisis de Datos\1_Visualizaición de información contable-02a\ana_05a'
    etiquetas = ['CMCY','MEM','RMYB','VMYB','RMID','RPRO','VCRB']
    #definir un dataframe vacio para despues modificarlo en el for-in
    df_cruzado = pds.DataFrame()
    for i in etiquetas:
        #definir dataframes de cada tipo y por etiqueta
        df_GYA = df_de_xlsx('GYA',i)
        df_PP = df_de_xlsx('PP',i)
        #unir las columnas que contienen la información necesaria en una sola
        df_GYA['Columnas_gen'] = df_GYA['Fecha'].astype(str) + '_' + df_GYA['Proveedor'] + '_' + df_GYA['Pagado'].astype(str)
        df_PP['Columnas_gen'] = df_PP['Fecha'].astype(str) + '_' + df_PP['Proveedor'] + '_' + df_PP['Total Aplicado'].astype(str)
        #cruzar datos de los archivos
        df_GYA_u = df_GYA[~df_GYA['Columnas_gen'].isin(df_PP['Columnas_gen'])].drop(columns=['Columnas_gen'])
        df_PP_u = (df_PP.drop(columns=['Columnas_gen'])).rename(columns={'Total Aplicado':'Pagado'})
        #unir los dataframes en uno solo
        df_cruzado = pds.concat([df_cruzado,df_GYA_u,df_PP_u],ignore_index= True)
    archivo_vacio = os.path.join(carpeta,'GYC-GEN.xlsx')
    df_cruzado.to_excel(archivo_vacio,index=False)
    print('Archivo GYC-GEN.xlsx creado.')
    
def gen_CC_GEN():
    #definir la carpeta de destino
    carpeta = r"G:\Mi unidad\Proyectos Análisis de Datos\1_Visualizaición de información contable-02a\ana_05a"
    #definir lista con etiquetas para posteriormente definir los dataframes de cada una
    etiquetas = ['CMCY','MEM','RMYB','VMYB','RMID','RPRO','VCRB']
    #definir un dataframe vació para concatenarlo posteriormente, en un bucle for-in y obtener un dataframe general de los datos 
    df_gen_desordenado = pds.DataFrame()
    for i in etiquetas:
        #definir cada dataframe con la lista iterada por el for-in
        df_relativo = df_de_xlsx('CC',i)
        #al final del bucle deberia de tener todos los datos de cada uno de los archivos
        df_gen_desordenado = pds.concat([df_gen_desordenado,df_relativo],ignore_index=True)
    #ordenar el df por fecha (opcional)
    df_gen_desordenado['Fecha'] = pds.to_datetime(df_gen_desordenado['Fecha'],format="%d/%m/%Y")
    df_gen_ordenado = df_gen_desordenado.sort_values(by='Fecha')
    #crear un archivo vacio para despues sobreescribirlo con la info del df general (el que contiene todos los datos)
    archivo_vacio = os.path.join(carpeta,f'CC-GEN.xlsx')
    #sobreescribir la info del df general al archivo csv
    df_gen_ordenado.to_excel(archivo_vacio,index=False)
    #imprimir que el proceso esta listo
    print('Archivo CC-GEN.xlsx creado.')
    
def gen_NOM_GEN():
    #definir la carpeta de destino
    carpeta = r"G:\Mi unidad\Proyectos Análisis de Datos\1_Visualizaición de información contable-02a\ana_05a"
    #definir lista con etiquetas para posteriormente definir los dataframes de cada una
    etiquetas = ['CMCY','MEM','RMYB','VMYB','RMID','RPRO','VCRB']
    #definir un dataframe vació para concatenarlo posteriormente, en un bucle for-in y obtener un dataframe general de los datos 
    df_gen_desordenado = pds.DataFrame()
    for i in etiquetas:
        #definir cada dataframe con la lista iterada por el for-in
        df_relativo = df_de_xlsx('NOM',i)
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
    print('Archivo NOM-GEN.xlsx creado.')

gen_CC_GEN()
gen_GYC_GEN()
gen_NOM_GEN()