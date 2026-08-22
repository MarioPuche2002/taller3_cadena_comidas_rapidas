from config import parametros
import pandas as pd
import numpy as np

def cargar_datos():
    par = parametros()
    file_path = par["ruta_archivo"]
    df = pd.read_csv(file_path, parse_dates=["fecha"])
    df = df.sort_values("fecha").reset_index(drop=True)
    
    df_dias = pd.get_dummies(df['dia_semana'], prefix='dia', dtype=int)
    df = pd.concat([df, df_dias], axis=1)
    
    df['mes'] = df['fecha'].dt.month
    df_meses = pd.get_dummies(df['mes'], prefix='mes', dtype=int)
    df = pd.concat([df, df_meses], axis=1)

    #print(df)

    return df