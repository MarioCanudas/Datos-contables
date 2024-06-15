import pandas as pds
import funciones_variadas_pagos as fx
#exportar archivos de cobro a clientes desde carpeta local
archivo_cmcy = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pago de proveedores centro de medios y comercio de yucatan.csv"
archivo_mem = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pagos proveedores medios electrónicos.csv"
archivo_rmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pago de proveedores radio mayab.csv"
archivo_vmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pago proveedores voz del mayab.csv"
archivo_rmid = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pago de proveedores radio merida.csv"
archivo_rpro = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pago proveedores radio progreso.csv"
archivo_vcrb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Pagos\pagos proveedores voz del caribe.csv"
lista_archivos = [archivo_cmcy,archivo_mem,archivo_rmyb,archivo_vmyb,archivo_rmid,archivo_rpro,archivo_vcrb]
#leer los archivos .csv 
dts_gen = fx.leer_archivos(archivo_cmcy,archivo_mem,archivo_rmyb,archivo_vmyb,archivo_rmid,archivo_rpro,archivo_vcrb)
#imprimir información del archivo
fx.info_dts_gen(dts_gen)