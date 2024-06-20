import os
import pandas as pds

#CMCY,MEM,RMYB,VMYB,RMID,RPRO,VCRB 
etiquetas = ['CMCY','MEM','RMYB','VMYB','RMID','RPRO','VCRB']
#permite convertir un archivo .xlsx a un .csv guardandolo con su nombre clave en la carpeta donde se necesitara    
def xlsx_a_csv_menu():
    #solicitar ruta del archivo
    archivo = input(r'Inserta la ruta del archivo .xlsx que quieres agregar: ')[1:-1]
    #solicitar destino para el archivo nuevo
    carpeta = input(r'Inserta la ruta de la carpeta de destino para el nuevo archivo .csv: ')[1:-1]
    #solicitar etiqueta del archivo
    nombre = input('Inserta el nuevo nómbre del archivo en clave: ')
    #leer el archivo xlsx
    xlsx = pds.read_excel(archivo)
    #crear el archico csv con la etiqueta
    csv_archivo = os.path.join(carpeta,f'{nombre}-C.csv')
    #convertir y sobreescrivir el archivo xlsx a csv en la carpeta
    xlsx.to_csv(csv_archivo,index=False,encoding = 'latin1')
    #imprimir resultado
    print(f'Archivo {nombre}.csv creado y guardado en la carpeta')
    
