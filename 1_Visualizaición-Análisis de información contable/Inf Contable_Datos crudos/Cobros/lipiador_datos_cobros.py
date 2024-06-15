import pandas as pds
import os
archivo_CMCY = os.path.join(os.path.dirname(__file__),'CC-CMCY-C.csv')
df_CMCY = pds.read_csv(archivo_CMCY,encoding='latin1')
columnas = ['Fecha','Cliente','Cobrado','ID Operacion']
df_CMCY_L = df_CMCY[columnas]
df_CMCY_L.info()

def elim_colum_CC(nombre):
    #solicitar nombre del archivo .csv (habilitar cuando se implemente en el menú)
    #nombre = input('Inserta el nombre clave (XX-YYYY-C.csv) del archivo:') 
    #abrir/importar el archivo
    archivo = os.path.join(os.path.dirname(__file__),nombre)
    #crear dataframe del archivo importado
    df = pds.read_csv(archivo,encoding='latin1')
    #columnas con las que se conserva
    x = ['Fecha','Cliente','Cobrado','ID Operacion']
    #dataframe limpio
    df_L = df[x]
    #devuelve el valor del dataframe limpio
    return df_L
