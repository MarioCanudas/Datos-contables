import funciones_variadas_nomina as fx
import os
#exportar archivos:
arch_cmcy = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\nomina centro de medios y comercio de yucatan.xlsx"
arch_mem = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\Nomina medios electrónicos.xlsx"
arch_rmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\nomina radio mayab.xlsx"
arch_vmyb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\nomina voz del mayab.xlsx"
arch_rmid = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\Nomina radio merida.xlsx"
arch_rpro = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\nomina radio progreso.xlsx"
arch_vcrb = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina\archivos xlsx\nomina voz del caribe.xlsx"
carpeta = r"C:\Users\mario\OneDrive - Universidad Autonoma de Yucatan\Proyectos Análisis de Datos\1_Visualizaición de información contable - Cadena rasa\Inf Contable_Datos crudos\Nomina"
list_arch = [arch_cmcy,arch_mem,arch_rmyb,arch_vmyb,arch_rmid,arch_rpro,arch_vcrb]
etiquetas = fx.etiquetas
for i,j in zip(list_arch,etiquetas):
    fx.xlsx_a_csv(i,carpeta,j)