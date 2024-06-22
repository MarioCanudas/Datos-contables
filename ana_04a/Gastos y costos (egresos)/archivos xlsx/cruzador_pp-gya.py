import pandas as pds
import os

def df_de_xlsx(tipo,etiqueta):
    #definir un dataframe con un archivo csv que este en la misma carpeta solo poporcionando la etiqueta
    df = pds.read_excel((os.path.join(os.path.dirname(__file__),f'{tipo}-{etiqueta}.xlsx')))
    #definir las columnas con las que nos queremos quedar
    if tipo == 'GYA':
        columnas = ['Fecha','Proveedor','Pagado','Saldo','Impuestos']
    elif tipo == 'PP':
        columnas  = ['Fecha','Proveedor','Total Aplicado']
    #elimnar todas las columnas exepcto con las que nos queremos quedar
    df_L = df[columnas]
    #agregar columna etiqueta para diferenciar de donde provienen los datos en el cruce
    df_L.loc[:,'Etiqueta'] = etiqueta
    return df_L

def cruzar_PP_GYA():
    #definir carpeta de destino del archivo cruzado, y definir todas las etiquetas
    carpeta = r'G:\Mi unidad\Proyectos Análisis de Datos\1_Visualizaición de información contable-02a\ana_04a\Gastos y costos (egresos)'
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
    
cruzar_PP_GYA()
    